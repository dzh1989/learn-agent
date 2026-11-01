"""day01 共享 LLM 客户端。

真实模式：走 OpenAI 兼容的 chat.completions 协议（DeepSeek / 通义 / 智谱通用，只换 base_url 与 api_key）。
离线模式：MockClient，无需任何 key 即可把 API 结构与返回字段讲清楚。

环境变量（真实模式）：
  OPENAI_API_KEY   必填
  OPENAI_BASE_URL  可选，默认 https://api.openai.com/v1
  OPENAI_MODEL     可选，默认 gpt-4o-mini

运行：python3 00_hello_llm.py --mock   # 离线
      python3 00_hello_llm.py           # 真实（需先 export OPENAI_API_KEY）
"""
from __future__ import annotations

import os
import random
import sys


def approx_tokens(text: str) -> int:
    """粗略估算 token 数，仅供离线演示与量级感受（非真实 tokenizer）。

    规则：CJK 字符按 1 token/字；连续的英文/数字按词计 1 token；标点各计 1。
    真实分词（如 cl100k_base）与这里会有偏差，仅作数量级参考。
    """
    if not text:
        return 0
    cjk = sum(1 for ch in text if "一" <= ch <= "鿿")
    rest: list[str] = []
    buf: list[str] = []
    for ch in text:
        if ch.isalnum():
            buf.append(ch)
        else:
            if buf:
                rest.append("".join(buf))
                buf = []
            if not ch.isspace():
                rest.append(ch)
    if buf:
        rest.append("".join(buf))
    return cjk + len(rest)


# ----------------------------- 离线 Mock -----------------------------
class _Msg:
    def __init__(self, content):
        self.content = content


class _Usage:
    def __init__(self, p, c):
        self.prompt_tokens = p
        self.completion_tokens = c
        self.total_tokens = p + c


class _Choice:
    def __init__(self, content, finish_reason="stop"):
        self.message = _Msg(content)
        self.finish_reason = finish_reason


class _Resp:
    def __init__(self, content, prompt_text, finish_reason="stop"):
        self.choices = [_Choice(content, finish_reason)]
        self.usage = _Usage(approx_tokens(prompt_text), approx_tokens(content))


class _Chunk:
    def __init__(self, delta):
        self.choices = [type("C", (), {"delta": type("D", (), {"content": delta})()})()]


class MockClient:
    def __init__(self, model="mock-llm"):
        self.model = model

    def _answer(self, question: str, temperature: float) -> str:
        if temperature <= 0.2:
            return (
                "大模型本质上是一个“下一个 token 预测器”：给定前面的文本，它算出概率最高的"
                "下一个 token，接到后面，再预测下一个，如此循环，直到输出结束。"
            )
        if temperature < 0.8:
            return (
                "你可以把大模型理解成一个超级自动补全：它根据上文，猜接下来最可能出现的字或词，"
                "一个接一个地往外蹦，直到说完。"
            )
        # 高温：追加随机编号，演示“发散/不稳定”（每次都不一样）
        return "说白了模型就是在做文字接龙——" + f"（示例编号 {random.randint(100, 999)}）"

    def create(self, messages, temperature=0.0, stream=False, max_tokens=None, **kwargs):
        prompt_text = "\n".join(m.get("content", "") for m in messages)
        question = messages[-1]["content"] if messages else ""
        content = self._answer(question, temperature)
        if stream:
            def gen():
                for ch in content:
                    yield _Chunk(ch)
            return gen()
        if max_tokens and approx_tokens(content) > max_tokens:
            truncated = content[: max(1, max_tokens * 2)]
            return _Resp(truncated, prompt_text, finish_reason="length")
        return _Resp(content, prompt_text, finish_reason="stop")


# ----------------------------- 真实客户端 -----------------------------
class RealClient:
    def __init__(self, api_key, base_url, model):
        from openai import OpenAI

        self._c = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def create(self, messages, temperature=0.0, stream=False, max_tokens=None, **kwargs):
        kw = dict(model=self.model, messages=messages, temperature=temperature, stream=stream)
        if max_tokens:
            kw["max_tokens"] = max_tokens
        return self._c.chat.completions.create(**kw)


def get_client():
    """默认离线 Mock；检测到有效 OPENAI_API_KEY 且未强制 --mock 时走真实。"""
    force_mock = "--mock" in sys.argv
    api_key = os.getenv("OPENAI_API_KEY")
    if (not force_mock) and api_key and api_key != "你的KEY":
        base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        return RealClient(api_key, base_url, model), False
    return MockClient(), True
