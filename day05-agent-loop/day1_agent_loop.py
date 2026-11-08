# -*- coding: utf-8 -*-
"""
Day 01 —— 裸写 Agent 主循环（不用任何框架）

学习目标
========
1. 理解 Agent 的本质：一个 while 循环 + 工具调用 + 结果回灌
2. 掌握三类终止条件：模型自然停止 / 轮次上限 / token 预算
3. 观察"模型自我纠错"：工具返回错误后，模型下一轮怎么反应

运行方式
========
  # Mock 模式（无 API Key 也能跑，脚本会模拟模型输出）：
  python3 day1_agent_loop.py

  # 真实模式（任意 OpenAI 兼容接口：DeepSeek / 通义 / OpenAI 均可）：
  export OPENAI_API_KEY=sk-xxx
  export OPENAI_BASE_URL=https://api.deepseek.com   # 可选，默认 DeepSeek
  export MODEL_NAME=deepseek-chat                    # 可选
  python3 day1_agent_loop.py --real

核心心智模型（面试必讲）
========================
    ┌────────────────────────────────────────────┐
    │  while True:                               │
    │      resp = LLM(messages, tools)           │      ← 模型决策
    │      if resp 没有 tool_call: break  ← 终止①  │
    │      for call in resp.tool_calls:          │
    │          result = execute(call)            │      ← 真正干活的是本地代码
    │          messages.append(tool 结果)         │      ← 回灌给模型看
    │      if 轮次超限: break              ← 终止②  │
    └────────────────────────────────────────────┘
    模型只负责"决策调哪个工具、传什么参数"，
    执行永远发生在你自己的代码里 —— 这句话面试时说出来很加分。
"""

import json
import os
import sys
import urllib.request

# ============================================================
# 第一部分：定义工具（Tool）
# 设计原则（Day 02 会展开）：名字动词化、描述写清"何时用/何时不用"、
# 参数用 JSON Schema 严格约束、错误信息对模型可读。
# ============================================================

# —— 工具的 JSON Schema 定义：这段会原样发给模型，模型据此决定怎么调 ——
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "精确计算一个四则运算表达式。当需要数学计算时必须使用本工具，"
                           "不要自己心算——大模型心算会出错。",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "四则运算表达式，只允许数字和 + - * / ( ) ，例如 '3.5 * (12 + 8)'",
                    }
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询某个城市当前的天气。仅支持国内主要城市；"
                           "查询国外城市会失败，不要用它查国外天气。",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市中文名，例如 '杭州'",
                    }
                },
                "required": ["city"],
            },
        },
    },
]

# —— 工具的本地实现：真正干活的地方，全是确定性代码 ——
_FAKE_WEATHER_DB = {
    "杭州": {"condition": "多云", "temp_c": 21, "humidity": 62},
    "上海": {"condition": "晴", "temp_c": 24, "humidity": 55},
    "北京": {"condition": "晴转多云", "temp_c": 17, "humidity": 40},
}


def tool_calculate(expression: str) -> str:
    """四则运算：用 Python 的 ast 做白名单求值，绝不用 eval（面试安全考点）。"""
    import ast
    import operator

    # 只放行四则运算节点，其他一切（函数调用、属性访问）都拒绝
    allowed_ops = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.USub: operator.neg, ast.UAdd: operator.pos,
    }

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in allowed_ops:
            return allowed_ops[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in allowed_ops:
            return allowed_ops[type(node.op)](_eval(node.operand))
        raise ValueError(f"表达式包含不允许的成分: {ast.dump(node)}")

    try:
        result = _eval(ast.parse(expression.strip(), mode="eval"))
        return json.dumps({"expression": expression, "result": result}, ensure_ascii=False)
    except ZeroDivisionError:
        # 错误信息写给模型看：说清"错在哪 + 模型该怎么改"
        return json.dumps({"error": "除数为零。请检查表达式后修正再调用。"}, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"表达式非法: {e}。只允许数字与 + - * / ( ) 。"}, ensure_ascii=False)


def tool_get_weather(city: str) -> str:
    """天气查询：用 mock 数据库模拟真实 API。"""
    if city not in _FAKE_WEATHER_DB:
        # 可读的错误信息 —— 模型读到后大概率会道歉或换问法，这就是"自我纠错"的入口
        return json.dumps(
            {"error": f"暂不支持城市 '{city}'，目前仅支持: {list(_FAKE_WEATHER_DB.keys())}"},
            ensure_ascii=False,
        )
    return json.dumps({"city": city, **_FAKE_WEATHER_DB[city]}, ensure_ascii=False)


# 工具名 -> 本地函数 的注册表。循环里通过它把"模型的选择"变成"真实的执行"
TOOL_REGISTRY = {"calculate": tool_calculate, "get_weather": tool_get_weather}


def execute_tool(call: dict) -> str:
    """执行一次工具调用，永不抛异常 —— 任何失败都转成可读的 error JSON 回灌给模型。"""
    name = call["function"]["name"]
    try:
        args = json.loads(call["function"].get("arguments") or "{}")
    except json.JSONDecodeError as e:
        return json.dumps({"error": f"参数不是合法 JSON: {e}"}, ensure_ascii=False)

    fn = TOOL_REGISTRY.get(name)
    if fn is None:
        return json.dumps({"error": f"未知工具 '{name}'"}, ensure_ascii=False)
    try:
        return fn(**args)
    except TypeError as e:
        return json.dumps({"error": f"参数不匹配: {e}"}, ensure_ascii=False)


# ============================================================
# 第二部分：模型接口（OpenAI 兼容 / Mock 双模式）
# ============================================================

def call_llm_real(messages: list, model: str = None, base_url: str = None,
                  api_key: str = None) -> dict:
    """调 OpenAI 兼容接口。用标准库 urllib，避免安装依赖。

    未传参时从环境变量读取（OPENAI_API_KEY / OPENAI_BASE_URL / MODEL_NAME）。
    缺 API Key 时直接抛清晰错误，避免在循环深处冒出难看的 KeyError。
    """
    api_key = api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("真实模式需要 OPENAI_API_KEY 环境变量，未设置则无法调用。")
    model = model or os.environ.get("MODEL_NAME", "deepseek-chat")
    base_url = (base_url or os.environ.get("OPENAI_BASE_URL", "https://api.deepseek.com")).rstrip("/")
    payload = {
        "model": model,
        "messages": messages,
        "tools": TOOL_SCHEMAS,          # 把工具 schema 告诉模型
        "tool_choice": "auto",          # Day 02 会实验 required / 指定函数 的差异
        "temperature": 0,
    }
    req = urllib.request.Request(
        url=f"{base_url}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ---------- Mock 模式：脚本化"演出"一个模型，让你离线看懂循环 ----------
# 每个场景是一个"剧本"：按顺序吐出模型的应答。
# 这样即便没有 API Key，也能完整观察循环、回灌、终止的每一步。

_SCENARIO_CALC = [  # 场景A：模型先调计算器，拿到结果后给最终回答
    {"tool_calls": [{"id": "call_1", "function": {"name": "calculate",
        "arguments": json.dumps({"expression": "3.5 * (12 + 8)"}, ensure_ascii=False)}}]},
    {"content": "3.5 × (12 + 8) = 3.5 × 20 = 70。"},
]

_SCENARIO_WEATHER_ERR = [  # 场景B：模型先查了个不存在的城市 → 收到错误 → 自我纠错换城市
    {"tool_calls": [{"id": "call_1", "function": {"name": "get_weather",
        "arguments": json.dumps({"city": "纽约"}, ensure_ascii=False)}}]},
    {"content": "抱歉，目前只支持国内主要城市的天气查询。请问您想查询杭州、上海还是北京的天气？"},
]

_SCENARIO_MULTI = [  # 场景C：一次并行调两个工具（Day 02 会细讲）
    {"tool_calls": [
        {"id": "call_1", "function": {"name": "get_weather", "arguments": json.dumps({"city": "杭州"}, ensure_ascii=False)}},
        {"id": "call_2", "function": {"name": "calculate", "arguments": json.dumps({"expression": "100 / 8"}, ensure_ascii=False)}},
    ]},
    {"content": "杭州当前多云 21°C；100 ÷ 8 = 12.5。"},
]


class MockLLM:
    """按剧本逐条返回，模拟模型行为。仅用于离线学习循环结构。"""

    def __init__(self, script: list):
        self._script = script
        self._idx = 0

    def next(self, messages: list) -> dict:
        if self._idx >= len(self._script):
            return {"content": "（Mock 剧本播完了）"}
        out = self._script[self._idx]
        self._idx += 1
        return out


class RealLLM:
    """真实模型客户端，复用 call_llm_real，对外暴露统一的 .next(messages) 接口。

    这样 run_agent 内部无需 isinstance 判断——Mock 与真实只是同一个接口的两个实现。
    """

    def next(self, messages: list) -> dict:
        return extract_message(call_llm_real(messages))


# ============================================================
# 第三部分：Agent 主循环 —— 本文件最重要的 40 行
# ============================================================

MAX_ROUNDS = 8          # 终止条件②：轮次硬上限（防死循环的第一道保险）
MAX_TOTAL_CHARS = 60000  # 终止条件③：上下文预算（简化版 token 预算）


def run_agent(user_question: str, llm, verbose: bool = True) -> str:
    """
    跑一次完整的 Agent 会话，返回最终文本回答。

    参数:
        user_question: 用户问题
        llm: 具备 .next(messages) 接口的模型客户端（真实或 Mock）
    """
    # messages 是整个循环的"唯一事实源"：模型看到的、做过的、工具返回的，全在里面
    messages = [
        {"role": "system", "content": "你是一个严谨的助手。需要精确计算时必须调用 calculate 工具，"
                                       "不要心算。回答保持简洁。"},
        {"role": "user", "content": user_question},
    ]

    for round_no in range(1, MAX_ROUNDS + 1):
        # ---------- 终止条件③：上下文预算熔断 ----------
        total_chars = sum(len(str(m)) for m in messages)
        if total_chars > MAX_TOTAL_CHARS:
            return "[熔断] 上下文超过预算，提前终止。真实场景这里应做摘要压缩而非直接放弃。"

        if verbose:
            print(f"\n{'='*62}\n◆ 第 {round_no} 轮 | 上下文 {total_chars} 字符")
            for m in messages[1:]:  # 打印时跳过 system
                role = m.get("role", "?")
                if role == "assistant" and m.get("tool_calls"):
                    for tc in m["tool_calls"]:
                        print(f"   [assistant] 调用工具 → {tc['function']['name']}({tc['function']['arguments']})")
                elif role == "tool":
                    print(f"   [tool]      返回   → {m['content']}")
                else:
                    print(f"   [{role}] {str(m.get('content'))[:60]}")

        # ---------- 调模型 ----------
        # 统一入口：Mock 与真实客户端都暴露 .next(messages)，循环里无需区分
        resp = llm.next(messages)

        # ---------- 终止条件①：模型不再要工具，给出最终回答 ----------
        tool_calls = resp.get("tool_calls")
        if not tool_calls:
            if verbose:
                print(f"   [assistant] 最终回答 → {resp.get('content')}")
            return resp.get("content", "")

        # ---------- 把模型的工具调用写回 messages（assistant 角色）----------
        assistant_msg = {"role": "assistant", "content": resp.get("content") or None,
                         "tool_calls": tool_calls}
        messages.append(assistant_msg)

        # ---------- 逐个执行工具，结果以 role=tool 回灌 ----------
        for call in tool_calls:
            result = execute_tool(call)
            if verbose:
                print(f"   [execute]   {call['function']['name']} → {result[:70]}")
            messages.append({
                "role": "tool",
                "tool_call_id": call["id"],   # 必须对应，协议要求
                "content": result,
            })
        # 循环继续：下一轮模型会看到工具结果，决定再调工具还是给最终答案

    # ---------- 终止条件②：轮次耗尽 ----------
    return "[终止] 达到最大轮次上限，防止无限循环。真实系统此处应上报并转人工。"


def extract_message(api_resp: dict) -> dict:
    """把 OpenAI 兼容响应拍平成 {'content':…, 'tool_calls':…}，统一真实/Mock 的形状。"""
    msg = api_resp["choices"][0]["message"]
    return {"content": msg.get("content"), "tool_calls": msg.get("tool_calls")}


# ============================================================
# 入口：三个场景，分别演示 正常调用 / 错误自纠 / 并行调用
# ============================================================

def main():
    use_real = "--real" in sys.argv
    print("Agent Day01 演示" + ("（真实 API 模式）" if use_real else "（Mock 离线模式，加 --real 切真实 API）"))

    scenarios = [
        ("场景A · 单工具调用：'3.5 乘以 (12+8) 等于多少？'", _SCENARIO_CALC,
         "3.5 * (12 + 8) 等于多少？请精确计算。"),
        ("场景B · 错误自我纠正：'纽约今天天气怎么样？'", _SCENARIO_WEATHER_ERR,
         "纽约今天天气怎么样？"),
        ("场景C · 一次并行调两个工具：'杭州天气 + 100除以8'", _SCENARIO_MULTI,
         "查一下杭州天气，顺便算一下 100 除以 8。"),
    ]

    for title, script, question in scenarios:
        print(f"\n\n{'#'*64}\n# {title}\n{'#'*64}")
        if use_real:
            run_agent(question, llm=RealLLM())
        else:
            run_agent(question, llm=MockLLM(script))

    print("""
【学习检查点】回答不出来说明还没吃透，回代码再看：
  1. 工具结果是以什么 role、带什么字段回灌的？（role=tool + tool_call_id）
  2. 三类终止条件分别防的是什么问题？
     ① 模型自然停止=正常收尾 ② 轮次上限=防死循环 ③ 上下文预算=防 token 爆炸
  3. execute_tool 为什么永不抛异常？
     —— 抛异常会直接杀死循环；转成可读 error 回灌，模型才有机会自我纠正。
""")


if __name__ == "__main__":
    main()
