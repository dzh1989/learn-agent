#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 learn-agent 仓库根目录 README.md（产品化落地页）。

读取《AI Agent 实战成长计划 · 系统学习手册》源稿（Markdown），
自动解析 初级/中级/高级/专题扩展 的层级、模块与课程，生成：
  - 项目介绍 / 特色 / 适合人群 / 最终成果
  - 学习路线（层级 + 模块总览）
  - 课程目录（自动：层级 → 模块 → 课程 + 公众号推荐标题 + 状态）
  - 主项目介绍 / 环境准备 / 快速开始 / 学习方法 / 公众号入口 / 更新日志

路径规则：所有路径相对本脚本自身，重跑即刷新，不硬编码绝对路径。
"""

import glob
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)                       # learn-agent/
SRC_MD = os.path.join(
    ROOT, "..", "Claw", "求职准备", "文档",
    "AI-Agent-系统学习手册.md",
)
OUT_MD = os.path.join(ROOT, "README.md")

TIERS = ["初级", "中级", "高级", "专题扩展"]
LESSON_RE = re.compile(r"^###\s*第\s*(\d+)\s*节\s*[｜|]?\s*(.*)$")
TOPIC_RE = re.compile(r"^###\s*专题\s*(\S+?)\s*[｜|]\s*(.*)$")
META_RE = re.compile(r"^\*\*\s*(等级|模块|公众号推荐标题|推荐学习时间)\s*：\*\*\s*(.*)$")


def parse(src_path: str):
    tiers = []
    cur_tier = None
    cur_lesson = None
    with open(src_path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            for t in TIERS:
                if s.startswith("## ") and t in s:
                    cur_tier = {"title": t, "lessons": []}
                    tiers.append(cur_tier)
                    cur_lesson = None
                    break
            else:
                if not cur_tier:
                    continue
                m = LESSON_RE.match(s)
                if m:
                    cur_lesson = {"no": int(m.group(1)), "title": m.group(2).strip() or s,
                                 "meta": {}, "rec": ""}
                    cur_tier["lessons"].append(cur_lesson)
                    continue
                mt = TOPIC_RE.match(s)
                if mt:
                    cur_lesson = {"no": 0, "title": "专题 " + mt.group(1) + " ｜ " + mt.group(2).strip(),
                                 "meta": {}, "rec": ""}
                    cur_tier["lessons"].append(cur_lesson)
                    continue
                if cur_lesson is not None:
                    mm = META_RE.match(s)
                    if mm:
                        if mm.group(1) == "公众号推荐标题":
                            cur_lesson["rec"] = mm.group(2).strip()
                        else:
                            cur_lesson["meta"][mm.group(1)] = mm.group(2).strip()
    return tiers


def lesson_dir(num: int):
    if num == 0:
        return None
    cands = sorted(glob.glob(os.path.join(ROOT, f"day{num:02d}-*")))
    return os.path.basename(cands[0]) if cands else None


def build_course_dir(tiers):
    out = ["## 课程目录（自动生成）", ""]
    for t in tiers:
        is_topic = t["title"] == "专题扩展"
        out.append(f"### {'专题扩展' if is_topic else t['title']}")
        out.append("")
        # 按模块分组
        modules = {}
        for d in t["lessons"]:
            mod = d["meta"].get("模块", "其他")
            modules.setdefault(mod, []).append(d)
        for mod, lessons in modules.items():
            out.append(f"**{mod}**")
            for d in lessons:
                no = f"第{d['no']}节" if d["no"] else "专题"
                ddir = lesson_dir(d["no"])
                if ddir:
                    title_cell = f"[第 {d['no']} 节 · {d['title']}]({ddir}/)" if d["no"] else f"[{d['title']}]({ddir}/)"
                    status = "✅"
                else:
                    title_cell = f"第 {d['no']} 节 · {d['title']}" if d["no"] else d["title"]
                    status = "⬜"
                rec = f"（公众号：{d['rec']}）" if d["rec"] else ""
                out.append(f"- {title_cell} {rec} {status}")
            out.append("")
    return "\n".join(out)


def main():
    if not os.path.isfile(SRC_MD):
        raise SystemExit(f"源稿不存在：{SRC_MD}")
    tiers = parse(SRC_MD)
    core = sum(len(t["lessons"]) for t in tiers if t["title"] != "专题扩展")
    total = sum(len(t["lessons"]) for t in tiers)
    course_dir = build_course_dir(tiers)

    doc = f"""# AI Agent 实战成长计划

> 从理解原理，到独立构建，再到工程化落地。
> 面向有一定编程基础的开发者 / AI 技术爱好者的 **AI Agent 系统实战课程**。

一个用真实代码与可运行项目驱动、由浅入深掌握 AI Agent 的系统学习仓库。
不再以「30 天 / 固定节数」设限——初级 + 中级约可在 30 个学习日内攻完，高级与专题作为持续延展。

## 这个项目能给你什么

- **真实可跑的代码**：每节课配套最小可运行示例（多数支持离线 Mock，无需 API Key 即可看懂核心机制）。
- **一条清晰路线**：初级建立认知并写出第一个 Agent → 中级掌握核心技术 → 高级工程化与平台化 → 专题深入前沿。
- **一个贯穿项目**：AI SaaS 竞品研究 Agent 随课程从 Loop 雏形成长为可评测、可部署的系统。
- **读者视角的文章**：公众号每篇都从真实问题切入，避免堆术语与 AI 味。

## 适合谁

- 会用 Python、想系统搞懂 AI Agent 的开发者。
- 已经会调大模型 API，但不满足于"调封装"、想理解底层的人。
- 希望带着新人一起学、或沉淀成技术专栏的作者。

## 最终学习成果

完成核心 {core} 篇 + 专题后，你将能够：**独立设计并实现一个具备工具调用、知识检索、记忆、工作流编排与评测能力的 Agent 系统**，并理解企业级 Agent 平台的架构与工程化要点。

## 学习路线

| 层级 | 篇数 | 目标 | 对应模块 |
|---|---|---|---|
| 初级 | 6 | 建立认知，写出第一个简单 Agent | 基础认知 / Agent 组成 / Agent Loop / Function Calling |
| 中级 | 16 | 掌握核心技术，构建具备实际任务能力的 Agent | 工具执行 / 上下文与记忆 / 工作流编排 / 质量与效果 |
| 高级 | 14 | 掌握工程化、系统架构与平台化设计 | 工程可靠性 / 系统架构与生产实践 |
| 专题扩展 | 不固定 | 深入新技术与专项主题 | 评测深入 / Skills / MCP 进阶 / LangGraph 进阶 / Agentic Coding / 新技术追踪 |

{course_dir}

## 主项目：AI SaaS 竞品研究 Agent

用户输入若干 SaaS 产品名 + 研究目标，Agent 辅助完成资料收集、整理、对比、报告生成。
能力分阶段演进：初级搭 Loop 雏形 → 中级接工具 / MCP / RAG / Memory / LangGraph → 高级完成闭环 + 评测 + 部署。
落地目录：`projects/saas-competitor-agent/`。

## 环境准备

- Python 3.10+
- 真实模型调用：设置 `OPENAI_API_KEY`（或其他 OpenAI 兼容厂商的 `BASE_URL` / `MODEL`）
- 多数课程支持 `--mock` 离线运行，先看机制再接真模型

## 快速开始

```bash
# 1) 大模型基础：无需 Key 即可看离线示例
cd day01-llm-basics && python3 00_hello_llm.py --mock

# 2) 手写 Agent Loop（离线可跑）
cd ../day05-agent-loop && python3 day5_agent_loop.py --mock

# 3) 改手册后刷新本 README
python3 scripts/gen_readme.py
```

## 学习方法

- **先理解再深入**：每节课从"它解决什么问题"切入，再讲原理、再动手。
- **代码优先**：先跑通示例，再读源码；优先 Mock，再接真实模型。
- **项目贯穿**：每学一个能力，就挂到竞品研究 Agent 上，避免学散。
- **公众号联动**：每天记录知识点 / 坑 / 素材，周末整理成文章（认知 / 实战 / 复盘三类交替）。

## 公众号系列入口

公众号：**溪月散人**。搜索即可关注，配合本仓库一起学习。

## 关联资源

- 完整学习计划（自包含 HTML，可浏览器看 / 打印）：[`AI-Agent-系统学习手册.html`](AI-Agent-系统学习手册.html)
- 路线图：[`ROADMAP.md`](ROADMAP.md)
- 更新日志：[`CHANGELOG.md`](CHANGELOG.md)

---

> 由源稿 Markdown 自动生成 · 改源稿后执行 `python3 scripts/gen_readme.py` 刷新课程目录。
"""
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(doc)

    done = sum(1 for t in tiers for d in t["lessons"] if lesson_dir(d["no"]) is not None)
    print(f"已生成 {OUT_MD}")
    print(f"解析到 {len(tiers)} 层级 / 核心 {core} 篇 / 专题 {total-core} 篇；代码已完成 {done} 节")


if __name__ == "__main__":
    main()
