#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 learn-agent 仓库根目录 README.md。

读取《30 天学习与面试执行手册》源稿（Markdown），
自动解析 4 周 / 30 天的结构，加上仓库门面与进度总表，
输出到仓库根目录 README.md。

路径规则：所有路径相对本脚本自身，重跑即刷新，不硬编码绝对路径。
"""

import os
import re

# 脚本位置：learn-agent/scripts/gen_readme.py
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)                       # learn-agent/
# 源稿与 learn-agent 同级（都在 Agent30天计划 下），跨目录引用
SRC_MD = os.path.join(
    ROOT, "..", "Claw", "求职准备", "文档",
    "AI-Agent-30天学习执行手册.md",
)
OUT_MD = os.path.join(ROOT, "README.md")

# 已建的代码目录命名约定：day{N}
DAY_DIR_RE = re.compile(r"^###\s*Day\s*(\d+)[｜|]\s*(.+)$")
WEEK_RE = re.compile(r"^##\s*第\s*(\d+)\s*周[：:].*$")


def parse_days(src_path: str):
    """解析出 [(day_num, title, week_label), ...]。"""
    days = []
    cur_week = ""
    with open(src_path, "r", encoding="utf-8") as f:
        for line in f:
            mw = WEEK_RE.match(line)
            if mw:
                cur_week = f"第{mw.group(1)}周"
                continue
            md = DAY_DIR_RE.match(line)
            if md:
                days.append((int(md.group(1)), md.group(2).strip(), cur_week))
    return days


def build_progress_table(days):
    rows = ["## 学习进度", "",
            "| Day | 周 | 主题 | 代码目录 | 状态 |",
            "|----|----|------|---------|------|"]
    for num, title, week in days:
        ddir = f"day{num}"
        exists = os.path.isdir(os.path.join(ROOT, ddir))
        if exists:
            day_cell = f"[Day {num}]({ddir}/)"
            dir_cell = f"[{ddir}/]({ddir}/)"
            status = "✅ 已完成"
        else:
            day_cell = f"Day {num}"
            dir_cell = f"{ddir}/（待建）"
            status = "⬜ 待产"
        rows.append(f"| {day_cell} | {week} | {title} | {dir_cell} | {status} |")
    return "\n".join(rows)


def build_header():
    return "\n".join([
        "# learn-agent",
        "",
        "> **35 岁阿里后端，用 30 天把自己重训成 Agent 工程师 —— 配套学习代码库。**",
        "",
        "本仓库是公众号系列 **「30 天把自己重训成 Agent 工程师」**（公众号：**溪月散人**）的",
        "**代码落地**。计划本身见 [`AI-Agent-30天学习执行手册.html`](AI-Agent-30天学习执行手册.html)；",
        "这里把计划每天变成可运行、可 review、可提交的真实产物。",
        "",
        "## 这个仓库怎么用",
        "",
        "- **每天一个目录** `dayN/`，里面包含当天全部学习产物。",
        "- **每目录三件套**：① 可运行代码（零依赖，`python3 xxx.py` 直接跑）；",
        "  ② 时序图 / 架构图（GitHub 用 Mermaid，公众号用交互式 HTML）；",
        "  ③ `README.md`（目标 / 资料 / 验收 / 面试题）。",
        "- **进度驱动**：下面的进度表会自动识别哪些 `dayN/` 已建，已建的标 ✅ 并链接。",
        "- **改计划后重跑**：编辑源稿 Markdown，执行 `python3 scripts/gen_readme.py` 即可刷新本文件。",
        "",
        "## 关联资源",
        "",
        "- 30 天学习计划（自包含 HTML，可浏览器看 / 打印）：[`AI-Agent-30天学习执行手册.html`](AI-Agent-30天学习执行手册.html)",
        "- 同名公众号连载：搜索 **溪月散人**（《30 天把自己重训成 Agent 工程师》）",
        "",
        "---",
        "",
    ])


def main():
    if not os.path.isfile(SRC_MD):
        raise SystemExit(f"源稿不存在：{SRC_MD}")
    days = parse_days(SRC_MD)
    header = build_header()
    progress = build_progress_table(days)

    # 源稿正文：去掉首行 h1 标题（避免与根 README 的 # 冲突），其余原样保留
    with open(SRC_MD, "r", encoding="utf-8") as f:
        src_lines = f.read().splitlines()
    body = []
    started = False
    for i, line in enumerate(src_lines):
        if i == 0 and line.startswith("# "):
            continue  # 跳过源稿 h1
        if line.startswith("## 第"):
            started = True
        if started:
            body.append(line)

    doc = "\n".join([
        header,
        progress,
        "",
        "---",
        "",
        "## 30 天学习计划（总纲）",
        "",
        "\n".join(body),
        "",
        "---",
        "",
        "> 由源稿 Markdown 自动生成 · 改源稿后执行 `python3 scripts/gen_readme.py` 刷新。",
    ]).strip() + "\n"

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(doc)

    done = sum(1 for n, _, _ in days if os.path.isdir(os.path.join(ROOT, f"day{n}")))
    print(f"已生成 {OUT_MD}")
    print(f"解析到 {len(days)} 天 / 当前已完成 {done} 天")


if __name__ == "__main__":
    main()
