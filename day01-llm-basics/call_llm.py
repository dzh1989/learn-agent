"""第 1 节 · 大模型基础认知：一次最小可运行调用。

目标：看清一次 API 调用返回的三样东西 ——
    content       模型说了啥
    usage         花了多少 token（你的成本）
    finish_reason 为什么停（stop 正常 / length 被截断）

运行：
    pip install openai

    # 真实调用（需配置环境变量）
    export OPENAI_API_KEY=你的KEY
    export OPENAI_BASE_URL=https://api.openai.com/v1   # 国内兼容模型改这里
    export OPENAI_MODEL=gpt-4o-mini
    python3 call_llm.py

    # 离线演示（无需任何 key，走本地 mock）
    python3 call_llm.py --mock
"""

import os
import sys


class MockClient:
    """本地 mock，无需真实 key 即可演示「一次调用 + usage 结构」。

    国内模型（DeepSeek / 通义 / 智谱）也走同一套 chat.completions 接口，
    只换 base_url 和 api_key，下面的 MockClient 仅用于离线验证代码逻辑。
    """

    class _Msg:
        def __init__(self, content):
            self.content = content

    class _Usage:
        prompt_tokens = 18
        completion_tokens = 42
        total_tokens = 60

    class _Choice:
        finish_reason = "stop"

        def __init__(self, content):
            self.message = MockClient._Msg(content)

    class _Resp:
        def __init__(self, content):
            self.choices = [MockClient._Choice(content)]
            self.usage = MockClient._Usage()

    class _Completions:
        def create(self, model, messages, temperature=0.2, **kwargs):
            question = messages[-1]["content"] if messages else ""
            answer = (
                f"[mock] 关于「{question}」："
                "token 是模型处理文本时的最小单元，类似“字”的碎片。"
            )
            return MockClient._Resp(answer)

    def __init__(self, **kwargs):
        self.chat = type("Chat", (), {"completions": self._Completions()})()


def real_client():
    from openai import OpenAI

    return OpenAI(
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        api_key=os.getenv("OPENAI_API_KEY", "你的KEY"),
    )


def main():
    use_mock = "--mock" in sys.argv
    client = MockClient() if use_mock else real_client()

    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": "用一句话解释什么是 token"}],
        temperature=0.2,
    )

    print("回答：", resp.choices[0].message.content)
    u = resp.usage
    print(
        "用量：",
        {
            "prompt_tokens": u.prompt_tokens,
            "completion_tokens": u.completion_tokens,
            "total_tokens": u.total_tokens,
        },
    )
    print("结束原因：", resp.choices[0].finish_reason)


if __name__ == "__main__":
    main()
