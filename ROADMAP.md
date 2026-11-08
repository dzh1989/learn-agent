# 学习路线图（ROADMAP）

> AI Agent 实战成长计划 的核心路线与项目演进。课程编号连续 1–36，专题扩展不固定。

## 一、能力演进路线

```
初级（6 篇） ──► 中级（16 篇） ──► 高级（14 篇） ──► 专题扩展（不固定）
 认知 + 第一个Agent   核心技术         工程化 + 平台化     前沿 / 专项深入
```

## 二、主项目演进（AI SaaS 竞品研究 Agent）

| 阶段 | 对应课程 | 项目能力 |
|---|---|---|
| 初级 | 第 1–6 节 | 搭 Agent Loop 雏形，完成单工具竞品初步分析 |
| 中级 | 第 7–22 节 | 接 Tool Registry / MCP / RAG / Memory / LangGraph，形成可运行骨架 |
| 高级 | 第 23–36 节 | 工程化（可靠/安全/可观测/网关）+ 综合项目五部曲（设计/开发/增强/评测/演示）+ 平台架构 + 部署 |
| 专题 | T1–T6 | 评测深入 / Skills / MCP 进阶 / LangGraph 进阶 / Agentic Coding / 新技术追踪 |

## 三、课程地图

### 初级（建立认知，写出第一个 Agent）
1. 大模型基础认知　2. Prompt Engineering　3. Workflow vs Agent　4. Agent 基本组成
5. Agent Loop 手写　6. Function Calling + 第一个简单 Agent

### 中级（掌握核心技术）
- 模块一 工具与执行：7 Tool Registry　8 MCP 原理　9 MCP 实战　10 执行范式
- 模块二 上下文与记忆：11 Context Engineering　12 RAG 基础　13 RAG 检索　14 RAG 实战　15 Memory　16 多轮对话
- 模块三 工作流编排：17 混合编排　18 LangGraph 核心　19 Checkpoint/HITL
- 模块四 质量与效果：20 Evaluation　21 中级项目实战　22 中级复盘

### 高级（工程化与平台化）
- 模块五 工程可靠性：23 Runtime　24 可靠性　25 安全　26 可观测性　27 成本优化　28 模型网关
- 模块六 系统架构与生产：29 Multi-Agent　30–34 综合项目五部曲　35 企业级平台　36 部署监控

### 专题扩展
T1 评测深入　T2 Skills　T3 MCP 进阶　T4 LangGraph 进阶　T5 Agentic Coding　T6 新技术追踪

## 四、代码目录约定

每节课一个 `dayNN-*` 目录（NN 与课程编号永久对齐），内含可运行代码 + README。
主项目统一放在 `projects/saas-competitor-agent/`，专题放在 `topics/`。
