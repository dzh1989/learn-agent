# 第 1 节 ｜ 大模型基础认知

最小可运行代码：一次模型调用，看清楚 `content` / `usage` / `finish_reason` 三样东西。

对应文章：《大模型根本不懂你在说什么，它只是在猜下一个字》

## 运行

```bash
pip install openai

# 真实调用（需配置环境变量）
export OPENAI_API_KEY=你的KEY
export OPENAI_BASE_URL=https://api.openai.com/v1   # 国内兼容模型改这里
export OPENAI_MODEL=gpt-4o-mini
python3 call_llm.py

# 离线演示（无需任何 key，走本地 mock）
python3 call_llm.py --mock
```

## 预期输出（mock）

```
回答： [mock] 关于「用一句话解释什么是 token」：token 是模型处理文本时的最小单元，类似“字”的碎片。
用量： {'prompt_tokens': 18, 'completion_tokens': 42, 'total_tokens': 60}
结束原因： stop
```

真实调用时数字随模型与输入变化；`finish_reason` 为 `stop` 表示正常结束，`length` 表示触到上限被截断。

## 关键认知

- Token 是模型处理 / 计费的最小单元（中文约 1–2 字一个 token）。
- 账单 = 输入 token × 输入单价 + 输出 token × 输出单价。
- Context Window 是模型一次能“看到”的 token 上限，超了会截断或丢弃历史。
- Temperature 控制随机性：接近 0 更稳（适合要可解析结果），接近 1 更发散。
