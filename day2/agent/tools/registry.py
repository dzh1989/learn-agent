# -*- coding: utf-8 -*-
"""
Day 02 —— 工具注册中心 V0（零依赖，仅用标准库）

学习目标
========
1. 用「注册表」统一管理工具：名字 / 描述 / 参数 Schema / 执行函数 / 权限要求
2. 在「执行之前」拦截坏参数：缺字段、类型错、非法枚举值都不该进到工具内部
3. 并行工具调用：多个互不依赖的 tool_calls，结果必须按 tool_call_id 一一对应
4. 统一结果格式：success / data / error / retryable，错误绝不把内部堆栈暴露给模型

为什么不用 Pydantic？
===================
生产环境强烈建议用 Pydantic（声明式、报错友好、自动生成 JSON Schema）。
但本仓库坚持「裸写、零依赖、能离线跑」，所以这里手写一个最小 JSON Schema 校验器——
它本身就是 Day 02 最重要的学习素材：你写完就知道 Pydantic 替你省了多少事。

运行方式
========
  from agent.tools.registry import ToolRegistry, ToolResult
  # 见同目录 day2_function_calling.py 的完整演示
"""

import json
import traceback
from concurrent.futures import ThreadPoolExecutor


# ============================================================
# 统一结果格式：所有工具执行完都长这样
# ============================================================
class ToolResult:
    """工具执行结果。无论成功失败，都收口成这个结构再回灌给模型。

    - success : 是否成功
    - data    : 成功时的业务数据（任意可 json 化的对象）
    - error   : 失败时的可读错误信息（写给模型看，不是写给开发者看）
    - retryable: 该错误是否可重试（模型/调度层据此决定要不要再试一次）
    """

    def __init__(self, success, data=None, error=None, retryable=False):
        self.success = success
        self.data = data
        self.error = error
        self.retryable = retryable

    def to_json(self) -> str:
        return json.dumps(
            {
                "success": self.success,
                "data": self.data,
                "error": self.error,
                "retryable": self.retryable,
            },
            ensure_ascii=False,
        )

    @classmethod
    def ok(cls, data) -> "ToolResult":
        return cls(success=True, data=data)

    @classmethod
    def fail(cls, error, retryable=False) -> "ToolResult":
        return cls(success=False, error=error, retryable=retryable)


# ============================================================
# 最小 JSON Schema 校验器（覆盖 Day 02 需要的三种拦截）
# ============================================================
def validate_args(schema: dict, args: dict) -> "tuple[bool, str]":
    """校验工具参数。返回 (是否通过, 错误信息)。

    支持的约束：
      - required  : 必填字段是否缺失
      - type      : 字段类型是否匹配（string / number / integer / boolean / object / array）
      - enum      : 枚举值是否合法
    未通过时，错误信息写成「模型能读懂并自行修正」的口吻，而非抛异常。
    """
    props = schema.get("properties", {})
    required = schema.get("required", [])

    # 1) 必填项缺失
    missing = [k for k in required if k not in args]
    if missing:
        return False, f"缺少必填参数: {missing}。请提供这些字段后再调用。"

    # 2) 类型 / 枚举校验（只校验「实际传了」的字段）
    for name, val in args.items():
        spec = props.get(name)
        if spec is None:
            # 不在 schema 里的字段：严格模式下应拒绝，这里给出提示
            return False, f"参数 '{name}' 不在工具定义中，请检查工具名或去掉该字段。"
        want_type = spec.get("type")
        if want_type and not _type_match(want_type, val):
            return False, (
                f"参数 '{name}' 类型错误：期望 {want_type}，实际收到 {type(val).__name__}。"
                f"请按工具描述修正后重试。"
            )
        enum = spec.get("enum")
        if enum is not None and val not in enum:
            return False, (
                f"参数 '{name}' 取值 '{val}' 不合法。合法取值为: {enum}。"
            )
    return True, ""


_TYPE_MAP = {
    "string": str,
    "boolean": bool,
    "object": dict,
    "array": list,
    "integer": int,
    "number": (int, float),
}


def _type_match(want: str, val) -> bool:
    # bool 是 int 的子类，先排除，避免 True 被当成 integer
    if want == "integer" and isinstance(val, bool):
        return False
    if want == "number" and isinstance(val, bool):
        return False
    allowed = _TYPE_MAP.get(want)
    if allowed is None:
        return True  # 未知类型声明不拦截
    return isinstance(val, allowed)


# ============================================================
# 工具注册中心
# ============================================================
class ToolRegistry:
    """工具的集中注册与执行入口。

    每个工具登记：name / description / parameters(JSON Schema) / func / permission。
    - func 的签名应是 **kwargs，参数由注册表从模型给的 arguments 里解出来。
    - permission 是可选的权限要求字符串，执行前可据此做鉴权（Day 04 会展开）。
    """

    def __init__(self):
        self._tools = {}

    def register(self, name, description, parameters, func, permission=None):
        if name in self._tools:
            raise ValueError(f"工具 '{name}' 已存在，不能重复注册")
        self._tools[name] = {
            "name": name,
            "description": description,
            "parameters": parameters,
            "func": func,
            "permission": permission,
        }

    def names(self):
        return list(self._tools.keys())

    def schema_of(self, name) -> dict:
        """生成发给模型的 tools 列表里那一项（OpenAI 兼容格式）。"""
        t = self._tools[name]
        return {
            "type": "function",
            "function": {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["parameters"],
            },
        }

    def tool_schemas(self) -> list:
        """全部工具的 schema，直接拼进 LLM 请求的 tools 字段。"""
        return [self.schema_of(n) for n in self._tools]

    def _authorize(self, name) -> "tuple[bool, str]":
        """占位鉴权：Day 04 会接真实 Token / 最小权限。这里默认放行。"""
        return True, ""

    def execute(self, call: dict) -> str:
        """执行「单个」工具调用，返回 ToolResult.to_json() 字符串。

        call 形如模型给的 tool_calls 元素：
            {"id": "call_1", "function": {"name": ..., "arguments": "<json 字符串>"}}
        绝不向外抛异常：任何失败（参数坏 / 工具崩 / 未授权）都收口成可读 error。
        """
        name = call["function"]["name"]
        call_id = call.get("id")

        tool = self._tools.get(name)
        if tool is None:
            return ToolResult.fail(f"未知工具 '{name}'，可用工具: {self.names()}").to_json()

        # 鉴权
        ok, why = self._authorize(name)
        if not ok:
            return ToolResult.fail(f"无权限调用 '{name}'：{why}").to_json()

        # 解析参数（模型给的是 JSON 字符串，可能不合格）
        try:
            args = json.loads(call["function"].get("arguments") or "{}")
        except json.JSONDecodeError as e:
            return ToolResult.fail(f"参数不是合法 JSON: {e}。请重新生成 arguments。", retryable=True).to_json()

        if not isinstance(args, dict):
            return ToolResult.fail("arguments 必须是 JSON 对象（键值对）。", retryable=True).to_json()

        # 执行前校验（拦截缺字段 / 类型错 / 非法枚举）
        passed, err = validate_args(tool["parameters"], args)
        if not passed:
            return ToolResult.fail(err, retryable=True).to_json()

        # 真正执行；工具内部崩了也不能炸到主循环
        try:
            result = tool["func"](**args)
            return ToolResult.ok(result).to_json()
        except Exception:
            # 关键：只给模型「发生了什么、能否重试」，绝不给 traceback / 内部堆栈
            inner = traceback.format_exc()
            # 真实系统应把 inner 写日志，绝不该回灌给模型或终端用户
            return ToolResult.fail("工具执行时发生内部错误，请调整参数后重试。", retryable=True).to_json()

    def execute_many(self, calls: list, max_workers: int = 4) -> list:
        """并行执行多个「互不依赖」的工具调用。

        返回顺序与输入一致，每项带 call_id，便于上层按 tool_call_id 配对回灌。
        """
        def _one(call):
            return call.get("id"), self.execute(call)

        if len(calls) <= 1 or max_workers == 1:
            return [_one(c) for c in calls]

        with ThreadPoolExecutor(max_workers=min(max_workers, len(calls))) as ex:
            return list(ex.map(_one, calls))
