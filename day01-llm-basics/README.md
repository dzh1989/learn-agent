# 第 1 节 · 大模型基础认知（day01-llm-basics）

用手写代码把 LLM 的几个核心概念**跑一遍**，而不是背定义。全部脚本支持离线 Mock，无需任何 key 即可演示；配置 `OPENAI_API_KEY` 后自动切真实调用（DeepSeek / 通义 / 智谱等兼容 OpenAI 协议的模型只需改 `OPENAI_BASE_URL`）。

> 本节不写背景故事，只讲 LLM 本身。对应文章与学习手册另出。

## 一句话核心

**大模型本质上是一个“下一个 token 预测器”**：给它前文，它算出概率最高的下一个 token，接上去，再预测下一个，如此循环，直到说完。`06_tiny_predictor.py` 用几十行代码把这个机制从零复现了一遍。

## 文件清单（由浅入深）

| 文件 | 讲什么 | 你会看到 |
|---|---|---|
| `llm_client.py` | 共享客户端：真实 + Mock，统一 `get_client()` | —（被其他脚本 import） |
| `00_hello_llm.py` | 一次最小调用，看 `content / usage / finish_reason` | 三样返回字段 |
| `01_tokens_and_cost.py` | Token 是计费最小单元，中/英/代码差异大 | 文本如何被切分、估算成本 |
| `02_context_window.py` | 上下文窗口与截断（`max_tokens` / Context Window） | `finish_reason=length` 被截断 |
| `03_temperature.py` | 温度控制随机性，低温稳、高温发散 | 同 prompt 不同温度的输出差异 |
| `04_streaming.py` | 流式输出，首字延迟低 | token 一个一个吐出来 |
| `05_structured_output.py` | 让模型返回可解析 JSON（Agent 的铺垫） | 自然语言 → 对象 |
| `06_tiny_predictor.py` | **从零实现“下一个字预测器”**（重点） | 概率接龙，与 GPT 同源 |

## 运行

```bash
pip install openai          # 真实调用才需要；Mock 不需要
# 可选：pip install tiktoken  # 看真实 token 切分（否则退化估算）

# 离线演示（无需任何 key）
python3 00_hello_llm.py --mock
python3 01_tokens_and_cost.py --mock
python3 02_context_window.py --mock
python3 03_temperature.py --mock
python3 04_streaming.py --mock
python3 05_structured_output.py --mock
python3 06_tiny_predictor.py          # 纯本地，不需要 --mock

# 真实调用（先配置环境变量）
export OPENAI_API_KEY=你的KEY
export OPENAI_BASE_URL=https://api.openai.com/v1   # 国内模型改这里，如 https://api.deepseek.com/v1
export OPENAI_MODEL=gpt-4o-mini
python3 00_hello_llm.py
```

## 预期输出（离线 Mock 示例）

`00_hello_llm.py`
```
（模式：离线 Mock）

回答： [mock] ...token 是模型处理文本时的最小单元...
用量： {'prompt_tokens': 18, 'completion_tokens': 42, 'total_tokens': 60}
结束原因： stop
```

`06_tiny_predictor.py`
```
训练语料： 大模型在猜下一个字。大模型不懂语言...（共 74 字）

--- 演示 1：给定前文「大」，下一个字的概率分布 ---
  '模': 100.00%

--- 演示 2：从「大」开始接龙（贪心，temperature=0，结果固定）---
   大模型在猜下一个字。大模型不懂语言，它只会算概率。下一个字由前文决定...

--- 演示 3：从「大」开始接龙（temperature=1.5，更发散）---
   大模型在猜下一个字。大模型不懂语言...（分叉处随机）

核心结论：上面的“接龙”和 GPT 是同一件事...
```

真实调用时数字随模型与输入变化；`finish_reason` 为 `stop` 表示正常结束，`length` 表示触到上限被截断。

## 关键认知（验收点）

- Token 是模型处理 / 计费的最小单元（中文约 1–2 字一个 token，英文约 1 词，代码更碎）。
- 账单 = 输入 token × 输入单价 + 输出 token × 输出单价。
- Context Window 是模型一次能“看到”的 token 上限，超了会截断或丢弃历史。
- Temperature 控制随机性：接近 0 更稳（适合可解析结果），接近 1 更发散（适合创意）。
- 流式输出让首字延迟极低，是大模型产品标配体验。
- 结构化输出（JSON / Function Calling）让模型输出能被代码消费——这是 Agent 的入口。

## 下一步

`../day02-prompt/`（Prompt Engineering）：怎么把“前文”写得更会引导模型。
