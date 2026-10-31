# learn-agent

> **35 岁阿里后端，用 30 天把自己重训成 Agent 工程师 —— 配套学习代码库。**

本仓库是公众号系列 **「30 天把自己重训成 Agent 工程师」**（公众号：**溪月散人**）的
**代码落地**。计划本身见 [`AI-Agent-30天学习执行手册.html`](AI-Agent-30天学习执行手册.html)；
这里把计划每天变成可运行、可 review、可提交的真实产物。

## 这个仓库怎么用

- **每天一个目录** `dayN/`，里面包含当天全部学习产物。
- **每目录三件套**：① 可运行代码（零依赖，`python3 xxx.py` 直接跑）；
  ② 时序图 / 架构图（GitHub 用 Mermaid，公众号用交互式 HTML）；
  ③ `README.md`（目标 / 资料 / 验收 / 面试题）。
- **进度驱动**：下面的进度表会自动识别哪些 `dayN/` 已建，已建的标 ✅ 并链接。
- **改计划后重跑**：编辑源稿 Markdown，执行 `python3 scripts/gen_readme.py` 即可刷新本文件。

## 关联资源

- 30 天学习计划（自包含 HTML，可浏览器看 / 打印）：[`AI-Agent-30天学习执行手册.html`](AI-Agent-30天学习执行手册.html)
- 同名公众号连载：搜索 **溪月散人**（《30 天把自己重训成 Agent 工程师》）

---

## 学习进度

| Day | 周 | 主题 | 代码目录 | 状态 |
|----|----|------|---------|------|
| [Day 1](day1/) | 第1周 | Agent Loop：从模型调用到工具执行 | [day1/](day1/) | ✅ 已完成 |
| [Day 2](day2/) | 第1周 | Function Calling 与工具设计 | [day2/](day2/) | ✅ 已完成 |
| Day 3 | 第1周 | MCP 协议与工具接入架构 | day3/（待建） | ⬜ 待产 |
| Day 4 | 第1周 | MCP 工程化与安全 | day4/（待建） | ⬜ 待产 |
| Day 5 | 第1周 | Agent 范式：ReAct、Plan-and-Execute、Reflexion | day5/（待建） | ⬜ 待产 |
| Day 6 | 第1周 | 上下文工程与 LLM 基础 | day6/（待建） | ⬜ 待产 |
| Day 7 | 第1周 | 第一周集成与模拟面试 | day7/（待建） | ⬜ 待产 |
| Day 8 | 第2周 | LangGraph 核心机制 | day8/（待建） | ⬜ 待产 |
| Day 9 | 第2周 | Checkpoint、恢复与 Human-in-the-loop | day9/（待建） | ⬜ 待产 |
| Day 10 | 第2周 | RAG 全链路 | day10/（待建） | ⬜ 待产 |
| Day 11 | 第2周 | RAG 进阶与质量评估 | day11/（待建） | ⬜ 待产 |
| Day 12 | 第2周 | Memory 记忆体系 | day12/（待建） | ⬜ 待产 |
| Day 13 | 第2周 | Evaluation：Agent 评测体系 | day13/（待建） | ⬜ 待产 |
| Day 14 | 第2周 | 可靠性、故障注入与成本优化 | day14/（待建） | ⬜ 待产 |
| Day 15 | 第3周 | 系统设计答题模板 | day15/（待建） | ⬜ 待产 |
| Day 16 | 第3周 | 系统设计题 1：企业级 Agent 平台 | day16/（待建） | ⬜ 待产 |
| Day 17 | 第3周 | 系统设计题 2：企业客服 Agent | day17/（待建） | ⬜ 待产 |
| Day 18 | 第3周 | 系统设计题 3：代码 Agent | day18/（待建） | ⬜ 待产 |
| Day 19 | 第3周 | 系统设计题 4：多 Agent 协作 | day19/（待建） | ⬜ 待产 |
| Day 20 | 第3周 | 系统设计题 5：Agent Gateway / 开放平台 | day20/（待建） | ⬜ 待产 |
| Day 21 | 第3周 | 系统设计串讲与复盘 | day21/（待建） | ⬜ 待产 |
| Day 22 | 第4周 | 主项目完整集成 | day22/（待建） | ⬜ 待产 |
| Day 23 | 第4周 | 项目指标、故障和安全复盘 | day23/（待建） | ⬜ 待产 |
| Day 24 | 第4周 | 项目故事：2 分钟、10 分钟、30 分钟 | day24/（待建） | ⬜ 待产 |
| Day 25 | 第4周 | Java / 分布式 / Coding 复习 | day25/（待建） | ⬜ 待产 |
| Day 26 | 第4周 | 模拟面试 1：技术原理与项目深挖 | day26/（待建） | ⬜ 待产 |
| Day 27 | 第4周 | 模拟面试 2：系统设计白板 | day27/（待建） | ⬜ 待产 |
| Day 28 | 第4周 | 英文面试与行为面试 | day28/（待建） | ⬜ 待产 |
| Day 29 | 第4周 | 简历、岗位匹配与定级证据 | day29/（待建） | ⬜ 待产 |
| Day 30 | 第4周 | 最终模拟面试与投递准备 | day30/（待建） | ⬜ 待产 |

---

## 30 天学习计划（总纲）

## 第 1 周：Agent 底层原理与工具编排

目标：不依赖 Agent 框架，能够独立写出 Agent 核心循环；理解 Function Calling、MCP、ReAct、上下文工程，并启动主项目。

### Day 1｜Agent Loop：从模型调用到工具执行
**时间：90～120 分钟**

学习：
- 理解 LLM、Tool、Agent、Environment 的关系。
- 理解一次 Agent 执行的完整生命周期。
- 学习模型返回 tool_calls 后，应用层如何执行工具并回传结果。
- 理解 Agent 终止条件：无工具调用、达到最大轮次、显式完成信号。

资料：
- OpenAI Function Calling：https://platform.openai.com/docs/guides/function-calling
- Anthropic Building Effective Agents：https://www.anthropic.com/engineering/building-effective-agents

代码：
- 创建 `agent-platform-lite/`。
- 编写 `agent/runtime/loop.py`。
- 定义 calculator 和 competitor_search_mock 两个工具。
- 实现模型调用 → 解析 tool_call → 执行工具 → 回灌结果 → 再次请求模型。
- 增加最大轮次、总 Token 预算和重复工具调用检测。

产出：
- 一个可运行的 Agent Loop。
- 一张 Agent 执行时序图。

验收：
- 能完成至少一次工具调用和两轮连续工具调用。
- 模型返回错误参数时，不发生程序崩溃。
- 达到最大轮次时能返回明确的终止状态。

面试题：
1. Agent 和普通 LLM Chat 有什么区别？
2. Agent Loop 的核心流程是什么？
3. 如何防止 Agent 无限循环？
4. 工具执行失败后，应该由模型重试还是应用层重试？

### Day 2｜Function Calling 与工具设计
**时间：90～120 分钟**

学习：
- tool_choice 的 auto、required、指定工具模式。
- JSON Schema 与参数校验。
- 并行工具调用与串行依赖。
- 结构化输出和工具调用的区别。
- 工具粒度如何设计。

资料：
- OpenAI Function Calling：https://platform.openai.com/docs/guides/function-calling
- Pydantic：https://docs.pydantic.dev/

代码：
- 编写 `agent/tools/registry.py`。
- 建立工具注册表：工具名称、描述、参数 Schema、执行函数、权限要求。
- 为工具参数增加 Pydantic 校验。
- 实现两个互不依赖的工具并行调用。
- 实现工具执行结果的统一格式：success、data、error、retryable。

产出：
- 工具注册中心 V0。
- 《工具设计规范》一页。

验收：
- 参数缺失、类型错误、非法枚举值都能被拦截。
- 并行工具结果能正确对应原始 tool_call_id。
- 工具错误不会直接暴露内部堆栈给模型或用户。

面试题：
1. 如何设计一个模型不容易误用的工具？
2. Function Calling 和普通 HTTP API 有什么区别？
3. 并行工具调用有哪些风险？
4. 工具粒度应该按 API 还是业务动作设计？

### Day 3｜MCP 协议与工具接入架构
**时间：90～120 分钟**

学习：
- MCP Host、Client、Server 三种角色。
- Tools、Resources、Prompts 的作用。
- stdio 和 Streamable HTTP 的使用场景。
- MCP 和传统插件体系的区别。
- MCP 的权限、安全和传输边界。

资料：
- MCP 官方文档：https://modelcontextprotocol.io/
- MCP Specification：https://modelcontextprotocol.io/specification/

代码：
- 创建 `mcp/server.py`。
- 暴露 `search_competitors`、`get_competitor_detail` 两个 Tool。
- 暴露一个竞品基础信息 Resource。
- 通过官方 SDK 启动 MCP Server。
- 画出 Host → Client → Server → Tool 的时序图。

产出：
- 一份可运行的 MCP Server。
- MCP 调用时序图。

验收：
- 能通过 MCP Client 发现工具。
- 能成功调用两个工具。
- 能解释工具发现、参数传递和结果返回的过程。

面试题：
1. MCP 解决了什么问题？
2. MCP 和 Function Calling 是什么关系？
3. MCP 和 A2A 有什么区别？
4. MCP 是否适合所有内部服务？为什么？

### Day 4｜MCP 工程化与安全
**时间：90～120 分钟**

学习：
- 工具鉴权、最小权限和凭证管理。
- 超时、错误码、大结果集处理。
- MCP Server 的部署和版本管理。
- 工具注册、健康检查和能力发现。

资料：
- MCP 官方文档：https://modelcontextprotocol.io/
- OWASP Top 10 for LLM Applications：https://owasp.org/www-project-top-10-for-large-language-model-applications/

代码：
- 给 MCP 工具加入 Token 鉴权。
- Token 从环境变量读取，不进入 Prompt。
- 加入超时、结果大小限制和错误映射。
- 为工具增加权限声明和调用审计。
- 编写 3 个非法调用测试。

产出：
- MCP Server V1。
- 工具权限矩阵。

验收：
- 未授权请求无法执行工具。
- 超时能返回可识别错误。
- 敏感凭证不会出现在日志和模型上下文中。

面试题：
1. MCP Server 如何做身份认证和授权？
2. 工具执行结果过大怎么办？
3. 如何防止 Agent 越权调用工具？
4. MCP 工具如何实现版本兼容？

### Day 5｜Agent 范式：ReAct、Plan-and-Execute、Reflexion
**时间：90～120 分钟**

学习：
- ReAct：思考、行动、观察。
- Plan-and-Execute：先规划，再执行。
- Reflexion：失败后反思和重试。
- Workflow 与 Agent 的区别。
- 多 Agent 的适用条件。

资料：
- Anthropic Building Effective Agents：https://www.anthropic.com/engineering/building-effective-agents
- 12-Factor Agents：https://github.com/humanlayer/12-factor-agents

代码：
- 为同一个竞品分析任务实现 ReAct 和 Plan-and-Execute 两种执行方式。
- 记录模型调用次数、工具调用次数、Token、成功率。
- 失败时增加一次受限反思重试。
- 对比三种模式的成本和效果。

产出：
- Agent 范式对比表。

验收：
- 能说清三种范式各自适用的任务。
- 能用真实实验数据解释为什么选其中一种。
- 不把多 Agent 当成默认架构。

面试题：
1. ReAct 和 Plan-and-Execute 有什么区别？
2. 什么情况下需要多 Agent？
3. 固定 Workflow 和 Agent 如何组合？
4. 为什么有时一个 Agent 加多个好工具，比多个 Agent 更好？

### Day 6｜上下文工程与 LLM 基础
**时间：90～120 分钟**

学习：
- System Prompt、历史消息、工具返回、用户输入的上下文结构。
- Token、Context Window、Embedding、Temperature。
- Transformer 和 Attention 的基本作用。
- Prefill、Decode、KV Cache 的基本概念。
- 上下文压缩、摘要和外部检索。

资料：
- Anthropic Context Engineering：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Hugging Face NLP Course：https://huggingface.co/learn/nlp-course/

代码：
- 编写 `agent/context/manager.py`。
- 实现 Prompt 分层模板。
- 统计输入 Token、输出 Token 和工具结果 Token。
- 实现历史消息滚动摘要。
- 对比原始工具结果与结构化摘要对任务效果的影响。

产出：
- 上下文管理模块。
- Token 预算表。

验收：
- 能解释上下文窗口为什么会影响 Agent 效果。
- 超长工具结果不会无限进入上下文。
- 压缩后仍能保留用户关键约束。

面试题：
1. Context Window 和 Token 是什么关系？
2. KV Cache 解决什么问题？
3. 为什么上下文越长不一定越好？
4. 如何避免上下文压缩导致关键约束丢失？

### Day 7｜第一周集成与模拟面试
**时间：4 小时**

任务：
- 集成 Agent Loop、工具注册中心、MCP Server。
- 补充 README、运行说明和架构图。
- 录制 3～5 分钟项目演示。
- 口头回答第一周面试题。

代码：
- 完成一次“分析竞品 → 查询工具 → 汇总结果”的端到端执行。
- 增加 5 个正常测试和 5 个异常测试。

产出：
- 项目 V0.1。
- 3～5 分钟演示视频。
- 第一周复盘文档。

验收：
- 能脱离框架解释一次完整 Agent 调用。
- 能现场运行 Demo。
- 能讲清工具调用、异常处理和终止条件。

模拟面试：
1. 请介绍你实现的 Agent Loop。
2. 为什么需要工具注册中心？
3. MCP 与 Function Calling 分别解决什么问题？
4. Agent 执行中模型连续调用同一个工具怎么办？
5. 为什么不直接把整个业务流程写成普通代码？

---

## 第 2 周：LangGraph、RAG、Memory 与生产化

目标：从能运行的 Agent，升级到有状态、可恢复、可评测、可控成本的 Agent 应用。

### Day 8｜LangGraph 核心机制
**时间：90～120 分钟**

学习：
- State、Node、Edge。
- 条件路由。
- Checkpoint。
- LangGraph 与手写 Agent Loop 的关系。
- 固定 Workflow 与动态 Agent 的组合。

资料：
- LangGraph 官方文档：https://docs.langchain.com/oss/python/langgraph/overview

代码：
- 创建 `agent/graph/workflow.py`。
- 把竞品分析流程拆为输入、检索、分析、结果生成四个 Node。
- 定义共享 State。
- 增加条件路由：信息不足时返回补充检索节点。

产出：
- 一个 LangGraph 工作流。

验收：
- 能画出 Graph。
- 能解释 State 如何在节点之间传递。
- 能解释 LangGraph 相比手写循环解决了什么问题。

面试题：
1. LangGraph 的 State、Node、Edge 分别是什么？
2. 为什么 Agent 需要状态管理？
3. LangGraph 和普通 Workflow 引擎有什么区别？
4. 什么情况下不需要 LangGraph？

### Day 9｜Checkpoint、恢复与 Human-in-the-loop
**时间：90～120 分钟**

学习：
- Checkpoint 和任务持久化。
- 中断与恢复。
- 人工审批节点。
- 长任务状态管理。
- 重复执行和恢复时的幂等问题。

资料：
- LangGraph Persistence：https://docs.langchain.com/oss/python/langgraph/persistence
- LangGraph Human-in-the-loop：https://docs.langchain.com/oss/python/langgraph/interrupts

代码：
- 为竞品报告流程增加 Checkpoint。
- 在发布报告前增加人工确认节点。
- 模拟程序中断后从上次状态恢复。
- 确保恢复执行不会重复写入相同报告。

产出：
- 可中断、可恢复的工作流。

验收：
- 能暂停任务并保存状态。
- 人工确认后能从暂停位置继续。
- 重启后不会无条件从头执行。

面试题：
1. Checkpoint 解决什么问题？
2. Human-in-the-loop 如何实现？
3. 长任务恢复时如何避免重复副作用？
4. 人工审批和模型置信度判断有什么区别？

### Day 10｜RAG 全链路
**时间：90～120 分钟**

学习：
- 文档解析和 Chunking。
- Embedding。
- 向量检索、关键词检索和 Hybrid Search。
- Rerank。
- Query Rewrite。
- RAG 适用边界。

资料：
- Hugging Face：https://huggingface.co/learn/nlp-course/
- OpenAI Embeddings：https://platform.openai.com/docs/guides/embeddings

代码：
- 创建 `agent/rag/`。
- 导入 10～20 份竞品说明文档或自建样本文档。
- 实现文档切分、Embedding 和向量检索。
- 增加关键词检索或 Hybrid Search。
- 对比 Top-3 检索结果。

产出：
- RAG V1。
- 10 条检索问题和结果记录。

验收：
- 能根据问题找到对应文档片段。
- 能解释 Chunking、Embedding、Rerank 的作用。
- 能说清哪些问题应该走 SQL/API，而不是 RAG。

面试题：
1. RAG 的完整链路是什么？
2. Chunking 如何选择？
3. 向量检索和关键词检索如何组合？
4. 什么场景不应该使用 RAG？

### Day 11｜RAG 进阶与质量评估
**时间：90～120 分钟**

学习：
- Advanced RAG。
- Query Rewrite。
- Rerank。
- Recall@K、MRR、NDCG 的概念。
- 检索质量与最终答案质量的区别。

资料：
- OpenAI Evals：https://platform.openai.com/docs/guides/evals

代码：
- 为 10～20 条问题准备标准答案和相关文档。
- 对比纯向量、Hybrid Search、Hybrid + Rerank。
- 计算 Top-3 命中率。
- 对错误召回做归因。

产出：
- RAG 评测报告。

验收：
- 能解释不同检索方案的效果差异。
- 能指出问题出在召回、排序还是生成。
- 不把最终回答正确率简单等同于检索准确率。

面试题：
1. RAG 召回率低怎么排查？
2. Rerank 有什么代价？
3. Recall@K 和 MRR 分别衡量什么？
4. 如何评估 RAG 的效果？

### Day 12｜Memory 记忆体系
**时间：90～120 分钟**

学习：
- 短期上下文窗口。
- 滚动摘要。
- 结构化用户档案。
- 长期向量记忆。
- 记忆写入、更新、读取、过期和删除策略。

资料：
- LangGraph Memory：https://docs.langchain.com/oss/python/langgraph/add-memory

代码：
- 创建 `agent/memory/manager.py`。
- 实现会话短期记忆。
- 实现竞品历史结论的结构化存储。
- 实现跨会话读取。
- 增加 TTL 和删除逻辑。

产出：
- Memory V1。
- 记忆读写决策图。

验收：
- 第二次会话能召回之前确认过的竞品信息。
- 临时状态不会被无条件写入长期记忆。
- 能删除指定记忆。

面试题：
1. Agent Memory 与普通 Chat History 有什么区别？
2. 哪些信息应该进入长期记忆？
3. 如何处理过期记忆？
4. 记忆系统如何满足用户删除要求？

### Day 13｜Evaluation：Agent 评测体系
**时间：90～120 分钟**

学习：
- 离线评测集。
- 正常、边界、恶意、应拒答四类样本。
- 结果层、过程层、系统层指标。
- LLM-as-judge。
- 人工抽检和评测校准。

资料：
- OpenAI Evals：https://platform.openai.com/docs/guides/evals

代码：
- 创建 `evals/dataset.jsonl`。
- 准备至少 30 条测试样本。
- 记录任务成功率、工具选择准确率、平均轮次、P95 延迟。
- 增加 LLM-as-judge 评分。
- 人工抽检至少 10 条。

产出：
- `evals/run_eval.py`。
- Agent 评测报告。

验收：
- 可以重复运行评测。
- 每次修改 Prompt 或模型后能对比效果。
- 能解释 Judge 的偏差及人工校准方法。

面试题：
1. 如何评估 Agent？
2. LLM-as-judge 有什么缺陷？
3. 如何建立一个有代表性的 Eval Set？
4. Agent 成功率高，为什么仍然可能不能上线？

### Day 14｜可靠性、故障注入与成本优化
**时间：4 小时**

学习：
- 超时、重试、指数退避、幂等、熔断。
- 工具重复调用检测。
- 主模型失败后的降级。
- 模型路由、Prompt Caching、并行调用。
- 首字延迟、P95 延迟、单任务成本。

资料：
- 12-Factor Agents：https://github.com/humanlayer/12-factor-agents
- OpenTelemetry：https://opentelemetry.io/docs/

代码：
- 为工具执行加入超时、重试、幂等键。
- 注入工具超时、500、模型调用失败等故障。
- 记录 Token、模型调用次数、工具耗时。
- 对比固定模型和简单模型路由的成本。
- 为执行链路生成结构化 Trace。

产出：
- 故障注入报告。
- 成本与延迟分析表。
- 项目 V0.5。

验收：
- 至少覆盖 5 种故障。
- 能恢复可重试故障。
- 写操作不会因重试重复产生业务副作用。
- 能解释成本主要来自哪里、延迟主要发生在哪里。

模拟面试：
1. Agent 工具调用如何做幂等？
2. 模型服务超时如何处理？
3. 模型路由如何设计？
4. 如何降低单任务成本？
5. 如何评估一次 Agent 优化是否真的有效？

---

## 第 3 周：企业级 Agent 平台系统设计

目标：把学习成果转化成中高级岗位的系统设计能力。每道题都要讲架构、关键决策、失败模式、评测、成本和容量。

### Day 15｜系统设计答题模板
**时间：90 分钟**

任务：
- 固化六步法：
  1. 澄清需求。
  2. 整体架构。
  3. 关键决策与 Trade-off。
  4. 失败模式。
  5. 评测与上线。
  6. 成本与容量。
- 准备用户规模、QPS、延迟 SLA、数据敏感度、多租户等澄清项。
- 为每个方案准备至少 2 个备选方案。

产出：
- 一张 A4 系统设计速查卡。

面试题：
1. 为什么系统设计不能上来就画架构？
2. 什么是 Trade-off？
3. 设计中如何体现容量和成本意识？

### Day 16｜系统设计题 1：企业级 Agent 平台
**时间：90～120 分钟**

题目：
设计一个支持 100 个 SaaS 工具、多个业务团队和多个模型的 Agent 平台。

重点：
- 接入层、编排层、工具层、模型层、观测层。
- 工具注册中心。
- MCP 与内部 API 的边界。
- 模型网关、配额和限流。
- 多租户、权限和审计。
- 版本发布与兼容。

产出：
- 一张完整架构图。
- 核心模块职责表。
- 6 种失败模式及应对方案。

面试题：
1. 从 0 到 1 如何建设企业级 Agent 平台？
2. 为什么要建设统一模型网关？
3. 工具注册中心应该管理哪些元数据？
4. 如何保证不同业务团队之间互不影响？

### Day 17｜系统设计题 2：企业客服 Agent
**时间：90 分钟**

题目：
设计支持多轮对话、知识检索、工单处理和人工接管的客服 Agent。

重点：
- 意图识别。
- RAG 检索。
- 工单工具调用。
- 人工接管条件。
- 会话状态和上下文交接。
- 知识库更新和版本管理。

产出：
- 一张状态机图。
- 一份转人工判定规则。

面试题：
1. 什么时候应该转人工？
2. 如何把上下文交给人工坐席？
3. 如何避免 Agent 在错误答案上不断重试？
4. 知识库更新如何避免旧知识污染新答案？

### Day 18｜系统设计题 3：代码 Agent
**时间：90 分钟**

题目：
设计一个能够读取代码、修改文件、运行测试并提交 PR 的代码 Agent。

重点：
- 沙箱隔离。
- 仓库权限分级。
- 命令执行策略。
- 文件系统和网络出口控制。
- 测试与 CI。
- Diff 审计和回滚。

产出：
- 权限分级矩阵。
- 代码 Agent 执行流程图。

面试题：
1. 代码 Agent 如何防止执行危险命令？
2. 如何限制 Agent 的文件和网络访问？
3. 修改错误代码后如何发现和回滚？
4. 如何让每次执行都可审计？

### Day 19｜系统设计题 4：多 Agent 协作
**时间：90 分钟**

题目：
设计一个包含研究、分析、审核三个角色的 Agent 协作系统。

重点：
- Supervisor、层级式、对等协作拓扑。
- 子任务拆分。
- 任务状态和消息传递。
- 上下文与权限隔离。
- 失败传播和任务恢复。
- A2A 的适用边界。

产出：
- 多 Agent 架构图。
- 是否拆分多 Agent 的决策树。

面试题：
1. 多 Agent 的必要条件是什么？
2. Supervisor 模式有什么问题？
3. Agent 之间如何共享状态？
4. 多 Agent 失败时如何定位责任节点？

### Day 20｜系统设计题 5：Agent Gateway / 开放平台
**时间：90～120 分钟**

题目：
设计一个为多个业务方提供统一 Agent 能力的 Gateway。

重点：
- 统一模型 API。
- 模型路由。
- Token 统计和计费。
- 租户限流与配额。
- Prompt、模型和工具版本管理。
- Trace 和审计。
- 灰度、回滚和 SLA。

产出：
- Trace 字段表。
- 限流与计费方案。
- 模型网关架构图。

面试题：
1. 模型网关需要解决哪些问题？
2. 如何统计单次任务的真实成本？
3. 多租户限流如何设计？
4. 如何实现 Prompt 和模型版本灰度？

### Day 21｜系统设计串讲与复盘
**时间：4 小时**

任务：
- 五道系统设计题，每道讲 8～10 分钟。
- 随机抽一道题，限时 40 分钟完成白板设计。
- 回听录音，记录逻辑断层、没有数据、没有 Trade-off 的地方。
- 补齐失败模式、成本和容量估算。

产出：
- 五份系统设计文档。
- 五段讲解录音。
- 一份薄弱点清单。

验收：
- 任一题都能先澄清需求，再画架构。
- 至少能讲出 3 个关键 Trade-off。
- 至少能列出 6 种失败模式及处置。
- 面对三层追问仍能给出有依据的答案。

---

## 第 4 周：项目深挖、Coding、英文与模拟面试

目标：把技术能力转化为面试表现，能够证明自己不仅会用 AI Coding，也能理解、设计和负责 Agent 系统。

### Day 22｜主项目完整集成
**时间：90～120 分钟**

任务：
- 集成模型网关、Agent Runtime、工具中心、LangGraph、RAG、Memory。
- 完成竞品监控端到端流程。
- 补充配置文件、异常处理和启动脚本。

代码：
- 完成 `app.py` 或 FastAPI 入口。
- 增加一个 API：提交竞品分析任务。
- 增加一个 API：查询任务状态和结果。

产出：
- Agent Platform Lite V0.8。
- 完整架构图。

验收：
- 一条请求可以从入口走到最终报告。
- 任务状态可查询。
- 关键步骤可追踪。

面试题：
1. 请介绍你的 Agent 平台架构。
2. 为什么这样划分模块？
3. 哪些环节是固定 Workflow，哪些环节由 Agent 决策？

### Day 23｜项目指标、故障和安全复盘
**时间：90 分钟**

任务：
- 汇总 30 条 Eval 测试结果。
- 统计成功率、工具调用准确率、P95 延迟、单任务成本。
- 记录 3 个真实失败案例。
- 检查 Prompt Injection、越权工具、跨租户数据访问。
- 编写项目安全检查清单。

产出：
- 项目质量报告。
- 安全检查清单。
- 三个故障故事。

验收：
- 不编造指标，未测量的数据明确标注为未测。
- 每个失败案例有现象、根因、处理和改进。
- 能解释 Agent 的安全边界。

面试题：
1. 你如何证明 Agent 的效果？
2. Prompt Injection 能彻底防止吗？
3. 多租户 RAG 如何避免数据串租户？
4. 你项目中最严重的失败是什么？

### Day 24｜项目故事：2 分钟、10 分钟、30 分钟
**时间：90 分钟**

任务：
- 准备 2 分钟项目介绍。
- 准备 10 分钟项目深挖。
- 准备 30 分钟白板讲解。
- 每个版本都包含业务背景、为什么用 Agent、架构取舍、指标、失败案例和复盘。

产出：
- 三份项目讲解提纲。

面试题：
1. 为什么这个场景需要 Agent？
2. 为什么不直接用规则引擎或普通 Workflow？
3. 项目里你亲自完成了哪些关键设计？
4. 如果重新做一次，你会改什么？

### Day 25｜Java / 分布式 / Coding 复习
**时间：90～120 分钟**

复习：
- JVM 内存与 GC。
- 线程池、锁、CAS、AQS。
- HashMap、并发容器。
- Netty 基本模型。
- 分布式事务、幂等。
- 限流、熔断、缓存一致性。
- HTTP、SSE、WebSocket。
- Redis、MySQL、消息队列。

Coding：
- 数组与哈希。
- 链表。
- 二叉树 DFS/BFS。
- 二分查找。
- TopK。
- 滑动窗口。

产出：
- 10 道 Java 高频题答案。
- 5 道算法题代码。
- 每道题一份复杂度分析。

验收：
- 能在 20～30 分钟内完成一道中等难度基础算法题。
- 能结合真实项目解释 Java 并发与分布式问题。

面试题：
1. 线程池参数如何设置？
2. 如何实现分布式幂等？
3. Redis 缓存与数据库如何保证一致性？
4. SSE 和 WebSocket 有什么区别？
5. Agent 工具执行为什么也需要并发控制？

### Day 26｜模拟面试 1：技术原理与项目深挖
**时间：4 小时**

模拟流程：
- 15 分钟：自我介绍。
- 45 分钟：Agent 原理和框架。
- 60 分钟：项目深挖。
- 30 分钟：RAG、Memory、Evaluation。
- 30 分钟：安全、可靠性和成本。
- 剩余时间：复盘与补漏。

重点追问：
- 你写的 Agent Loop 中，状态在哪里？
- 为什么选 LangGraph？
- Checkpoint 如何恢复？
- 工具调用重复执行怎么办？
- 你如何测量项目质量？
- 如果流量增长 10 倍，最先出现什么瓶颈？

产出：
- 一份模拟面试评分表。
- 三个需要补强的问题。

验收：
- 不依赖背稿，能解释代码实现。
- 被连续追问三层时不跑题。
- 对项目数据不夸大、不编造。

### Day 27｜模拟面试 2：系统设计白板
**时间：4 小时**

任务：
- 随机抽一道系统设计题。
- 40 分钟完成设计。
- 20 分钟接受追问。
- 再抽一道题做 30 分钟快速设计。
- 复盘架构、Trade-off、容量和失败模式。

重点追问：
- 为什么选择这个架构？
- 如果模型供应商不可用怎么办？
- 如何支持多个租户？
- 如何控制成本？
- 如何灰度和回滚？
- 如何判断 Agent 效果退化？

产出：
- 两份白板设计稿。
- 系统设计复盘报告。

### Day 28｜英文面试与行为面试
**时间：90 分钟**

任务：
- 英文自我介绍 2 分钟。
- 英文讲项目 3 分钟。
- 准备五类行为题：
  - Conflict：团队冲突。
  - Failure：失败经历。
  - Ambiguity：模糊需求。
  - Prioritization：优先级决策。
  - Influence：跨团队影响力。
- 准备反问面试官的问题。

产出：
- 两段英文录音。
- 五个行为题回答提纲。

验收：
- 能自然表达项目和技术取舍。
- 不追求复杂语法，重点是准确、清晰、有逻辑。

### Day 29｜简历、岗位匹配与定级证据
**时间：90～120 分钟**

任务：
- 更新中文简历和英文简历。
- 将 Agent 平台项目放在显眼位置。
- 使用真实数据表达成功率、成本、延迟、覆盖场景。
- 梳理过往分布式系统、团队管理、跨团队影响力。
- 准备中高级岗位定级证据。

产出：
- 中英文简历。
- 项目介绍材料。
- 定级证据清单。

验收：
- 每条关键经历都有背景、个人贡献和结果。
- 项目指标可解释、可验证。
- 不将 AI Coding 工具生成的代码量当作个人技术贡献。

### Day 30｜最终模拟面试与投递准备
**时间：4 小时**

任务：
- 进行一次完整模拟面试。
- 复习 20 道 Agent 高频题。
- 复习五道系统设计题。
- 检查 GitHub 项目、README、演示视频。
- 按真实 JD 更新简历关键词。
- 建立投递跟踪表，准备内推沟通。

产出：
- 最终项目 V1。
- 中英文简历。
- 面试题清单。
- 投递跟踪表。

验收：
- 能进行 2 分钟自我介绍。
- 能讲解项目 10～30 分钟。
- 能完成一轮系统设计。
- 能解释核心代码、指标和架构取舍。
- 能针对真实岗位 JD 说明匹配点和差距。

---

> 由源稿 Markdown 自动生成 · 改源稿后执行 `python3 scripts/gen_readme.py` 刷新。
