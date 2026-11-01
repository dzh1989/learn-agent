"""02 上下文窗口与截断：模型一次能“看到”的 token 有上限。

两个上限要分清：
    max_tokens        单次回答最多能生成多少 token（触顶则 finish_reason=length，被截断）
    Context Window    输入 + 输出 的总 token 上限（超了要么报错，要么丢弃最早的历史）

运行：python3 02_context_window.py --mock
"""
from llm_client import get_client, approx_tokens


def main():
    client, is_mock = get_client()
    print(f"（模式：{'离线 Mock' if is_mock else '真实调用'}）\n")

    prompt = "请详细列出大模型工程师需要掌握的 30 项核心能力，每项一句话。"
    print("问题：", prompt)

    # 故意把 max_tokens 设很小，观察截断
    resp = client.create(
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=20,
    )
    print("\n返回内容：", resp.choices[0].message.content)
    print("结束原因：", resp.choices[0].finish_reason)
    print(
        "提示：finish_reason=length 表示触到 max_tokens 上限被截断；"
        "真实场景还要注意 Context Window 上限（输入+输出总 token 不能超过它）。"
    )

    print(f"\n附：一篇 2000 字中文，本仓库 mock 估算约 {approx_tokens('中' * 2000)} token")


if __name__ == "__main__":
    main()
