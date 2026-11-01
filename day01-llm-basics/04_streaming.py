"""04 流式输出：token 一个一个吐出来，体验“生成中”。

流式（stream=True）让首字延迟极低：用户边想边出，是大模型产品的标配体验。
真实模式与 Mock 都支持；Mock 按字符逐个 yield。
运行：python3 04_streaming.py --mock
"""
from llm_client import get_client


def main():
    client, is_mock = get_client()
    print(f"（模式：{'离线 Mock' if is_mock else '真实调用'}）\n")

    print("模型：", end="", flush=True)
    stream = client.create(
        messages=[{"role": "user", "content": "用三句话讲讲 token、context window、temperature 的关系"}],
        temperature=0.5,
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        print(delta, end="", flush=True)
    print("\n\n（流式让首字延迟极低，用户边想边出，是大模型产品的标配体验。）")


if __name__ == "__main__":
    main()
