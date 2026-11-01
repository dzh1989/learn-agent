"""01 Token 与成本：看清“模型在按字收费”。

Token 是模型处理与计费的最小单元。同一段文字，英文、中文、代码的 token 数差异很大：
    英文近似“词”、中文近似“字”、代码因符号多而更碎。

有 tiktoken 时能看到真实切分；没有就退化为估算（pip install tiktoken）。
运行：python3 01_tokens_and_cost.py --mock
"""
from llm_client import approx_tokens

# 每 1K token 价格（示意，以各模型官网为准）
PRICE = {"gpt-4o-mini": {"in": 0.00015, "out": 0.0006}}


def show_with_tiktoken(text: str) -> int:
    import tiktoken

    enc = tiktoken.get_encoding("cl100k_base")
    ids = enc.encode(text)
    toks = [enc.decode([i]) for i in ids]
    print(f"字符数：{len(text)}  真实 token 数：{len(ids)}")
    print("token 切分：", " | ".join(toks))
    return len(ids)


def show_approx(text: str) -> int:
    n = approx_tokens(text)
    print(f"字符数：{len(text)}  估算 token 数：{n}（approx，非真实 tokenizer）")
    return n


def main():
    print("（真实 tokenizer 用 tiktoken；未安装时退化为估算，pip install tiktoken 可看真实切分）\n")
    samples = {
        "英文": "Token is the smallest unit an LLM processes.",
        "中文": "Token 是大模型处理文本时的最小单元。",
        "代码": "def add(a, b):\n    return a + b",
    }
    for label, text in samples.items():
        print(f"【{label}】{text}")
        try:
            n = show_with_tiktoken(text)
        except Exception:
            n = show_approx(text)
        cost_in = n / 1000 * PRICE["gpt-4o-mini"]["in"]
        print(f"若作为输入，按 gpt-4o-mini 估算成本约 ${cost_in:.6f}\n")


if __name__ == "__main__":
    main()
