# -*- coding: utf-8 -*-
"""
Day 02 —— 演示脚本：工具注册中心 V0

运行:  python3 day2_function_calling.py
（零依赖，仅标准库；无需 API Key，全程用 mock 工具演示）

覆盖 Day 02 四个验收点：
  ✅ 参数缺失 / 类型错误 / 非法枚举值 都能被「执行前」拦截
  ✅ 并行工具结果能正确对应原始 tool_call_id
  ✅ 工具错误不会直接暴露内部堆栈给模型或用户
  ✅ 统一结果格式 success / data / error / retryable
"""

import json
import os
import sys

# 让脚本无论从哪运行都能 import 到 agent.tools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agent.tools.registry import ToolRegistry, ToolResult  # noqa: E402


# ============================================================
# 两个互不依赖的 mock 工具
# ============================================================
_WEATHER = {"杭州": {"condition": "多云", "temp_c": 21}, "北京": {"condition": "晴", "temp_c": 17}}
_KB = {
    "agent loop": "Agent 循环是一个 while 循环：调模型→解析 tool_calls→执行→回灌。",
    "mcp": "MCP 是模型与外部工具之间的标准协议，类比 USB-C。",
}


def get_weather(city: str) -> dict:
    if city not in _WEATHER:
        # 业务层的「预期失败」：返回可读错误，由注册表收到 success=False
        raise KeyError(f"暂不支持城市 '{city}'")
    return _WEATHER[city]


def search_knowledge(query: str) -> dict:
    # 模拟一个会「意外崩溃」的工具（除零），用来演示错误隔离
    if query == "__boom__":
        1 / 0
    hit = _KB.get(query)
    if hit is None:
        raise KeyError(f"知识库未收录 '{query}'")
    return {"query": query, "answer": hit}


def build_registry() -> ToolRegistry:
    reg = ToolRegistry()
    reg.register(
        name="get_weather",
        description="查询国内城市当前天气。参数 city 必须是已支持的城市之一。",
        parameters={
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市中文名，如 '杭州' / '北京'"}
            },
            "required": ["city"],
        },
        func=get_weather,
        permission="tool:weather:read",
    )
    reg.register(
        name="search_knowledge",
        description="在知识库检索 Agent 相关概念。query 取 'agent loop' 或 'mcp'。",
        parameters={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "enum": ["agent loop", "mcp"],
                    "description": "检索关键词，仅支持枚举内的值",
                }
            },
            "required": ["query"],
        },
        func=search_knowledge,
        permission="tool:kb:read",
    )
    return reg


def _print(title: str):
    print(f"\n{'#'*64}\n# {title}\n{'#'*64}")


def demo_validation(reg: ToolRegistry):
    """验收点①：执行前拦截坏参数。"""
    _print("验收① 参数校验（缺字段 / 类型错 / 非法枚举）")
    cases = [
        ("缺必填 city", {"id": "c1", "function": {"name": "get_weather", "arguments": "{}"}}),
        ("类型错：city 传数字", {"id": "c2", "function": {"name": "get_weather", "arguments": json.dumps({"city": 123})}}),
        ("非法枚举：query 不在枚举内", {"id": "c3", "function": {"name": "search_knowledge", "arguments": json.dumps({"query": "rag"})}}),
        ("正常：合法参数", {"id": "c4", "function": {"name": "get_weather", "arguments": json.dumps({"city": "杭州"})}}),
    ]
    for label, call in cases:
        res = reg.execute(call)
        print(f"  · {label}\n    → {res}")


def demo_tool_choice():
    """演示 tool_choice 三种模式：只是「请求构造」的差异，不影响执行。"""
    _print("tool_choice 三种模式（请求层差异，这里用 Mock 说明）")
    print("  auto     : 模型自己决定调不调、调哪个（默认，最常用）")
    print("  required : 强制模型必须返回一个 tool_call（适合『这步一定得用工具』）")
    print("  指定工具 : {\"type\":\"function\",\"function\":{\"name\":\"get_weather\"}}（锁定唯一工具）")
    print("  代码对照：")
    print('    payload["tool_choice"] = "auto"')
    print('    payload["tool_choice"] = "required"')
    print('    payload["tool_choice"] = {"type":"function","function":{"name":"get_weather"}}')
    print("  面试点：required 用于『必须落地一个动作』；指定工具用于『流程已锁定下一步』。")


def demo_parallel(reg: ToolRegistry):
    """验收点②：并行执行 + tool_call_id 配对。"""
    _print("验收② 并行工具调用（结果按 tool_call_id 配对）")
    calls = [
        {"id": "call_weather", "function": {"name": "get_weather", "arguments": json.dumps({"city": "杭州"})}},
        {"id": "call_kb", "function": {"name": "search_knowledge", "arguments": json.dumps({"query": "mcp"})}},
    ]
    results = reg.execute_many(calls)
    for call_id, res_json in results:
        res = json.loads(res_json)
        print(f"  · tool_call_id={call_id:<12} success={res['success']} data={res.get('data')}")
    print("  ⇒ 上层把每个 result 以 role=tool + 对应 tool_call_id 回灌，模型才能正确配对。")


def demo_error_isolation(reg: ToolRegistry):
    """验收点③：工具崩溃不暴露堆栈。

    注意：__boom__ 那种会被枚举校验拦下，到不了崩溃。要真正测『内部崩溃』，
    得用一个『参数合法、但函数体里炸了』的工具。
    """
    _print("验收③ 错误隔离（工具内部崩溃 → 只给可读错误，不给 traceback）")

    def crash_tool(reason: str) -> dict:
        # 参数合法（通过校验），但函数体里故意抛异常
        raise RuntimeError(f"数据库连接失败: {reason}")  # 模拟真实内部故障

    # 临时注册一个会崩的工具，专测错误隔离
    reg.register(
        name="crash_demo",
        description="测试用：必定内部崩溃的工具。",
        parameters={"type": "object", "properties": {"reason": {"type": "string"}}, "required": ["reason"]},
        func=crash_tool,
    )
    call = {"id": "c_boom", "function": {"name": "crash_demo", "arguments": json.dumps({"reason": "timeout"})}}
    res = reg.execute(call)
    print(f"  模型/用户看到 → {res}")
    print("  内部 RuntimeError 的 traceback 已被吞掉，只暴露『可重试 + 请调整参数』。")
    print("  （真实系统应把 traceback 写日志，绝不该回灌给模型或终端用户）")

    # 顺带演示：枚举校验确实先于执行——坏参数根本进不到工具内部
    bad = {"id": "c_bad", "function": {"name": "search_knowledge", "arguments": json.dumps({"query": "__boom__"})}}
    print(f"  对照·坏枚举被拦下 → {reg.execute(bad)}")


def demo_unified_format(reg: ToolRegistry):
    """验收点④：统一结果格式。"""
    _print("验收④ 统一结果格式 success/data/error/retryable")
    print("  ToolResult.ok(data)      → {\"success\":true,\"data\":...,\"error\":null,\"retryable\":false}")
    print("  ToolResult.fail(err,True)→ {\"success\":false,\"data\":null,\"error\":\"...\",\"retryable\":true}")
    print("  全部工具收口成同一结构，模型才好稳定解析、调度层才好决定重试。")


def main():
    reg = build_registry()
    print("工具注册中心已就绪，已注册:", reg.names())
    print("发给模型的 tools schema 数量:", len(reg.tool_schemas()))
    demo_validation(reg)
    demo_tool_choice()
    demo_parallel(reg)
    demo_error_isolation(reg)
    demo_unified_format(reg)
    print("\n✅ Day 02 演示结束。回顾四个验收点是否都通过。\n")


if __name__ == "__main__":
    main()
