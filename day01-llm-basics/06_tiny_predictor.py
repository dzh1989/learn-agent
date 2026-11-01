"""06 从零实现一个“下一个字预测器”（bigram 字符模型）。

不需要任何大模型、不需要联网。用几十行代码证明一件事：
    大模型的核心机制，就是“根据前文，预测概率最高的下一个字”，然后接龙。

我们在一小段文本上统计「每个字后面最常跟哪个字」，就得到一个最简单的语言模型。
GPT 做的事与下面完全同源，只是它用上亿参数的 Transformer、在万亿 token 上训练，
把“概率”估得准得多。

运行：python3 06_tiny_predictor.py
"""
from __future__ import annotations

import random
from collections import Counter, defaultdict

CORPUS = (
    "大模型在猜下一个字。它不懂语言，只会算概率。"
    "下一个字由前文决定。前文越长，猜得越准。"
    "token 是模型看见的最小单位。模型把字切成 token 再算概率。"
    "温度越高，模型越爱选冷门的字。温度越低，模型越保守。"
)


def build_model(text: str):
    """统计 (前一个字 -> 后一个字) 的次数，并转成概率分布。"""
    counts = defaultdict(Counter)
    for i in range(len(text) - 1):
        a, b = text[i], text[i + 1]
        counts[a][b] += 1
    model = {}
    for a, c in counts.items():
        total = sum(c.values())
        model[a] = {b: n / total for b, n in c.items()}
    return model


def predict_next(model, context_char: str, top: int = 5):
    dist = model.get(context_char)
    if not dist:
        return None
    return sorted(dist.items(), key=lambda kv: kv[1], reverse=True)[:top]


def generate(model, seed: str, length: int = 25, temperature: float = 1.0) -> str:
    out = seed
    cur = seed[-1]
    for _ in range(length):
        dist = model.get(cur)
        if not dist:
            break
        chars = list(dist.keys())
        probs = list(dist.values())
        if temperature <= 0.01:
            nxt = chars[0]  # 贪心：永远选概率最高的
        else:
            scaled = [p ** (1.0 / temperature) for p in probs]  # 温度缩放
            s = sum(scaled)
            probs = [x / s for x in scaled]
            nxt = random.choices(chars, weights=probs, k=1)[0]
        out += nxt
        cur = nxt
    return out


def main():
    random.seed(7)
    model = build_model(CORPUS)
    print("训练语料：", CORPUS[:40], "...（共 %d 字）" % len(CORPUS))

    print("\n--- 演示 1：给定前文「大」，下一个字的概率分布 ---")
    for ch, p in (predict_next(model, "大") or []):
        print(f"  {ch!r}: {p:.2%}")

    print("\n--- 演示 2：从「大模型」开始接龙（贪心，temperature=0，结果固定）---")
    print("  ", generate(model, "大模型", length=20, temperature=0.0))

    print("\n--- 演示 3：从「大模型」开始接龙（temperature=1.5，更发散）---")
    print("  ", generate(model, "大模型", length=20, temperature=1.5))

    print(
        "\n核心结论：上面的“接龙”和 GPT 是同一件事，"
        "区别只是真实大模型把“概率”估得准得多、能处理更长的前文。"
        "\n（bigram 模型在更短的语料上很容易陷入死循环，"
        "这是它最大的局限；真实大模型靠海量参数与超长上下文才解决了这个问题。）"
    )


if __name__ == "__main__":
    main()
