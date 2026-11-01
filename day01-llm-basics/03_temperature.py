"""03 Temperature：控制“随机性”。

    temperature 接近 0  → 每次输出稳定、可复现（适合要可解析结果：JSON、分类、抽取）
    temperature 接近 1  → 每次输出发散、有创意（适合头脑风暴、文案）

一句话：低温求“准”，高温求“活”。
运行：python3 03_temperature.py --mock
"""
from llm_client import get_client

PROMPT = "用一句话向新人解释什么是大模型。"


def run_at(temp: float, times: int):
    client, _ = get_client()
    outs = []
    for _ in range(times):
        r = client.create(messages=[{"role": "user", "content": PROMPT}], temperature=temp)
        outs.append(r.choices[0].message.content)
    return outs


def main():
    print("问题：", PROMPT, "\n")

    print("=== temperature=0（应每次几乎一致）===")
    for o in run_at(0.0, 3):
        print(" -", o)

    print("\n=== temperature=1.2（应每次不同）===")
    for o in run_at(1.2, 3):
        print(" -", o)

    print("\n结论：要可解析/稳定的结果用低温度；要创意/发散用高温度。")


if __name__ == "__main__":
    main()
