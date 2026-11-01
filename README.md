# learn-agent

> **35 岁阿里后端，用 30 天把自己重训成 Agent 工程师 —— 配套学习代码库。**
> **终极目标**：具备大型分布式系统经验、能负责企业级 AI Agent 平台与应用工程化落地的技术负责人。

本仓库是公众号系列 **「30 天把自己重训成 Agent 工程师」**（公众号：**溪月散人**）的
**代码落地**。计划本身见 [`AI-Agent-30天学习执行手册.html`](AI-Agent-30天学习执行手册.html)；
这里把计划每节变成可运行、可 review、可提交的真实产物。

## 这个仓库怎么用

- **每节一个目录** `dayNN-*/`（如 `day04-agent-loop/`），里面包含该节全部学习产物。
- **每目录三件套**：① 可运行代码（零依赖，`python3 xxx.py` 直接跑）；
  ② 时序图 / 架构图（GitHub 用 Mermaid，公众号用交互式 HTML）；
  ③ `README.md`（目标 / 资料 / 验收 / 自测题）。
- **进度驱动**：下面的进度表会自动识别哪些 `dayNN-*/` 已建，已建的标 ✅ 并链接。
- **改计划后重跑**：编辑源稿 Markdown，执行 `python3 scripts/gen_readme.py` 即可刷新本文件。
- **发布节奏**：弹性更新。作者在职，只能空闲时写，争取每周 1–2 节、有空 3 节，断更正常，不排死线。

## 关联资源

- 30 节学习计划（自包含 HTML，可浏览器看 / 打印）：[`AI-Agent-30天学习执行手册.html`](AI-Agent-30天学习执行手册.html)
- 同名公众号连载：搜索 **溪月散人**（《30 天把自己重训成 Agent 工程师》）

---

## 学习进度（30 节）

| 节 | 主题 | 代码目录 | 状态 |
|----|------|---------|------|
| 第 1 节 | Workflow 与 Agent 的本质区别 | day01-*/（待建） | ⬜ 待产 |
| 第 2 节 | 什么时候该用 Workflow | day02-*/（待建） | ⬜ 待产 |
| 第 3 节 | 什么时候需要升级到 Agent | day03-*/（待建） | ⬜ 待产 |
| [第 4 节](day04-agent-loop/) | Agent Loop 从零写 | [day04-agent-loop/](day04-agent-loop/) | ✅ 已完成 |
| [第 5 节](day05-function-calling/) | Function Calling 与工具设计 | [day05-function-calling/](day05-function-calling/) | ✅ 已完成 |
| 第 6 节 | MCP 协议与工具接入架构 | day06-*/（待建） | ⬜ 待产 |
| 第 7 节 | MCP 工程化与安全 | day07-*/（待建） | ⬜ 待产 |
| 第 8 节 | Agent 范式：ReAct、Plan-and-Execute、Reflexion | day08-*/（待建） | ⬜ 待产 |
| 第 9 节 | 上下文工程与 LLM 基础 | day09-*/（待建） | ⬜ 待产 |
| 第 10 节 | LangGraph 核心机制 | day10-*/（待建） | ⬜ 待产 |
| 第 11 节 | Checkpoint、恢复与 Human-in-the-loop | day11-*/（待建） | ⬜ 待产 |
| 第 12 节 | RAG 全链路 | day12-*/（待建） | ⬜ 待产 |
| 第 13 节 | RAG 进阶与质量评估 | day13-*/（待建） | ⬜ 待产 |
| 第 14 节 | Memory 记忆体系 | day14-*/（待建） | ⬜ 待产 |
| 第 15 节 | Agent 评测体系 | day15-*/（待建） | ⬜ 待产 |
| 第 16 节 | 可靠性、故障注入与成本优化 | day16-*/（待建） | ⬜ 待产 |
| 第 17 节 | 实战：把 bot 改造成 Agent | day17-*/（待建） | ⬜ 待产 |
| 第 18 节 | Workflow 与 Agent 在一个系统里共存 | day18-*/（待建） | ⬜ 待产 |
| 第 19 节 | 系统设计答题模板（六步法） | day19-*/（待建） | ⬜ 待产 |
| 第 20 节 | 系统设计题 1：企业级 Agent 平台 | day20-*/（待建） | ⬜ 待产 |
| 第 21 节 | 系统设计题 2：企业客服 Agent | day21-*/（待建） | ⬜ 待产 |
| 第 22 节 | 系统设计题 3：代码 Agent | day22-*/（待建） | ⬜ 待产 |
| 第 23 节 | 系统设计题 4：多 Agent 协作 | day23-*/（待建） | ⬜ 待产 |
| 第 24 节 | 系统设计题 5：Agent Gateway / 开放平台 | day24-*/（待建） | ⬜ 待产 |
| 第 25 节 | 主项目完整集成 | day25-*/（待建） | ⬜ 待产 |
| 第 26 节 | 项目指标、故障和安全复盘 | day26-*/（待建） | ⬜ 待产 |
| 第 27 节 | 项目复盘与架构讲解（2 / 10 / 30 分钟三档） | day27-*/（待建） | ⬜ 待产 |
| 第 28 节 | Java / 分布式 / Coding 复习 | day28-*/（待建） | ⬜ 待产 |
| 第 29 节 | 技术领导力与工程决策 | day29-*/（待建） | ⬜ 待产 |
| 第 30 节 | 综合复盘与 90 天进阶路线 | day30-*/（待建） | ⬜ 待产 |

---

## 30 节学习计划（总纲）

## 目标

具备大型分布式系统经验、能够负责企业级 AI Agent 平台和应用工程化落地的技术负责人。

30 节结束时，应能够：

- 不依赖框架，独立写出 Agent 核心循环（Loop / 工具编排 / 上下文工程）；
- 设计有状态、可恢复、可评测、可控成本的生产级 Agent 应用（LangGraph / RAG / Memory / Evaluation）；
- 主导企业级 Agent 平台与典型业务场景（客服 / 代码 / 多 Agent / Gateway）的系统设计，讲清架构、Trade-off、失败模式、成本与容量；
- 补齐分布式与工程化短板，并具备技术负责人的架构评审、决策记录（ADR）与跨团队对齐能力；
- 最重要的是：能判断一个需求到底该用 Workflow 还是 Agent，并在该升级时知道改哪里。

---

## 模块 A · 认知框架：Workflow 与 Agent 的本质

> 技术负责人最该有的不是「会不会写 Agent」，而是「知不知道什么时候不该上 Agent」。本模块用我真实跑着的 `ai-requirement-bot`（一个典型 Workflow）当标本，把这条判断线立起来。

### 第 1 节 ｜ Workflow 与 Agent 的本质区别
**时间：60～90 分钟**

学习：
- 判定标准只有一条：流程的下一步由谁决定？代码（if/else、状态机）决定 = Workflow；模型自主决定下一步（含工具自决、循环） = Agent。
- Workflow 的特征：步骤固定、可复现、每一步的输入输出确定、易单测。
- Agent 的特征：模型在循环里自己选工具、自己看结果、自己决定继续还是停。
- 常见误解：用了 LLM 不等于 Agent；LLM 只是流程里一个确定性节点时，它还是 Workflow。

案例：
- 读 `process_message`：意图分支是 `if/elif` 写死的，不是模型选的。
- 读 `spec_checker.build`：verdict 由纯函数算，模型只给 gates 结果——分支可测、可复现。
- 结论：这个 bot 用了 LLM，但它是 Workflow，不是 Agent。

资料：
- Anthropic · Building Effective Agents：https://www.anthropic.com/engineering/building-effective-agents
- 12-Factor Agents：https://github.com/humanlayer/12-factor-agents

产出：
- 一张「Workflow vs Agent」对照卡（左侧代码决定、右侧模型决定）。
- 一份 5 问判定清单：① 步骤固定吗 ② 需模型自决下一步吗 ③ 需多工具自治吗 ④ 需依中间结果决策吗 ⑤ 失败了能写死重试吗。

验收：
- 拿到任意一段 AI 代码，能一句话说清它是 Workflow 还是 Agent，并指出判定依据。
- 能解释「用 LLM 的 Workflow」为什么仍可测、可复现。

自测题：
1. 判定 Workflow 与 Agent 的那一条标准是什么？
2. 一个调用了 GPT 做文本分类的服务，是 Workflow 还是 Agent？为什么？
3. 为什么「用了 LLM」不等于「是 Agent」？
4. 你手头有没有一个「以为是 Agent 其实是 Workflow」的项目？

### 第 2 节 ｜ 什么时候该用 Workflow
**时间：60～90 分钟**

学习：
- Workflow 不是 Agent 的「低配版」，而是很多场景的更优解：更便宜、更可控、更好 debug、可单测覆盖。
- 适合 Workflow 的信号：步骤明确、规则清晰、要可复现、要低成本、出错要可定位。
- Agent 的代价：更贵（多轮调用）、更难测（非确定性）、更难 debug（链路长）、需要 eval 才敢上线。
- 工程现实：绝大多数「AI 功能」用 Workflow 就够了，硬上 Agent 是负担。

案例：
- 需求结构化（`structure_requirement`）、RAG 问答（`rag_engine`）：纯 Workflow 就稳，上 Agent 反而引入非确定性和成本。
- 它的「确认卡片才提交编码」是代码触发的硬门，不需要模型判断。

资料：
- Anthropic · Effective Agents（何时用 / 何时不用）：https://www.anthropic.com/engineering/building-effective-agents

产出：
- 一页「选型决策树」：从需求特征出发，输出 Workflow / Agent / 混合。

验收：
- 能给一个具体需求，画出决策树路径并说明为什么选 Workflow。
- 能讲出 Agent 相对 Workflow 至少 3 个真实代价。

自测题：
1. 什么场景下 Workflow 比 Agent 更优？
2. 为什么 Agent 需要评测体系才敢上线，而 Workflow 可以靠单测？
3. 如果把一个稳定 Workflow 硬改成 Agent，通常会引入哪些问题？
4. 「Agent 化」在你们团队是不是被当成了政治正确？举一个反例。

### 第 3 节 ｜ 什么时候需要升级到 Agent
**时间：60～90 分钟**

学习：
- 该升级的 4 类信号：① 非确定性链路（步骤无法写死）② 需动态拆解任务 ③ 需依中间结果决策 ④ 需自主调度多个工具完成一个目标。
- 升级不是「全改」，而是「把最该自治的那一段交给循环」，其余保持 Workflow。
- 反例：硬上 Agent 翻车的典型——把能写死的状态机换成模型自决，结果不可测、成本爆炸、debug 无门。
- 升级原则：先 Workflow 跑通，再识别瓶颈段，最后只把瓶颈段 Agent 化。

案例：
- 现状：编码甩给外部 Agent（`execute_task` fire-and-forget + `poll_agent_tasks` 轮询），bot 自身不参与端到端自治。
- 升级信号：若要 bot 自己完成「读代码 → 改 → 测 → 建 PR → 看结果再改」这类无法写死步骤的链路，就超出 Workflow 能力，必须引入 Agent Loop。

资料：
- 12-Factor Agents（何时引入循环）：https://github.com/humanlayer/12-factor-agents

产出：
- 一份「升级信号清单」（4 类信号 + 每条的判定问题）。
- 一张反例卡：「硬上 Agent 翻车」的 3 个真实症状。

验收：
- 能从一个真实需求里，圈出「该 Agent 化的瓶颈段」和「应保留的 Workflow 段」。
- 能解释为什么升级应是局部而非整体。

自测题：
1. 哪 4 类信号出现时该考虑升级到 Agent？
2. 为什么升级应该是「局部 Agent 化」而不是「整体重写」？
3. 举一个你见过的「硬上 Agent 翻车」案例，问题出在哪？
4. 如果让你给团队定一条「上 Agent 的准入标准」，你会写哪三条？

---

## 模块 B · Agent 核心能力（第 4–9 节）

> 这一部分就是「怎么写 Agent」。每一节都补一句「这一步 Workflow 做不到，必须 Agent」——把模块 A 的判断落到手上。

### 第 4 节 ｜ Agent Loop 从零写
**时间：90～120 分钟**

学习：
- 理解 LLM、Tool、Agent、Environment 的关系。
- 理解一次 Agent 执行的完整生命周期。
- 模型返回 tool_calls 后，应用层如何执行工具并回传结果。
- Agent 终止条件：无工具调用、达到最大轮次、上下文预算熔断。

案例：
- 对比：bot 没有这个循环，所以「多步自治」它做不到——这正是它该保持 Workflow 的原因，也是第 17 节要补的东西。

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
- 一张 Agent 执行时序图（九步）。

验收：
- 能完成至少一次工具调用和两轮连续工具调用。
- 模型返回错误参数时，不发生程序崩溃。
- 达到最大轮次时能返回明确的终止状态。

自测题：
1. Agent 和普通 LLM Chat 有什么区别？
2. Agent Loop 的核心流程是什么？
3. 如何防止 Agent 无限循环？
4. 工具执行失败后，应该由模型重试还是应用层重试？

### 第 5 节 ｜ Function Calling 与工具设计
**时间：90～120 分钟**

学习：
- tool_choice 的 auto、required、指定工具模式。
- JSON Schema 与参数校验。
- 并行工具调用与串行依赖。
- 结构化输出和工具调用的区别。
- 工具粒度如何设计。

案例：
- 对比：bot 的工具是代码分支写死的（发卡片 / 查 RAG），不是模型按结果自选——这正是 Workflow 与 Agent 在「工具调用」上的分水岭。

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

自测题：
1. 如何设计一个模型不容易误用的工具？
2. Function Calling 和普通 HTTP API 有什么区别？
3. 并行工具调用有哪些风险？
4. 工具粒度应该按 API 还是业务动作设计？

### 第 6 节 ｜ MCP 协议与工具接入架构
**时间：90～120 分钟**

学习：
- MCP Host、Client、Server 三种角色。
- Tools、Resources、Prompts 的作用。
- stdio 和 Streamable HTTP 的使用场景。
- MCP 和传统插件体系的区别。
- MCP 的权限、安全和传输边界。

案例：
- 延伸：bot 的编码 Agent 适配器（Trace / Qoder）就是「外部工具接入」的雏形——MCP 把它标准化了。

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

自测题：
1. MCP 解决了什么问题？
2. MCP 和 Function Calling 是什么关系？
3. MCP 和 A2A 有什么区别？
4. MCP 是否适合所有内部服务？为什么？

### 第 7 节 ｜ MCP 工程化与安全
**时间：90～120 分钟**

学习：
- 工具鉴权、最小权限和凭证管理。
- 超时、错误码、大结果集处理。
- MCP Server 的部署和版本管理。
- 工具注册、健康检查和能力发现。

案例：
- 延伸：bot 的飞书验签 + 人工确认门，正是「工具调用要受控」的真实样本——MCP 把这套机制做成了协议层。

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

自测题：
1. MCP Server 如何做身份认证和授权？
2. 工具执行结果过大怎么办？
3. 如何防止 Agent 越权调用工具？
4. MCP 工具如何实现版本兼容？

### 第 8 节 ｜ Agent 范式：ReAct、Plan-and-Execute、Reflexion
**时间：90～120 分钟**

学习：
- ReAct：思考、行动、观察。
- Plan-and-Execute：先规划，再执行。
- Reflexion：失败后反思和重试。
- Workflow 与 Agent 的区别（呼应第 1 节）。
- 多 Agent 的适用条件。

案例：
- 对比：bot 的 3 轮硬限追问 = 手写 Plan 的退化版，缺 Reflexion 的「失败后反思」——所以它卡在第 3 轮就停，不会自己换思路。

资料：
- Anthropic Building Effective Agents：https://www.anthropic.com/engineering/building-effective-agents
- 12-Factor Agents：https://github.com/humanlayer/12-factor-agents

代码：
- 为同一个竞品分析任务实现 ReAct 和 Plan-and-Execute 两种执行方式。
- 记录模型调用次数、工具调用次数、Token、成功率。
- 失败时增加一次受限反思重试。
- 对比三种模式的成本和效果。

产出：
- Agent 范式对比表（实测数据）。

验收：
- 能说清三种范式各自适用的任务。
- 能用真实实验数据解释为什么选其中一种。
- 不把多 Agent 当成默认架构。

自测题：
1. ReAct 和 Plan-and-Execute 有什么区别？
2. 什么情况下需要多 Agent？
3. 固定 Workflow 和 Agent 如何组合？
4. 为什么有时一个 Agent 加多个好工具，比多个 Agent 更好？

### 第 9 节 ｜ 上下文工程与 LLM 基础
**时间：90～120 分钟**

学习：
- System Prompt、历史消息、工具返回、用户输入的上下文结构。
- Token、Context Window、Embedding、Temperature。
- Transformer 和 Attention 的基本作用。
- Prefill、Decode、KV Cache 的基本概念。
- 上下文压缩、摘要和外部检索。

案例：
- 看 bot 的 `_history_for`：它已经在手工管理上下文窗口（裁系统追加、限 6 轮）——这正是上下文工程的雏形，只是写死在代码里。

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
- 第一周集成产物：项目 V0.1 + 3～5 分钟演示（把 Loop / 注册中心 / MCP 跑通端到端）。

验收：
- 能解释上下文窗口为什么会影响 Agent 效果。
- 超长工具结果不会无限进入上下文。
- 压缩后仍能保留用户关键约束。
- 能脱离框架解释一次完整 Agent 调用、讲清工具调用与终止条件。

自测题：
1. Context Window 和 Token 是什么关系？
2. KV Cache 解决什么问题？
3. 为什么上下文越长不一定越好？
4. 如何避免上下文压缩导致关键约束丢失？

---

## 模块 C · 生产化（第 10–16 节）

> 从能运行的 Agent，升级到有状态、可恢复、可评测、可控成本的 Agent 应用。

### 第 10 节 ｜ LangGraph 核心机制
**时间：90～120 分钟**

学习：
- State、Node、Edge。
- 条件路由。
- Checkpoint。
- LangGraph 与手写 Agent Loop 的关系。
- 固定 Workflow 与动态 Agent 的组合。

案例：
- 点破：很多人以为「上了 LangGraph 就是 Agent」，其实它只是把 Workflow 用框架表达——Loop 才是 Agent 的灵魂。

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

自测题：
1. LangGraph 的 State、Node、Edge 分别是什么？
2. 为什么 Agent 需要状态管理？
3. LangGraph 和普通 Workflow 引擎有什么区别？
4. 什么情况下不需要 LangGraph？

### 第 11 节 ｜ Checkpoint、恢复与 Human-in-the-loop
**时间：90～120 分钟**

学习：
- Checkpoint 和任务持久化。
- 中断与恢复。
- 人工审批节点。
- 长任务状态管理。
- 重复执行和恢复时的幂等问题。

案例：
- bot 的「确认卡片才提交编码」就是 HITL，但它是代码触发不是 Agent 判断——本节把它升级成 Agent 可暂停、可恢复。

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

自测题：
1. Checkpoint 解决什么问题？
2. Human-in-the-loop 如何实现？
3. 长任务恢复时如何避免重复副作用？
4. 人工审批和模型置信度判断有什么区别？

### 第 12 节 ｜ RAG 全链路
**时间：90～120 分钟**

学习：
- 文档解析和 Chunking。
- Embedding。
- 向量检索、关键词检索和 Hybrid Search。
- Rerank。
- Query Rewrite。
- RAG 适用边界。

案例：
- bot 的 `rag_engine` + `okf_parser` + `git_sync` 是现成的 RAG 全链路样本——直接当教材拆。

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

自测题：
1. RAG 的完整链路是什么？
2. Chunking 如何选择？
3. 向量检索和关键词检索如何组合？
4. 什么场景不应该使用 RAG？

### 第 13 节 ｜ RAG 进阶与质量评估
**时间：90～120 分钟**

学习：
- Advanced RAG。
- Query Rewrite。
- Rerank。
- Recall@K、MRR、NDCG 的概念。
- 检索质量与最终答案质量的区别。

案例：
- 用 bot 的增量索引（`sync_files` by hash）讲工程化取舍：全量重跑 vs 增量同步。

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

自测题：
1. RAG 召回率低怎么排查？
2. Rerank 有什么代价？
3. Recall@K 和 MRR 分别衡量什么？
4. 如何评估 RAG 的效果？

### 第 14 节 ｜ Memory 记忆体系
**时间：90～120 分钟**

学习：
- 短期上下文窗口。
- 滚动摘要。
- 结构化用户档案。
- 长期向量记忆。
- 记忆写入、更新、读取、过期和删除策略。

案例：
- bot 的 `session_store` 是「短期上下文」的最小实现，缺长期档案——本节补齐。

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

自测题：
1. Agent Memory 与普通 Chat History 有什么区别？
2. 哪些信息应该进入长期记忆？
3. 如何处理过期记忆？
4. 记忆系统如何满足用户删除要求？

### 第 15 节 ｜ Agent 评测体系
**时间：90～120 分钟**

学习：
- 离线评测集。
- 正常、边界、恶意、应拒答四类样本。
- 结果层、过程层、系统层指标。
- LLM-as-judge。
- 人工抽检和评测校准。

案例：
- 呼应第 1 节：bot 作为 Workflow 靠单测可测；Agent 必须建 eval 才敢上线——这是两者工程成本和可靠性的分水岭。

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

自测题：
1. 如何评估 Agent？
2. LLM-as-judge 有什么缺陷？
3. 如何建立一个有代表性的 Eval Set？
4. Agent 成功率高，为什么仍然可能不能上线？

### 第 16 节 ｜ 可靠性、故障注入与成本优化
**时间：4 小时**

学习：
- 超时、重试、指数退避、幂等、熔断。
- 工具重复调用检测。
- 主模型失败后的降级。
- 模型路由、Prompt Caching、并行调用。
- 首字延迟、P95 延迟、单任务成本。

案例：
- bot 的「立即 ACK + 异步队列 + 主动推送」就是可靠性范本（防飞书超时重试）——Agent 链路更长，这套更关键。

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

实战复盘：
1. Agent 工具调用如何做幂等？
2. 模型服务超时如何处理？
3. 模型路由如何设计？
4. 如何降低单任务成本？
5. 如何评估一次 Agent 优化是否真的有效？

---

## 模块 D · 改造实战（第 17–18 节，用户特需）

> 拿真实跑着的 `ai-requirement-bot` 当标本，演示「从 Workflow 升级成 Agent 到底改哪」，以及「两者如何在一个系统里共存」。

### 第 17 节 ｜ 实战：把 bot 改造成 Agent
**时间：120～180 分钟**

学习：
- 改造点逐条：状态机 → 循环；固定分支 → 工具自决；3 轮硬限 → 反思重试；甩外部 → 端到端。
- 保留 Workflow 的部分：意图分发、人工确认门——这些不该 Agent 化。
- 改造的边界：只在「非确定性瓶颈段」插 Agent Loop，其余不动。

案例：
- 以 `_handle_requirement` / `_submit_agent` 为改造起点，演示在哪插 Agent Loop（`agent/runtime/loop.py`）。
- 对照：改造前（状态机 + 外部甩单）vs 改造后（bot 自身端到端自治读→改→测→PR→再改）。

资料：
- 12-Factor Agents：https://github.com/humanlayer/12-factor-agents
- Anthropic Building Effective Agents：https://www.anthropic.com/engineering/building-effective-agents

代码：
- 在 `learn-agent/day17-bot-to-agent/` 新建改造分支。
- 复用 `ai-requirement-bot` 作对照。
- 把「需求→编码→验证→再改」链路接入 Agent Loop。
- 保留意图分发与人工确认门为 Workflow 节点。

产出：
- 改造前后对照文档。
- 新增 `agent/runtime/loop.py` 接入点示意。

验收：
- 能讲清每一处「为什么这里要改、那里保留」。
- 改造后链路可端到端跑通一个非确定性子任务。
- 不把原本稳定的 Workflow 段弄坏。

自测题：
1. 把 bot 改造成 Agent，哪几段该改、哪几段该保留？
2. 为什么「3 轮硬限追问」不等于「反思重试」？
3. 改造后如何保证原本可测的 Workflow 段不被破坏？
4. 你怎么验证「升级后真的更好」而不是更贵更难测？

### 第 18 节 ｜ Workflow 与 Agent 在一个系统里共存
**时间：90～120 分钟**

学习：
- 分层：网关 / 路由层用 Workflow（快、可控、便宜）；复杂子任务交 Agent（慢、贵、但能自治）。
- 不是二选一，是分层——这是企业级系统的常态。
- 边界怎么划：哪些请求走 Workflow、哪些升级给 Agent、怎样平滑切换。

案例：
- bot 现状就是分层范本：意图分发 = Workflow，编码 = 外部 Agent。本节把它抽象成可复用的边界决策。

资料：
- Anthropic Building Effective Agents：https://www.anthropic.com/engineering/building-effective-agents

产出：
- 一张「分层架构图」（Workflow 层 + Agent 层 + 边界）。
- 一份边界决策清单（何时升级给 Agent）。

验收：
- 能画出一个真实系统的 Workflow / Agent 分层。
- 能写出「哪些请求走哪层」的判定规则。
- 不把「全部 Agent 化」当成目标。

自测题：
1. 为什么企业级系统里 Workflow 与 Agent 通常共存而非二选一？
2. 路由层该用 Workflow 还是 Agent？为什么？
3. 如何界定「哪些子任务该升级给 Agent」？
4. 分层后如何保证两层之间的失败不互相污染？

---

## 模块 E · 系统设计（第 19–24 节）

> 把学习成果转化成企业级 Agent 平台的系统设计能力。每道题讲架构、关键决策、失败模式、评测、成本和容量；每题都强调 Workflow 与 Agent 如何分工。

### 第 19 节 ｜ 系统设计答题模板（六步法）
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

案例：
- 拿 bot 当「小系统」过一遍六步：它为什么是 Workflow、若升级 Agent 架构怎么变。

产出：
- 一张 A4 系统设计速查卡。

自测题：
1. 为什么系统设计不能上来就画架构？
2. 什么是 Trade-off？
3. 设计中如何体现容量和成本意识？

### 第 20 节 ｜ 系统设计题 1：企业级 Agent 平台
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

案例：
- 把 bot 的「编码 Agent 适配层」放大成平台视角：它只是平台里一个 Agent 接入点的雏形。

产出：
- 一张完整架构图。
- 核心模块职责表。
- 6 种失败模式及应对方案。

自测题：
1. 从 0 到 1 如何建设企业级 Agent 平台？
2. 为什么要建设统一模型网关？
3. 工具注册中心应该管理哪些元数据？
4. 如何保证不同业务团队之间互不影响？

### 第 21 节 ｜ 系统设计题 2：企业客服 Agent
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

案例：
- bot 的「意图分发 + 人工确认门」已是客服雏形——本节把它扩成完整客服 Agent 架构。

产出：
- 一张状态机图。
- 一份转人工判定规则。

自测题：
1. 什么时候应该转人工？
2. 如何把上下文交给人工坐席？
3. 如何避免 Agent 在错误答案上不断重试？
4. 知识库更新如何避免旧知识污染新答案？

### 第 22 节 ｜ 系统设计题 3：代码 Agent
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

案例：
- bot 的 `execute_task` 是代码 Agent 调度的最小版——本节把它扩成带沙箱与审计的企业级形态。

产出：
- 权限分级矩阵。
- 代码 Agent 执行流程图。

自测题：
1. 代码 Agent 如何防止执行危险命令？
2. 如何限制 Agent 的文件和网络访问？
3. 修改错误代码后如何发现和回滚？
4. 如何让每次执行都可审计？

### 第 23 节 ｜ 系统设计题 4：多 Agent 协作
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

案例：
- 对比 bot 单 Agent 适配器：何时该拆多 Agent、拆了之后失败怎么定位。

产出：
- 多 Agent 架构图。
- 是否拆分多 Agent 的决策树。

自测题：
1. 多 Agent 的必要条件是什么？
2. Supervisor 模式有什么问题？
3. Agent 之间如何共享状态？
4. 多 Agent 失败时如何定位责任节点？

### 第 24 节 ｜ 系统设计题 5：Agent Gateway / 开放平台
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

案例：
- bot 的「编码 Agent 适配层」就是内部 gateway 雏形——本节把它做成多租户开放平台。

产出：
- Trace 字段表。
- 限流与计费方案。
- 模型网关架构图。

验收：
- 任一题都能先澄清需求，再画架构。
- 至少能讲出 3 个关键 Trade-off。
- 至少能列出 6 种失败模式及处置。
- 面对三层追问仍能给出有依据的答案（把第 21 节串讲能力落到这里）。

自测题：
1. 模型网关需要解决哪些问题？
2. 如何统计单次任务的真实成本？
3. 多租户限流如何设计？
4. 如何实现 Prompt 和模型版本灰度？

---

## 模块 F · 落地与复盘（第 25–30 节）

> 把 30 节成果收敛成「可负责企业级 Agent 平台」的能力——完成主项目、补齐分布式与工程化短板，沉淀技术负责人的架构评审、决策记录与跨团队对齐方法。

### 第 25 节 ｜ 主项目完整集成
**时间：90～120 分钟**

任务：
- 集成模型网关、Agent Runtime、工具中心、LangGraph、RAG、Memory。
- 完成竞品监控端到端流程（或直接以「改造后的 bot」作主项目 V0.8）。
- 补充配置文件、异常处理和启动脚本。

代码：
- 完成 `app.py` 或 FastAPI 入口。
- 增加一个 API：提交竞品分析任务。
- 增加一个 API：查询任务状态和结果。

产出：
- Agent Platform Lite V0.8（或改造后 bot 的 Agent 版）。
- 完整架构图。

验收：
- 一条请求可以从入口走到最终报告。
- 任务状态可查询。
- 关键步骤可追踪。

自测题：
1. 请介绍你的 Agent 平台架构。
2. 为什么这样划分模块？
3. 哪些环节是固定 Workflow，哪些环节由 Agent 决策？

### 第 26 节 ｜ 项目指标、故障和安全复盘
**时间：90 分钟**

任务：
- 汇总 30 条 Eval 测试结果。
- 统计成功率、工具调用准确率、P95 延迟、单任务成本。
- 记录 3 个真实失败案例。
- 检查 Prompt Injection、越权工具、跨租户数据访问。
- 编写项目安全检查清单。

案例：
- 复盘 bot 已踩的硬伤（README 故障表）：飞书超时重试、上下文溢出、编码外部不可控——把 Workflow 的坑和 Agent 的坑分开记。

产出：
- 项目质量报告。
- 安全检查清单。
- 三个故障故事。

验收：
- 不编造指标，未测量的数据明确标注为未测。
- 每个失败案例有现象、根因、处理和改进。
- 能解释 Agent 的安全边界。

自测题：
1. 你如何证明 Agent 的效果？
2. Prompt Injection 能彻底防止吗？
3. 多租户 RAG 如何避免数据串租户？
4. 你项目中最严重的失败是什么？

### 第 27 节 ｜ 项目复盘与架构讲解（2 / 10 / 30 分钟三档）
**时间：90 分钟**

任务：
- 准备 2 分钟版：业务背景 + 为什么用 Agent + 一句话成果。
- 准备 10 分钟版：架构取舍 + 关键指标 + 1 个失败案例。
- 准备 30 分钟版：白板从头推导架构，含 Trade-off 与容量。
- 每档都包含：背景 / 为什么 Agent / 架构取舍 / 指标 / 失败复盘。
- 用 bot 讲「从 Workflow 长成 Agent」的真实故事（呼应第 17–18 节）。

产出：
- 三档讲解提纲（可复用为技术评审 / 述职 / 内部分享素材）。

自测题：
1. 为什么这个场景需要 Agent？
2. 为什么不直接用规则引擎或普通 Workflow？
3. 项目里你亲自完成了哪些关键设计？
4. 如果重新做一次，你会改什么？

### 第 28 节 ｜ Java / 分布式 / Coding 复习
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

自测题：
1. 线程池参数如何设置？
2. 如何实现分布式幂等？
3. Redis 缓存与数据库如何保证一致性？
4. SSE 和 WebSocket 有什么区别？
5. Agent 工具执行为什么也需要并发控制？

### 第 29 节 ｜ 技术领导力与工程决策
**时间：90～120 分钟**

学习：
- 技术负责人（Tech Lead）/ 架构师（Staff Engineer）的职责边界。
- 架构决策记录（ADR）：何时写、写什么、怎么演进。
- 方案评审流程：反对意见清单、决策标准、复盘机制。
- 跨团队对齐：如何推动一个不归你管辖的技术方案。
- 技术债的量化、可视化与排期。

案例：
- 第 1–3 节的「Workflow vs Agent 判定清单」，正是技术负责人要给团队定的规范——本节把它落成 ADR 与评审清单。

资料：
- Google Engineering Practices：https://google.github.io/eng-practices/
- ADR 模板：https://adr.github.io/
- Staff Engineer 概念参考：https://staffeng.com/

任务：
- 为主项目写 1 份 ADR：是否引入 Agent / 为什么选 LangGraph / 为什么用 MCP。
- 模拟一次方案评审：列出至少 3 条反对意见与应对。
- 画一张「业务团队—平台—基础设施」职责对齐图。
- 对照技术负责人能力模型自评（分布式架构 / Agent 平台 / 工程化 / 技术领导力 / 业务理解），标注三态。

产出：
- ADR 模板 + 1 份真实 ADR。
- 方案评审清单（含反对意见应对）。
- 技术领导力自查表 + 能力雷达自评表（五维 + 状态）。

验收：
- 能说清在「做不做 / 怎么做 / 谁维护」上的决策框架。
- 能区分技术决策与流程决策，并说明各自落地方式。
- ADR 能回答「为什么不是更简单方案」。

自测题：
1. 技术负责人和架构师的核心区别是什么？
2. 如何推动一个跨团队但对你没有直接管辖权的技术方案？
3. 为什么要用 ADR 而不是只在 wiki 记结论？
4. 技术债如何量化并向业务方争取排期？
5. 你距离独立负责企业级 Agent 平台还差哪 2 项关键能力？

### 第 30 节 ｜ 综合复盘与 90 天进阶路线
**时间：4 小时**

任务：
- 回看 30 节全部产出（第 4 节起代码 / 时序图 / 报告）。
- 绘制能力地图：已会 / 会但没上过生产 / 不会。
- 写一份「后续 90 天」计划：真实业务场景落地、性能压测、线上值班、开源贡献。
- 整理可对外分享的技术资产（GitHub README / 公众号文章 / 内部 TechTalk）。
- 收尾：我的 bot 现在是 Workflow 还是 Agent，你怎么选（呼应第 1 节与第 17 节）。

产出：
- 30 节复盘报告（认知变化 + 最强 / 最弱项）。
- 能力地图（三态）。
- 90 天进阶计划（可验收节点）。
- 可分享资产清单。

验收：
- 能一句话说清这 30 节自己提升了什么。
- 90 天计划有可验收里程碑，且至少有 1 项对外沉淀。
- 能力地图能指导下一步，而非罗列知识点。

自测题：
1. 这 30 节你最大的认知变化是什么？
2. 如果要带一个新人重走这条路，你会怎么改顺序？
3. 哪些能力必须靠真实生产事故 / 值班才能补齐？

---

> 由源稿 Markdown 自动生成 · 改源稿后执行 `python3 scripts/gen_readme.py` 刷新。
