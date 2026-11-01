"""00 最小调用：看清一次 API 返回的三样东西。

一次对话补全（chat.completions.create）返回的对象里，最该记住三个字段：
    choices[0].message.content   模型“说了什么”
    usage                         花了多少 token（你的账单来源）
    choices[0].finish_reason      为什么停（stop=正常结束，length=被截断）

运行：python3 00_hello_llm.py --mock
"""
from llm_client import get_client


def main():
    client, is_mock = get_client()
    print(f"（模式：{'离线 Mock' if is_mock else '真实调用'}）\n")

    resp = client.create(
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
