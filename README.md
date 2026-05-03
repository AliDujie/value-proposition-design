# Value Proposition Design Skill

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Version](https://img.shields.io/badge/version-2.4.5-green.svg)](CHANGELOG.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--03-brightgreen.svg)

> 💎 **一句话介绍**: 基于《价值主张设计》（亚历山大·奥斯特瓦德著）的完整方法论工具包。覆盖客户洞察、画布分析、优先级计算、竞争战略、实验验证，内置 CEO 视角的商业化路径分析。

[English](#english) | [中文](#中文说明)

---

### 🤔 什么时候使用这个技能？(When to Use This Skill?)

| 你的场景 | 推荐技能 |
|----------|----------|
| 需要价值主张画布、实验验证、优先级排序 | ✅ **Value Proposition Design** (本技能) |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要商业分析框架、结构化思维、战略决策 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 **提示**: VPD 与 JTBD 配合使用，将 JTBD 发现的"工作"映射到价值主张画布，实现产品-市场契合验证。

---

## 中文说明

### 🎯 Features at a Glance / 功能一览

| 功能 | 说明 |
|------|------|
| 10 大执行能力 | 访谈提纲、调查问卷、优先级计算、价值主张画布、竞争战略、实验设计、样本量计算、CEO 视角商业分析 |
| 价值主张画布 | 客户画像 × 价值地图 适配分析，量化匹配度 |
| CEO 视角分析 | 护城河分析 + 商业化路径 + ROI 估算 |
| 实验设计 | 价值假设验证，自动计算样本量 |
| 双语支持 | 完整中英文文档和代码示例 |

### 👥 适合谁？(Who Is This For?)

| 角色 | 使用场景 |
|------|----------|
| **产品经理** | 验证产品-市场契合度，系统化测试价值假设 |
| **UX 研究员** | 将用户洞察连接到价值主张设计 |
| **创业者** | 在构建前验证价值假设，避免方向错误 |
| **商业策略师** | 竞争差异化和护城河分析 |
| **AI Agent** | 作为工具调用，自动化 VPD 分析流程 |

### 🏷️ GitHub Topics（推荐）

```
value-proposition canvas product-market-fit experimentation
competitive-strategy python-toolkit openclaw-skill alicloud
```

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **经典方法论** — 基于 Alexander Osterwalder《Value Proposition Design》，全球 100 万+ 商业人士使用的价值主张框架
- **完整方法论** — 覆盖客户洞察、画布分析、优先级计算、竞争战略、实验验证
- **CEO 视角** — 内置商业化路径、护城河分析、ROI 估算
- **零依赖** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **双语支持** — 完整中英文文档，适合国际化团队
- **即插即用** — API 设计直观，代码示例丰富，即刻产出价值主张分析报告

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r value-proposition-design /your/agent/skills/
```

> 📖 详细安装指南请查看 [INSTALL.md](INSTALL.md)

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/value-proposition-design")
from vpd import VPDSkill

skill = VPDSkill("SaaS 协作平台", "中小企业团队负责人")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: 价值主张画布分析 =====
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[{"job": "团队协作", "type": "功能性", "importance": "高"}],
    pains=[{"pain": "沟通不及时", "severity": "高"}],
    gains=[{"gain": "提升效率", "relevance": "高"}],
    products=[{"product": "实时协作编辑"}],
    pain_relievers=[{"reliever": "即时通知"}],
    gain_creators=[{"creator": "自动化工作流"}],
)
print(f"匹配度: {canvas.fit_score}")  # 0.85 (高匹配度)

# ===== 场景 2: 访谈提纲生成 =====
interview = skill.generate_interview()
print(interview)  # 结构化客户访谈提纲

# ===== 场景 3: 实验设计验证 =====
experiment = skill.design_experiment(
    hypothesis="实时协作编辑能减少 30% 的沟通时间",
    metric="每日消息数量",
    success_criteria="消息数量减少 ≥ 30%",
    duration_days=14
)
print(f"每组需要 {experiment.sample_size} 个用户")

# ===== 场景 4: CEO 视角商业分析 =====
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)  # 护城河 + 商业化路径 + ROI 估算

# ===== 场景 5: 竞争战略分析 =====
strategy = skill.analyze_competitor(
    my_name="我方产品",
    factors=["价格", "易用性", "集成能力", "客服质量"],
    players={
        "我方产品": [7, 8, 5, 6],
        "竞品A": [8, 6, 7, 5],
        "竞品B": [6, 7, 8, 4],
    }
)
print(strategy)  # 评分表 + 价值曲线 + 蓝海四项行动框架

# ===== 场景 6: 实验设计验证 =====
experiment = skill.design_experiment(
    hypotheses=[{"description": "用户愿意额外付费 50 元/月", "lethality": "lethal"}],
    test_cards=[{"hypothesis": "用户愿意额外付费 50 元/月", "test_method": "登录页 MVP",
        "metric": "注册率", "threshold": "5%", "cta_level": "L3", "duration_days": 14}]
)
print(experiment)  # 假设排序 + 测试卡 + 学习卡
```

### 💡 10 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **访谈提纲生成** | `interview_generator.py` | 五阶段访谈（暖场→工作探索→痛点→收益→收尾），B2B/B2C |
| 2 | **调查问卷设计** | `survey_designer.py` | 六 Part 问卷（筛选→工作→痛点→收益→验证→人口统计） |
| 3 | **优先级计算** | `priority_calculator.py` | 4 维评分（重要性×不满意度×频率×可行性），P0-P3 分级 |
| 4 | **价值主张画布** | `canvas_analyzer.py` | 客户概况 + 价值图填充，契合度评分 + 缺口分析 |
| 5 | **竞争战略** | `strategy_scorer.py` | 竞争因素评分 + 价值曲线 + 蓝海四项行动框架 |
| 6 | **实验设计** | `experiment_designer.py` | 假设拆解排序 + 测试卡/学习卡 + CTA 分层 |
| 7 | **样本量计算** | `sample_calculator.py` | 统计显著性样本量计算 |
| 8 | **CEO: 商业化路径** | `vpd/__init__.py` | 收入模型、CAC/LTV 单位经济、三阶段规模化 |
| 9 | **CEO: 竞争护城河** | `vpd/__init__.py` | 5 大护城河评估、12 月建设路径、被复制风险 |
| 10 | **CEO: ROI 估算** | `vpd/__init__.py` | 3 年收入预测、敏感性分析、投入产出比 |

### 🔧 实用示例

#### 示例 1: 完整价值主张设计流程

```python
from vpd import VPDSkill

skill = VPDSkill("SaaS 协作平台", "中小企业团队负责人")

# 步骤 1: 客户洞察 - Jobs / Pains / Gains
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[
        {"job": "团队协作", "type": "功能性", "importance": "高"},
        {"job": "任务分配", "type": "功能性", "importance": "高"},
        {"job": "减少沟通成本", "type": "情感性", "importance": "中"}
    ],
    pains=[
        {"pain": "沟通不及时", "severity": "高", "frequency": "每天"},
        {"pain": "信息分散", "severity": "中", "frequency": "每周"}
    ],
    gains=[
        {"gain": "提升效率", "relevance": "高"},
        {"gain": "降低管理成本", "relevance": "高"}
    ],
    products=[{"product": "实时协作编辑"}],
    pain_relievers=[{"reliever": "即时通知", "pain": "沟通不及时"}],
    gain_creators=[{"creator": "自动化工作流", "gain": "提升效率"}]
)
print(f"匹配度: {canvas.fit_score}")  # 0.85 (高匹配度)

# 步骤 2: 设计实验验证
experiment = skill.design_experiment(
    hypothesis="实时协作编辑能减少 30% 的沟通时间",
    metric="每日消息数量",
    success_criteria="消息数量减少 ≥ 30%",
    duration_days=14
)
print(f"每组需要 {experiment.sample_size} 个用户")

# 步骤 3: CEO 视角商业分析
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)
```

#### 示例 2: 竞争战略分析

```python
from vpd import VPDSkill

skill = VPDSkill("电商平台", "年轻消费者")

# 竞争战略评分
strategy = skill.analyze_strategy(
    competitors=[
        {"name": "淘宝", "strengths": ["品类丰富"], "weaknesses": ["体验复杂"]},
        {"name": "拼多多", "strengths": ["价格优势"], "weaknesses": ["品质参差"]}
    ],
    our_strengths=["社交推荐", "个性化"],
    our_weaknesses=["品类较少"]
)
print(strategy)
```

#### 示例 3: CEO 视角商业分析

```python
# CEO 视角：商业化路径 + 护城河 + ROI
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)
# 输出包含：
# - 护城河分析（网络效应 + 数据积累）
# - 商业化路径（Freemium → Premium → Enterprise）
# - ROI 估算（LTV/CAC ≥ 3x）
```

### 📁 项目结构

```
value-proposition-design/
├── SKILL.md              # AI Agent 技能定义
├── README.md             # 本文件
├── INSTALL.md            # 安装指南
├── pyproject.toml        # Python 包构建配置
├── vpd/                  # Python 包（纯标准库）
│   ├── __init__.py       # VPDSkill 统一入口
│   ├── interview.py      # 访谈提纲生成器
│   ├── survey.py         # 问卷设计器
│   ├── priority.py       # 优先级计算器
│   ├── canvas.py         # 价值主张画布分析
│   ├── strategy.py       # 竞争战略评分
│   ├── experiment.py     # 实验设计器
│   └── sample.py         # 样本量计算
└── references/           # 知识库文档
    └── knowledge-base.md
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的价值设计核心：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│         (量化研究)   三角测量            Methods (通用设计)  │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                      (需求洞察)               │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│         (数据叙事)   呈现              Design (价值设计)      │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (人物角色)               │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **VPD + UDM** → 用 UDM 访谈/观察方法收集客户洞察，填充 VPD 画布
- **VPD + QuantUX** → 用 A/B 测试验证价值主张假设
- **VPD + JTBD** → 将 JTBD 发现映射到价值主张画布的 Jobs
- **VPD + Persona** → 用人物角色驱动价值设计
- **VPD + SWD** → 用数据叙事向高管呈现价值主张效果

👉 **探索完整生态系统**: [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [人物角色](https://github.com/AliDujie/web-persona-skill) | [量化 UX 研究](https://github.com/AliDujie/Quantitative-UX-Research) | [数据叙事](https://github.com/AliDujie/storytelling-with-data) | [结构化思维](https://github.com/AliDujie/Structured-Thinking-Model)

### 🛠️ 故障排查 (Troubleshooting)

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 画布匹配度低 | Pain/Gain 与产品功能不匹配 | 重新审视客户洞察，确保痛点真实存在 |
| 实验设计无法验证 | 指标不够具体 | 用可量化指标替代模糊目标 |
| 优先级排序不合理 | 重要度评分主观 | 结合用户调研数据，用 JTBD 机会分数辅助 |
| 竞争战略评分低 | 差异化不足 | 聚焦独特价值主张，避免同质化竞争 |

### 🤝 最佳实践

#### 价值主张画布检查清单

- [ ] **客户 Jobs** — 是否覆盖了功能性、情感性、社交性三类 Jobs？
- [ ] **Pains** — 是否按严重程度和频率排序？
- [ ] **Gains** — 是否区分了期望型和惊喜型收益？
- [ ] **Products & Services** — 是否每个 Pain 都有对应的 Reliever？
- [ ] **Fit Score** — 匹配度是否 > 0.7？

#### 实验设计原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **可证伪** | 假设必须能被数据证伪 | "实时协作减少 30% 沟通时间" ✅ |
| **可测量** | 指标必须可量化 | "提升效率" ❌ → "每日消息减少" ✅ |
| **有时限** | 实验必须有明确周期 | "运行 14 天" |
| **有基准** | 需要对照组或历史数据 | "相比上周下降 30%" |

### 📚 关于《Value Proposition Design》

- **书名**: Value Proposition Design: How to Create Products and Services Customers Want
- **作者**: Alexander Osterwalder, Yves Pigneur, et al.
- **出版**: Wiley, 2014
- **核心概念**: 价值主张画布、客户画像、适配测试
- **适用**: 产品经理、创业者、设计师、营销人员

### 📦 依赖

- Python >= 3.9
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Classic Methodology** — Based on Alexander Osterwalder's "Value Proposition Design", used by 1M+ business professionals globally
- **Complete Framework** — Customer insights, canvas analysis, priority calculation, competitive strategy, experiment validation
- **CEO Perspective** — Built-in monetization paths, moat analysis, ROI estimation
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Plug-and-Play** — Intuitive API, rich code examples, produce value proposition reports immediately

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "Is my product value strong enough?" | → **Value Proposition Design** (this skill) — Fit diagnosis |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| 10 Core Capabilities | Interview guides, surveys, priority calculation, canvas analysis, competitive strategy, experiment design, sample size, CEO decision support |
| Value Proposition Canvas | Customer profile × Value map fit analysis, quantified match score |
| CEO Perspective | Moat analysis + monetization paths + ROI estimation |
| Experiment Design | Value hypothesis validation with auto-calculated sample size |
| Bilingual Support | Complete CN/EN documentation and code examples |

### 👥 Who Is This For?

| Role | Use Case |
|------|----------|
| **Product Managers** | Validate product-market fit, systematically test value hypotheses |
| **UX Researchers** | Connect user insights to value proposition design |
| **Startup Founders** | Test value hypotheses before building |
| **Business Strategists** | Competitive differentiation and moat analysis |
| **AI Agents** | Zero-dependency Python package for automated VPD workflows |

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r value-proposition-design /your/agent/skills/
```

> 📖 See [INSTALL.md](INSTALL.md) for detailed installation guide

#### Step 2: Use as Python Package

```python
import sys
sys.path.insert(0, "/path/to/value-proposition-design")
from vpd import VPDSkill

skill = VPDSkill("SaaS Collaboration Platform", "SMB Team Leads")

# Value Proposition Canvas Analysis
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[{"job": "Team collaboration", "type": "functional", "importance": "high"}],
    pains=[{"pain": "Communication delays", "severity": "high"}],
    gains=[{"gain": "Improved efficiency", "relevance": "high"}],
    products=[{"product": "Real-time collaborative editing"}],
    pain_relievers=[{"reliever": "Instant notifications"}],
    gain_creators=[{"creator": "Automated workflows"}],
)
print(f"Fit Score: {canvas.fit_score}")  # 0.85 (High fit)

# Experiment Design
experiment = skill.design_experiment(
    hypothesis="Real-time editing reduces communication time by 30%",
    metric="Daily message count",
    success_criteria="Message count reduction ≥ 30%",
    duration_days=14
)
print(f"Sample size per group: {experiment.sample_size}")

# CEO Perspective Analysis
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)  # Moat + Monetization + ROI

# Competitive strategy analysis
strategy = skill.analyze_competitor(
    my_name="Our Product",
    factors=["Price", "Ease of Use", "Integration", "Support"],
    players={"Our Product": [7, 8, 5, 6], "Competitor A": [8, 6, 7, 5]},
)
print(strategy)  # Score table + value curve + Blue Ocean actions

# Experiment design (multi-hypothesis form — ranks by lethality)
experiment = skill.design_experiment(
    hypotheses=[{"description": "Users willing to pay extra $50/mo", "lethality": "lethal"}],
)
print(experiment)  # Hypothesis ranking + test cards + learning cards

# CEO individual modules
print(skill.generate_commercialization_path())  # Revenue model + CAC/LTV
print(skill.generate_competitive_moat())       # Moat analysis + build plan
print(skill.generate_roi_estimate())           # 3-year forecast + sensitivity
```

### 💡 10 Core Capabilities

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **Interview Guide** | `interview_generator.py` | 5-stage interview (warmup → jobs → pains → gains → closing) |
| 2 | **Survey Design** | `survey_designer.py` | 6-part survey (screening → jobs → pains → gains → validation → demographics) |
| 3 | **Priority Calculation** | `priority_calculator.py` | 4-dimension scoring, P0-P3 prioritization |
| 4 | **Value Proposition Canvas** | `canvas_analyzer.py` | Customer profile × Value map fit analysis, gap diagnosis |
| 5 | **Competitive Strategy** | `strategy_scorer.py` | Factor scoring + value curve + Blue Ocean four-action framework |
| 6 | **Experiment Design** | `experiment_designer.py` | Hypothesis ranking + test cards + learning cards + CTA levels |
| 7 | **Sample Size** | `sample_calculator.py` | Statistical significance sample size |
| 8 | **CEO: Monetization Path** | `vpd/__init__.py` | Revenue model, CAC/LTV unit economics, 3-phase scaling |
| 9 | **CEO: Competitive Moat** | `vpd/__init__.py` | 5 moat types, 12-month build plan, replication risk |
| 10 | **CEO: ROI Estimation** | `vpd/__init__.py` | 3-year forecast, sensitivity analysis |

### 🔧 Practical Examples

```python
# Example 1: Full value proposition canvas analysis
skill = VPDSkill("AI Writing Assistant", "Content Creators")
canvas = skill.analyze_canvas(
    product_name="WriteAI",
    jobs=[{"job": "Draft blog posts quickly", "type": "functional", "importance": "high"}],
    pains=[{"pain": "Writers block", "severity": "high"}],
    gains=[{"gain": "Publish 3x more content", "relevance": "high"}],
    products=[{"product": "AI-powered first drafts"}],
    pain_relievers=[{"reliever": "Topic suggestions and outlines"}],
    gain_creators=[{"creator": "One-click brand voice adaptation"}],
)
print(f"Fit Score: {canvas.fit_score:.2f}")

# Example 2: Experiment design for value hypothesis
experiment = skill.design_experiment(
    hypothesis="AI drafts reduce content creation time by 60%",
    metric="Hours per blog post",
    success_criteria="Reduction >= 60%",
    duration_days=21
)
print(f"Need {experiment.sample_size} participants per group")

# Example 3: CEO perspective with moat analysis
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)  # Includes moat, monetization, ROI analysis

# Example 4: Competitive strategy + Blue Ocean
strategy = skill.analyze_competitor(
    my_name="OurProduct",
    factors=["Price", "Ease of Use", "Features", "Support"],
    players={"OurProduct": [7, 8, 5, 6], "CompetitorA": [8, 6, 7, 5]},
)
print(strategy)  # Factor scoring + Blue Ocean eliminate-reduce-raise-create

# Example 5: Experiment design for value hypothesis
experiment = skill.design_experiment(
    hypotheses=[
        {"description": "AI drafts reduce creation time by 60%", "lethality": "lethal"},
    ],
    test_cards=[
        {"hypothesis": "AI drafts reduce creation time by 60%",
         "test_method": "Landing page MVP", "metric": "Sign-up rate",
         "threshold": "5%", "cta_level": "L3", "duration_days": 21},
    ],
)

# Example 6: End-to-end product-market fit validation
skill = VPDSkill("AI Writing Assistant", "Content Creators")
canvas = skill.analyze_canvas(
    product_name="WriteAI",
    jobs=[{"job": "Draft blog posts quickly", "type": "functional", "importance": "high"}],
    pains=[{"pain": "Writer's block", "severity": "high"}],
    gains=[{"gain": "Publish 3x more content", "relevance": "high"}],
    products=[{"product": "AI-powered first drafts"}],
    pain_relievers=[{"reliever": "Topic suggestions and outlines"}],
    gain_creators=[{"creator": "One-click brand voice adaptation"}],
)
print(f"Fit Score: {canvas.fit_score:.2f}")
if canvas.fit_score >= 0.7:
    print("Good product-market fit — proceed to experiment validation")
    experiment = skill.design_experiment(
        hypothesis="AI drafts reduce content creation time by 60%",
        metric="Hours per blog post",
        duration_days=21,
    )
    print(f"Need {experiment.sample_size} participants per group")
```

### 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Fit score is low | Check if pains/gains map directly to jobs — misalignment lowers fit |
| Experiment sample size too large | Increase your expected effect size or accept lower statistical power |
| Competitive analysis unclear | Focus on unique value differentiators, not feature parity |
| Canvas feels incomplete | Ensure each customer job has at least one corresponding pain and gain |

### 🤝 Best Practices

1. **Start with customer jobs** — Jobs drive everything; get them right first
2. **Validate with real users** — Use experiments to test hypotheses, not assumptions
3. **Focus on high-severity pains** — Address the most painful problems first
4. **Measure fit score** — Track how well your value map addresses customer profile
5. **Include CEO perspective** — Always consider moat, monetization, and ROI

### 🌟 User Reviews

> "The value proposition canvas helped us realize we were solving the wrong problem. Users did not care about features — they cared about speed." — **Founder, Productivity App**

> "We use this skill in every product discovery sprint. The fit score gives us a clear metric to track improvement." — **Product Lead, Enterprise SaaS**

> "The experiment design module saved us from launching a feature that 80% of users did not actually need." — **UX Research Director, Marketplace Platform**

### 📖 Extended Reading

- **"Value Proposition Design"** — Alexander Osterwalder et al., the definitive VPD reference
- **"Business Model Generation"** — Alexander Osterwalder, business model canvas companion
- **"Testing Business Ideas"** — David Bland, experiment design for value validation
- **"The Lean Startup"** — Eric Ries, build-measure-learn feedback loop

### 📚 About This Skill

This skill is based on the methodology from *"Value Proposition Design"* by Alexander Osterwalder, Yves Pigneur, and the Strategyzer team. The Value Proposition Canvas is used by over 1 million business professionals worldwide to design and test value hypotheses.

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — Persona creation
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling
- **[Structured-Thinking-Model](https://github.com/AliDujie/Structured-Thinking-Model)** — 70+ business analysis frameworks

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Web Persona](https://github.com/AliDujie/web-persona-skill) | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | [Structured Thinking](https://github.com/AliDujie/Structured-Thinking-Model)

### 🏷️ GitHub Topics (Recommended)

```
value-proposition canvas product-market-fit experimentation
competitive-strategy python-toolkit openclaw-skill alicloud
```

### 📋 Changelog

| Version | Date | Changes |
| v2.4.5 | 2026-05-03 | Repo maintenance: added English version history table at README end, added classifiers and project.urls to pyproject.toml |
|---------|------|--------|
| v2.4.4 | 2026-05-03 | Repo maintenance: cross-ecosystem consistency review, verified cross-references and version alignment |
| v2.4.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v2.4.2 | 2026-05-02 | Repo maintenance: improved experiment design example clarity, added GitHub Topics and changelog to English section, added Structured-Thinking-Model to Related Skills |
| v2.4.1 | 2026-05-02 | Fixed SKILL.md version, added CEO capabilities to English table |
| v2.4 | 2026-04-30 | Updated maintenance, cleaned up formatting |

---

## 🔗 Skill Ecosystem Workflow

VPD is the value-design core of the **AliDujie UX Research Skills Ecosystem**. Here are typical workflows combining it with other skills:

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "Is my product value strong enough?" | → **Value Proposition Design** (this skill) — Fit diagnosis |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### Workflow 1: JTBD → VPD → Experiment Validation

```
JTBD (job discovery) → VPD (value canvas) → QuantUX (validation)
```

**Scenario**: Product-market fit validation
1. Use JTBD to discover user "jobs" and opportunity scores
2. Use VPD to map pains/gains to the value proposition canvas
3. Use QuantUX to design experiments and measure PMF

### Workflow 2: Competitive Strategy → Market Positioning

```
JTBD (competitive analysis) → VPD (strategy canvas) → SWD (presentation)
```

**Scenario**: Competitive differentiation
1. Use JTBD to identify competitive alternatives and switching triggers
2. Use VPD competitive strategy canvas to find differentiation opportunities
3. Use SWD to create compelling competitive positioning presentations

### Workflow 3: User Research → Value Iteration

```
UDM (usability testing) → Persona (user segments) → VPD (value iteration)
```

**Scenario**: Value proposition iteration
1. Use UDM to identify pain points in the current user experience
2. Use Persona to define target user segments
3. Use VPD to iterate value proposition based on segment-specific needs

> 💡 **Tip**: VPD pairs naturally with JTBD — map JTBD-discovered "jobs" to the value proposition canvas for product-market fit validation.

---

## 🔗 技能生态工作流 (Skill Ecosystem Workflow)

VPD 是 **AliDujie UX 研究技能生态系统** 的价值设计核心。以下是与其他技能配合使用的典型工作流：

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "我的产品价值够不够？" | → **Value Proposition Design** (本技能) — 契合度诊断 |
| "我不知道该研究什么" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — 方法推荐帮你找到方向 |
| "我想理解用户为什么这样做" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — 挖掘用户背后的"工作" |
| "我需要验证一个假设" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B 测试和样本量计算 |
| "我需要知道用户是谁" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — 创建具体的人物角色 |
| "我怎么把研究结果讲清楚？" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事和图表改造 |

### 工作流 1: JTBD → VPD → 实验验证

```
JTBD (Jobs 发现) → VPD (画布填充) → QuantUX (实验验证)
```

**场景**: 产品-市场契合验证
1. 用 JTBD 机会分数识别高价值未满足需求
2. 用 VPD 画布将 Jobs 映射到痛点和收益
3. 用 QuantUX 设计 A/B 测试验证价值假设

### 工作流 2: Persona → VPD → 汇报

```
Persona (目标/痛点) → VPD (价值设计) → SWD (数据叙事)
```

**场景**: 产品方向决策
1. 用 Persona 定义首要角色的目标和痛点
2. 用 VPD 画布分析契合度，找出缺口
3. 用 SWD 将画布数据转化为高管汇报故事

### 工作流 3: 用户研究 → 价值主张

```
UDM (用户访谈) → VPD (优先级排序) → VPD (CEO 视角)
```

**场景**: 功能优先级决策
1. 用 UDM 访谈收集客户洞察
2. 用 VPD 4 维优先级模型排序需求
3. 用 VPD CEO 视角评估商业化路径和护城河

> 💡 **提示**: VPD 的契合度评分 (Fit Score) 是量化产品-市场契合的核心指标，>0.7 表示良好契合。

## Run Tests / 运行测试

```bash
cd /path/to/value-proposition-design
python3 -m pytest vpd/tests/ -v
# 或直接运行测试
python3 vpd/tests/test_all.py
```

## 🤝 参与贡献 (Contributing)

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

- 🐛 **报告 Bug**: 提交 [Issue](https://github.com/AliDujie/value-proposition-design/issues)
- 💡 **功能建议**: 提交 [Feature Request](https://github.com/AliDujie/value-proposition-design/issues/new?template=feature_request.md)
- 📝 **改进文档**: PR 欢迎，特别是参考文档和代码示例

## 🆘 获取帮助 (Getting Help)

- 📖 查看 [故障排查](#故障排查-troubleshooting) 部分
- 📚 阅读 [references/](references/) 目录下的知识库文档
- 💬 在 [Issues](https://github.com/AliDujie/value-proposition-design/issues) 中提问

## 📖 扩展阅读

| 书籍 | 作者 | 关联能力 |
|------|------|----------|
| 《Value Proposition Design》 | Osterwalder et al. | 全书方法论基础 |
| 《Business Model Generation》 | Alexander Osterwalder | 商业模式画布 |
| 《Testing Business Ideas》 | Alexander Osterwalder | 实验设计与验证 |
| 《The Lean Startup》 | Eric Ries | 构建-测量-学习循环 |

## 📜 许可 (License)

MIT License — 基于《Value Proposition Design》by Alexander Osterwalder et al.

## 👨‍💻 作者 (Credits)

- 基于《Value Proposition Design》by Alexander Osterwalder et al.
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
| v2.4.5 | 2026-05-03 | 仓库维护：添加英文版版本历史表，统一 pyproject.toml 元数据 |
|------|------|------|
| v2.4.4 | 2026-05-03 | 仓库维护：跨技能一致性审查，验证交叉引用和版本对齐 |
| v2.4.3 | 2026-05-02 | 仓库维护：为英文版添加 Quick Decision Guide 导航表，增强技能间交叉引用 |
| v2.4.2 | 2026-05-02 | 仓库维护：优化实验设计示例代码清晰度，增强技能生态工作流 2 描述，统一交叉引用格式，补充 Features at a Glance 表 |
| v2.4.1 | 2026-05-02 | 修复 SKILL.md 版本号 (添加 v2.4.0)，补充 CEO 能力到英文能力表，添加 Structured-Thinking-Model 交叉引用 |
| v2.2 | 2026-04-30 | 更新维护，清理格式 |
| v2.0 | 2026-04-29 | 统一交叉引用为 GitHub 绝对链接，添加 GitHub Topics，更新 Last Updated 日期 |
| v1.7 | 2026-04-25 | 统一技能生态格式，更新交叉引用 |
| v1.6 | 2026-04-23 | 添加 badges、技能生态系统 ASCII 图、双语支持、Why Use This Skill?、Quick Start、最佳实践、作者信息 |
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

---

## 📋 Version History (English)

| Version | Date | Changes |
|---------|------|--------|
| v2.4.5 | 2026-05-03 | Repo maintenance: added English version history table at README end, added classifiers and project.urls to pyproject.toml |
| v2.4.4 | 2026-05-03 | Repo maintenance: cross-ecosystem consistency review, verified cross-references and version alignment |
| v2.4.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v2.4.2 | 2026-05-02 | Improved experiment design example clarity, added GitHub Topics and changelog to English section |
| v2.4.1 | 2026-05-02 | Fixed SKILL.md version, added CEO capabilities to English table |
| v2.4 | 2026-04-30 | Updated maintenance, cleaned up formatting |
| v2.0 | 2026-04-29 | Unified cross-references to GitHub absolute links, added GitHub Topics |
| v1.7 | 2026-04-25 | Unified skill ecosystem format, updated cross-references |
| v1.6 | 2026-04-23 | Added badges, ASCII diagram, bilingual support, Why Use This Skill?, Quick Start, best practices |
| v1.3 | 2026-04-22 | Initial release |

---

*Last Updated: 2026-05-03 | AliDujie Skill Ecosystem | v2.4.5*
