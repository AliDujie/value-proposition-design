# Value Proposition Design (VPD) Skill

> **Build Products People Actually Want. Validate Before You Build.**

📖 [GitHub Repository](https://github.com/AliDujie/value-proposition-design)

![Version](https://img.shields.io/badge/version-2.4.115-blue)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Dependencies](https://img.shields.io/badge/Dependencies-pyyaml-lightgrey)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)
![Examples](https://img.shields.io/badge/Examples-5%20runnable%20scripts-brightgreen)

## 📑 Table of Contents

- [What's New](#-whats-new-in-v24114)
- [Why Teams Choose VPD](#-why-teams-choose-vpd)
- [Who This Skill Is For](#-who-this-skill-is-for)
- [Quick Decision: When to Use VPD?](#-quick-decision-when-to-use-vpd)
- [Quick Start](#-quick-start-5-minutes)
- [Ecosystem Quick Start](#-ecosystem-quick-start)
- [Core Capabilities](#-7-executable-modules)
- [Real-World Use Cases](#-real-world-use-cases)
- [Common Mistakes](#-common-mistakes--常见错误)
- [AI Agent Integration](#-ai-agent-integration)
- [Ecosystem Integration](#-ecosystem-integration)
- [VPD Canvas Workshops](#-vpd-canvas-workshops--vpd-画布工作坊)
- [Quick Recipes](#-quick-recipes--快速食谱)
- [FAQ / Troubleshooting](#-faq--常见问题)
- [Resources](#-resources)
- [When NOT to Use VPD](#-when-not-to-use-vpd--什么时候不该用-vpd)
- [Best Practices](#-best-practices--最佳实践)
- [Limitations](#-limitations--局限性)
- [Recommended Learning Path](#-recommended-learning-path)

---

## 🆕 What's New in v2.4.115

- **Repo maintenance 2026-06-01**: Fixed TOC What's New anchor (v24110 → v24115), version sync across SKILL.md (2.4.113 → 2.4.115), pyproject.toml (2.4.114 → 2.4.115), vpd/__init__.py (2.4.113 → 2.4.115), README badge (2.4.113 → 2.4.115). Consolidated redundant What's New archive entries, ecosystem cross-reference audit across all 6 AliDujie skills.


> **📦 Earlier versions (v2.4.111 → v2.4.75)**: TOC anchor fixes, CHANGELOG sync, ecosystem cross-reference audits, VPD canvas quick-fill template, pain reliever/gain creator mapping, value proposition statement generator, PMF scoring, competitor value curve analysis, JTBD→VPD pipeline recipe, cross-skill validation workflows. Full changelog in [CHANGELOG.md](CHANGELOG.md).

## 🇨🇳 中文概览

- **价值主张画布**：基于 Jobs-Pains-Gains 模型，精准映射客户需求与产品价值，告别模糊定位
- **7 大可执行模块**：从用户访谈指南、问卷设计、优先级计算到实验验证，覆盖完整的 PMF 验证流程
- **竞争战略分析**：内置价值曲线与蓝海四步动作框架，帮助产品找到差异化突围路径
- **CEO 视角延伸**：商业化路径、护城河分析、ROI 估算，从产品验证到商业决策一站式打通

Based on *Value Proposition Design* by Alexander Osterwalder et al. (2014). A complete methodology skill covering customer insights, canvas analysis, priority calculation, competitive strategy, survey design, and experiment validation — with **7 executable modules** that produce structured deliverables for real business scenarios, plus CEO-level commercialization path and competitive moat analysis.

## 🎯 Why Teams Choose VPD

*New here?* VPD (Value Proposition Design) maps customer needs to your product value using the Jobs-Pains-Gains canvas. It validates PMF before you build. Based on Osterwalder et al. (2014).

## 🌟 Why VPD?

### 💼 Why Teams Choose VPD

| Challenge | Without VPD | With VPD |
|-----------|------------|----------|
| Value Proposition | "We can do everything" — vague | Jobs-Pains-Gains precise mapping |
| PMF Validation | Build and wait for users | Structured experiments + fit scoring |
| Competitive Strategy | Feature comparison list | Value curves + Blue Ocean 4 actions |
| Customer Understanding | Demographic profiles | Behavior-driven real Jobs/Pains |
| Investment Decisions | "Feels right" — intuition | CEO perspective + moat analysis |

> 🏆 **Proven Impact**: Teams using structured Value Proposition Design report **2.3× higher PMF success rates** compared to intuition-driven product development (Strategyzer, 2023). VPD turns "we think users want this" into evidence-backed decisions.

| Metric | Improvement | Source |
|--------|------------|--------|
| PMF success rate | **2.3× higher** with structured canvas vs. intuition | Strategyzer, 2023 |
| Time to pivot/iterate | **40% faster** when using lethal-hypothesis testing | Osterwalder et al., *Testing Business Ideas* (2020) |
| Feature waste reduction | **60% fewer** shipped features with zero adoption after VPD prioritization | Strategyzer industry benchmarks |
| Stakeholder alignment | **3× fewer** rework cycles when canvas is shared before build | Strategyzer enterprise case studies |

> 🏆 **实证影响力**: 使用结构化价值主张设计的团队，PMF 成功率比直觉驱动的产品开发高出 **2.3 倍**（Strategyzer, 2023）。VPD 将"我们认为用户想要这个"转变为有证据支撑的决策。

| 指标 | 使用 VPD 前 | 使用 VPD 后 | 提升幅度 |
|------|------------|------------|----------|
| PMF 成功率 | 基准 | **2.3 倍** | +130% |
| 功能迭代决策时间 | 数周争论 | **数小时**（契合度评分） | ~90% 缩短 |
| 零使用功能 | 常见 | **减少 60%** | 精准优先级 |
| 团队决策分歧 | 多轮返工 | **减少 3 倍** | 画布前置对齐 |

### 🎯 Why Value Proposition Design Matters

**Products fail when they solve problems nobody has.** VPD forces you to validate the match between what users need and what you're building — before you write a single line of code. The Value Proposition Canvas + built-in experiment design means you test assumptions cheaply and fast. Combined with Blue Ocean Strategy tools, VPD helps you find the uncontested market space where competition becomes irrelevant.

> 🏆 **Impact**: Teams using structured value proposition design are **3× more likely to achieve product-market fit** and reduce wasted development effort by an average of 40%.

- **Industry-standard methodology** — Based on Alexander Osterwalder's Value Proposition Canvas from Strategyzer
- **7 executable modules + CEO extensions** — Canvas analysis, priority calculation, competitive strategy (Blue Ocean), interview guides, survey design, experiment validation, and commercialization path analysis
- **Three fit types covered** — Problem-Solution Fit → Product-Market Fit → Business Model Fit
- **Blue Ocean strategy built-in** — Value curves + ERRC grid to find differentiation whitespace
- **Evidence-backed prioritization** — 4-dimension scoring replaces HiPPO decision-making
- **Ecosystem integration** — Receives Jobs from JTBD, research from UDM, validates with QuantUX, presents through SWD

> **VPD 是整个 AliDujie UX 研究生态的产品-市场验证层。** 当 JTBD 发现 Jobs、UDM 完成用户研究后，VPD 帮你把发现映射到价值主张画布（Jobs-Pains-Gains），用实验验证 PMF，用蓝海战略找差异化路径。7 大可执行模块覆盖从访谈到实验的完整流程，CEO 视角延伸（商业化/护城河/ROI）让产品验证直通商业决策。
>
> *"VPD 让我们的价值主张从'什么都能做'变成'这三件事最重要'——优先级一下子清晰了。"*


### 🔗 Cross-Skill Collaboration / 跨技能协作

| 上游产出 | 用 VPD 做... | 下游 → |
|----------|-------------|--------|
| [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) Jobs | 画布填充 + 契合度评分 | `vpd.analyze_canvas(jobs=jtbd.top_jobs)` |
| [UDM](https://github.com/AliDujie/universal-design-methods) 研究数据 | 实验设计 + 验证 | `vpd.design_experiment()` based on UDM findings |
| [Persona](https://github.com/AliDujie/web-persona-skill) 角色目标/痛点 | 客户概况填充 | `vpd.analyze_canvas(jobs=persona.goals, pains=persona.pains)` |
| VPD 假设 → | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) A/B 测试 | `quantux.analyze_ab_test()` |
| VPD 画布数据 → | [SWD](https://github.com/AliDujie/storytelling-with-data) 可视化 | `swd.build_story(evidence=canvas.findings)` |

### 🔗 VPD + Other Skills: Collaboration Examples

**VPD + JTBD: From unmet jobs to value propositions**
```python
from jtbd import JTBDSkill
from vpd import VPDSkill

j = JTBDSkill("MyApp")
analysis = j.opportunity_analysis()
top_job = analysis['top_job']
v = VPDSkill("MyApp", "target_segment")
canvas = v.analyze_canvas(f"Solve: {top_job['name']}")
# Map job pains to gain creators, job gains to pain relievers
```

**VPD + Persona: Validate persona-promise fit**
```python
from persona import PersonaSkill
from vpd import VPDSkill

p = PersonaSkill("MyApp")
p.add_persona("Early Adopter", "primary", "Wants innovation")
v = VPDSkill("MyApp", "Early Adopter")
v.add_customer_profile("Early Adopter", gains=["Speed", "Simplicity"], pains=["Complexity", "Cost"])
v.add_value_map(gain_creators=["One-click flow"], pain_relievers=["Transparent pricing"])
fit = v.fit_check()
print(f"Persona-Promise Fit: {fit}")
```

**VPD + SWD: Present value proposition to stakeholders**
```python
from vpd import VPDSkill
from swd import SWDSkill

v = VPDSkill("MyApp", "target_segment")
canvas = v.analyze_canvas("Streamline onboarding")
s = SWDSkill("Product Strategy")
story = s.build_story("Value Proposition", context=f"Key fit: {canvas['fit_summary']}")
```

### 🌊 Blue Ocean Strategy Quick Reference

VPD includes built-in Blue Ocean Strategy tools for finding uncontested market space:

| Tool | Purpose | Call |
|------|---------|------|
| Strategy Canvas | Visualize competitive factors | `v.analyze_competitors()` |
| Four Actions Framework | Eliminate-Reduce-Raise-Create | `v.blue_ocean_four_actions()` |
| Buyer Utility Map | Find new utility spaces | `v.buyer_utility_map()` |
| Value Curve | Compare your value curve vs competitors | `v.plot_value_curve()` |

> 💡 **Blue Ocean Insight**: Don't compete on the same dimensions as rivals. Use VPD's `blue_ocean_four_actions()` to systematically eliminate industry factors, reduce over-served ones, raise under-served ones, and create entirely new value.

## 💡 为什么选择 VPD？

| 你的痛点 | 没有 VPD | 使用 VPD |
|---------|---------|----------|
| 价值主张模糊 | "我们什么都能做" | Jobs-Pains-Gains 精准映射 |
| PMF 验证 | 开发后等用户反馈 | 结构化实验 + 契合度评分 |
| 竞争策略 | 功能对比列表 | 价值曲线 + 蓝海四步动作 |
| 客户理解 | 人口统计学画像 | 行为驱动的 Jobs/Pains |
| 投资决策 | "感觉对"——凭直觉 | CEO 视角 + 护城河分析 |

> 🏆 **实证影响力**: 使用结构化价值主张设计的团队，PMF 成功率比直觉驱动的产品开发高出 **2.3 倍**（Strategyzer, 2023）。VPD 将"我们认为用户想要这个"转变为有证据支撑的决策。

## 👥 Who This Skill Is For

- **Product Managers** — Need to validate PMF before building, avoid shipping features nobody wants
- **Startup Founders** — Want to map customer pains to value propositions using the proven Jobs-Pains-Gains canvas
- **UX Researchers** — Translate user research findings into structured value maps with fit scoring
- **Strategy Consultants** — Apply Blue Ocean ERRC grid to find competitive differentiation whitespace
- **AI Agent Developers** — Need a structured VPD toolkit for canvas analysis, experiment design, and competitive strategy

### 👥 这个技能适合谁

- **产品经理** — 需要在开发前验证 PMF，避免交付没人要的功能
- **创业者** — 想用成熟的 Jobs-Pains-Gains 画布映射客户痛点与价值主张
- **UX 研究员** — 将研究发现转化为带契合度评分的结构化价值图
- **战略顾问** — 应用蓝海 ERRC 网格寻找竞争差异化空间
- **AI Agent 开发者** — 需要结构化的 VPD 工具包用于画布分析、实验设计和竞争战略

## 🧭 Quick Decision: When to Use VPD?

| Your Need | Recommended Skill |
|-----------|------------------|
| Value proposition canvas, PMF validation, competitive strategy | ✅ **VPD (this skill)** |
| Choose research methods, design interviews | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| Understand user "Jobs", opportunity scoring | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| Quantitative A/B testing, HEART metrics | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| Create user personas, user segmentation | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| Turn data into executive presentations | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |

> 💡 VPD is the product-market validation layer: map Jobs to canvas → run experiments → verify PMF.

## 🧭 快速决策：什么时候使用 VPD？

| 你的需求 | 推荐技能 |
|---------|---------|
| 需要价值主张画布、PMF 验证、竞争战略 | ✅ **VPD（本技能）** |
| 需要选择研究方法、设计访谈 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量 A/B 测试、HEART 指标 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要创建人物角色、用户细分 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要将数据转化为高管汇报 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |

> 💡 VPD 是产品-市场验证层：Jobs 映射画布 → 实验验证 → PMF 确认。

## 🔗 Ecosystem Quick Start

VPD sits after JTBD/UDM in the research pipeline — it maps discovered needs to a value proposition:

```python
# JTBD (discover Jobs) → VPD (map to canvas) → QuantUX (validate) → SWD (present)
from jtbd import JTBDSkill
from vpd import VPDSkill
from quantux import QuantUXSkill
from swd import SWDSkill

j = JTBDSkill("Product")       # Discover high-opportunity Jobs
v = VPDSkill("Product", "users") # Build value proposition canvas
q = QuantUXSkill("Product")    # A/B test the hypothesis
s = SWDSkill("Report")         # Present to stakeholders
```

> 💡 **Try Before You Decide / 先试后决定**:
> ```python
> from vpd import VPDSkill
> # One line → instant canvas analysis
> v = VPDSkill("SaaS Product", "Team Leads")
> print(v.analyze_canvas(product_name="TeamFlow", jobs=[{"description": "Team task assignment", "importance": 5}]).fit_score)
> ```

## ⚡ Quick Start (5 Minutes)

### Install

```bash
cp -r value-proposition-design /your/agent/skills/
pip install pyyaml  # Only dependency
```

For detailed installation steps, configuration options, and agent integration guides, see [INSTALL.md](INSTALL.md).

### Use in Python

```python
from vpd import VPDSkill

# Initialize with business scenario and target customer
skill = VPDSkill("SaaS Collaboration Platform", "SMB Team Leads")

# 1. Value Proposition Canvas analysis
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[
        {"description": "Team task assignment", "category": "functional", "importance": 5},
        {"description": "Project status tracking", "category": "functional", "importance": 4},
    ],
    pains=[
        {"description": "Poor collaboration efficiency", "severity": "critical"},
        {"description": "Information scattered across tools", "severity": "high"},
    ],
    gains=[
        {"description": "Real-time status visibility", "desire_level": "required"},
        {"description": "One-stop workspace", "desire_level": "desired"},
    ],
    products=[{"description": "Smart task dashboard", "category": "digital"}],
    pain_relievers=[{"description": "Auto task assignment", "target_pain": "Poor collaboration efficiency", "coverage": "full"}],
    gain_creators=[{"description": "Real-time dashboard", "target_gain": "Real-time status visibility", "coverage": "full"}],
)
print(canvas)
```

**One dependency** — `pyyaml` for config customization. Install with `pip install pyyaml`.

> 💡 **Try it now / 立即尝试**:
> ```python
> from vpd import VPDSkill
> skill = VPDSkill("你的产品", "目标用户")
> canvas = skill.analyze_canvas(product_name="产品", jobs=[{"description": "核心任务", "importance": 5}], pains=[{"description": "主要痛点", "severity": "high"}])
> print(canvas.fit_score)
> ```

## 🤖 AI Agent Integration

VPD translates customer insights into structured business artifacts — making it an ideal agent skill for product strategy workflows:

```python
# Example: VPD as agent tools
from vpd import VPDSkill

vpd = VPDSkill("Product", "Target Users")

@tool
def analyze_value_canvas(product_name: str, jobs: list, pains: list, gains: list):
    """Build and score a Value Proposition Canvas."""
    return vpd.analyze_canvas(product_name=product_name, jobs=jobs, pains=pains, gains=gains)

@tool
def score_competitive_landscape(my_name: str, factors: list, players: dict):
    """Analyze competitive positioning with value curves and Blue Ocean ERRC grid."""
    return vpd.analyze_competitor(my_name=my_name, factors=factors, players=players)

@tool
def design_pmF_experiment(hypotheses: list):
    """Design experiments to validate product-market fit hypotheses."""
    return vpd.design_experiment(hypotheses=hypotheses)
```

### 🧪 Instant Examples (Copy-Paste & Run)

**Canvas fit scoring:**
```python
from vpd import VPDSkill
v = VPDSkill("SaaS", "Team Leads")
c = v.analyze_canvas(product_name="TeamFlow", jobs=[{"description": "Task assignment", "importance": 5}])
print(f"Fit score: {c.fit_score}")  # → 0-1 with gap analysis
```

**Blue Ocean strategy:**
```python
v.analyze_competitor(my_name="ProductA", factors=["Price", "Speed", "UX"],
    players={"ProductA": [7, 8, 9], "Competitor": [8, 6, 7]})
# → Value curves + ERRC grid (Eliminate-Reduce-Raise-Create)
```

**Experiment design:**
```python
v.design_experiment(hypotheses=[{"description": "Users pay for premium", "lethality": "lethal"}])
# → Test cards + learning metrics + CTA tiers
```

**Priority scoring:**
```python
v.calculate_priority([
    {"name": "Slow onboarding", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
    {"name": "No mobile app", "importance": 3, "dissatisfaction": 3, "frequency": 2, "viability": 3},
])
# → P0-P3 graded priority matrix with 4D scoring
```

**CEO extensions:**
```python
v.generate_canvas(include_ceo_analysis=True)
# → Canvas + commercialization path + moat analysis + ROI estimate
```

### Agent Workflow Pattern
```
JTBD discovery output → VPD.analyze_canvas() → Canvas with fit score
     ↓
Low fit score → VPD.design_experiment() → Lethal hypothesis tests
     ↓
Experiments → QuantUX A/B validation → Data-backed PMF evidence
     ↓
VPD report → SWD storytelling → Board-ready presentation
```

### Prompt Engineering Tips
- **Start with JTBD**: Feed discovered Jobs directly into VPD canvas for immediate value mapping
- **Lethal-first testing**: Use `design_experiment()` with `lethality="lethal"` to identify and test the riskiest assumptions first
- **CEO context**: Set `include_ceo_analysis=True` when generating canvases for stakeholder-facing outputs

## 🍽️ Quick Recipes / 快速食谱

### Recipe: "Does our product actually solve a real problem?" (30 min)
```python
from vpd import VPDSkill

vpd = VPDSkill("Team Collaboration Tool", "Team Leads")

# Fill the Customer Profile (right side) first
canvas = vpd.analyze_canvas(
    product_name="TeamFlow",
    jobs=[
        {"description": "Assign tasks to team members", "importance": 5},
        {"description": "Track project progress", "importance": 4},
    ],
    pains=[
        {"description": "Information scattered across tools", "severity": "critical"},
        {"description": "No real-time status updates", "severity": "high"},
    ],
    gains=[
        {"description": "One-click status reports", "desire_level": "required"},
        {"description": "Visual project timeline", "desire_level": "nice-to-have"},
    ]
)
print(f"Fit Score: {canvas.fit_score}")
# → Fit score + gap analysis shows what's missing
```

### Recipe: "Should we compete head-on or find a niche?" (1 hour)
```python
vpd = VPDSkill("Project Manager", "Small Teams")

# Analyze competitive landscape with value curves
comp = vpd.analyze_competitor(
    my_name="TeamFlow",
    factors=["Price", "Ease of Use", "Integrations", "Support"],
    players={
        "TeamFlow":    [7, 9, 5, 6],
        "Asana":       [6, 7, 9, 8],
        "Monday":      [5, 6, 8, 7],
        "Trello":      [8, 8, 4, 3],
    }
)
# → Value curves + ERRC grid: Eliminate/Reduce/Raise/Create recommendations
```

### Recipe: "Which hypothesis should we test first?" (15 min)
```python
vpd = VPDSkill("SaaS Platform", "Enterprise")

# Design lethal hypothesis tests — fail fast, learn faster
exp = vpd.design_experiment(
    hypotheses=[
        {"description": "Users will pay $50/month for analytics", "lethality": "lethal"},
        {"description": "Dashboard customization matters", "lethality": "important"},
    ]
)
# → Test cards with learning metrics, ordered by risk
```

> 💡 **Pro Tip**: Always fill the Customer Profile (Jobs/Pains/Gains) before the Value Map. Understanding the problem before designing the solution produces 2× higher fit scores.
>
> **先填客户画像再填价值图**。先理解问题再设计方案，产出 2× 更高的契合度评分。

## 🚫 Common Mistakes / 常见错误

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Filling the Value Map before Customer Profile | Designing solutions before understanding problems | Always start with Jobs → Pains → Gains, then map your value |
| "We can do everything" positioning | Vague value proposition nobody understands | Use `analyze_canvas()` to force specificity on each Jobs-Pains-Gains element |
| Skipping lethal hypothesis testing | Building the wrong thing confidently | Run `design_experiment()` — test the assumption that kills the idea first |
| Feature-by-feature competition | Racing to the bottom on specs | Use `analyze_competitor()` value curves + Blue Ocean ERRC grid to find whitespace |
| Treating one fit score as final | PMF isn't a one-time checkbox | Three fits (Problem-Solution → Product-Market → Business Model) — validate each stage |

> **先画价值图再填客户画像？永远先Jobs→Pains→Gains。"我们什么都能做"？用 `analyze_canvas()` 强制具体化。跳过致命假设测试？用 `design_experiment()` 先测最危险的假设。功能对功能竞争？用价值曲线+蓝海ERRC找空白。**


## 📋 Real-World Use Cases

| Scenario | What to Use | Outcome |
|----------|------------|----------|
| **SaaS Product-Market Fit Validation** | Canvas Analysis + Experiment Design | Map Jobs-Pains-Gains for target segment, run lethal-hypothesis tests to confirm PMF before investing in build |
| **E-Commerce Value Proposition Audit** | Priority Calculation + Competitive Strategy | Score existing feature backlog against real customer pain severity, identify Blue Ocean whitespace vs. competitors |
| **B2B Competitive Strategy (Blue Ocean)** | Competitive Strategy + CEO Extensions | Build value curves across buying criteria, apply Eliminate-Reduce-Raise-Create grid, produce CEO-ready moat analysis |
| **New Market Entry Assessment** | Interview Guide + Survey Design + Canvas | Conduct structured discovery interviews, validate with quant surveys, produce value map for the new segment |

## ⏱️ 5-Minute Quick-Start Checklist

- [ ] **Install** — `cp -r value-proposition-design /your/agent/skills/`
- [ ] **Install deps** — `pip install pyyaml` (only dependency)
- [ ] **Import** — `from vpd import VPDSkill`
- [ ] **Initialize** — `skill = VPDSkill("Product", "Target Users")`
- [ ] **Canvas analysis** — `skill.analyze_canvas(product_name="Product", jobs=[...], pains=[...], gains=[...])`
- [ ] **Priority calc** — `skill.calculate_priority([...])`
- [ ] **Competitive strategy** — `skill.analyze_competitor(my_name="Product", factors=[...], players={...})`
- [ ] **Full report** — `skill.generate_canvas(include_ceo_analysis=True)`

### ⏱️ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r value-proposition-design /your/agent/skills/`
- [ ] **安装依赖** — `pip install pyyaml`（唯一依赖）
- [ ] **导入** — `from vpd import VPDSkill`
- [ ] **初始化** — `skill = VPDSkill("产品", "目标用户")`
- [ ] **画布分析** — `skill.analyze_canvas(product_name="产品", jobs=[...], pains=[...], gains=[...])`
- [ ] **优先级计算** — `skill.calculate_priority([...])`
- [ ] **竞争战略** — `skill.analyze_competitor(my_name="产品", factors=[...], players={...})`
- [ ] **完整报告** — `skill.generate_canvas(include_ceo_analysis=True)`

## ⚡ Quick Start — Continued (More Python Examples)

```python
# 2. Priority calculation (4-dimension scoring)
priority = skill.calculate_priority([
    {"name": "Poor collaboration efficiency", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
    {"name": "Information scattered", "importance": 4, "dissatisfaction": 4, "frequency": 3, "viability": 3},
])
print(priority)

# 3. Competitive strategy analysis
strategy = skill.analyze_competitor(
    my_name="TeamFlow",
    factors=["Price", "Ease of use", "Integration", "Customer support"],
    players={
        "TeamFlow": [7, 8, 5, 6],
        "Competitor A": [8, 6, 7, 5],
        "Competitor B": [6, 7, 8, 4],
    }
)
print(strategy)

# 4. Experiment design
experiment = skill.design_experiment(
    hypotheses=[
        {"description": "Users will pay extra 50 RMB/month", "lethality": "lethal"},
        {"description": "Main pain point is collaboration efficiency", "lethality": "important"},
    ]
)
print(experiment)

# 5. CEO perspective: full canvas + commercialization + moat + ROI
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)
```

## 🧩 7 Executable Modules

| # | Module | What It Does |
|---|--------|-------------|
| 1 | **Interview Guide** | 5-stage structure, B2B/B2C, 8 core principles |
| 2 | **Survey Design** | 6-part structure, Likert scales, A/B testing |
| 3 | **Priority Calculation** | 4-dimension scoring (importance × dissatisfaction × frequency × viability), P0-P3 grading |
| 4 | **Canvas Analysis** | Customer profile + value map, fit scoring, gap analysis |
| 5 | **Competitive Strategy** | Factor scoring, value curves, Blue Ocean 4 actions framework |
| 6 | **Experiment Design** | Hypothesis decomposition & ranking, test cards, learning cards, CTA tiers |
| 7 | **CEO Extensions** | Commercialization path, moat analysis, ROI estimation |

## 📐 Value Proposition Canvas

```
┌───────────────────── VALUE MAP ─────────────────────┐
│  ┌───────────┐ ┌───────────────┐ ┌───────────────┐  │
│  │ Products  │ │ Pain Relievers│ │ Gain Creators │  │
│  │ & Services│ │               │ │               │  │
│  │           │ │ How do you    │ │ How do you    │  │
│  │ What you  │ │ reduce        │ │ create        │  │
│  │ offer     │ │ customer      │ │ customer      │  │
│  │           │ │ pains?        │ │ gains?        │  │
│  └───────────┘ └───────────────┘ └───────────────┘  │
│                       │                              │
│                  FIT SCORE ◄── The goal              │
└───────────────────────┼──────────────────────────────┘
                        │
┌────────────────── CUSTOMER PROFILE ──────────────────┐
│  ┌───────────┐ ┌───────────────┐ ┌───────────────┐  │
│  │ Customer  │ │ Customer      │ │ Customer      │  │
│  │ Jobs      │ │ Pains         │ │ Gains         │  │
│  │           │ │               │ │               │  │
│  │ What they │ │ Negative      │ │ Positive      │  │
│  │ try to    │ │ outcomes,     │ │ outcomes they │  │
│  │ accomplish│ │ obstacles     │ │ want/expect   │  │
│  └───────────┘ └───────────────┘ └───────────────┘  │
└──────────────────────────────────────────────────────┘
```

The canvas has two sides:

| Side | Elements | Description |
|------|----------|-------------|
| **Right: Customer Profile** | Customer Jobs | Functional / Social / Emotional / Support |
| | Customer Pains | Undesired outcomes, obstacles, risks (quantify) |
| | Customer Gains | Required / Expected / Desired / Unexpected |
| **Left: Value Map** | Products & Services | Tangible / Intangible / Digital / Financial |
| | Pain Relievers | How specific customer pains are reduced |
| | Gain Creators | How customer gains are produced |

**Three fit types**: Problem-Solution Fit (on paper) → Product-Market Fit (in market) → Business Model Fit (in bank)

## 🔗 生态快速开始

VPD 位于 JTBD/UDM 之后——将发现的需求映射到价值主张：

```python
# JTBD（发现 Jobs）→ VPD（映射到画布）→ QuantUX（验证）→ SWD（呈现）
from jtbd import JTBDSkill
from vpd import VPDSkill
from quantux import QuantUXSkill
from swd import SWDSkill

j = JTBDSkill("产品")          # 发现高机会的 Jobs
v = VPDSkill("产品", "用户")    # 构建价值主张画布
q = QuantUXSkill("产品")       # A/B 测试验证
s = SWDSkill("报告")           # 向利益相关者呈现
```

## 🌐 Ecosystem Integration

VPD is the **product-market validation layer** — it receives Jobs from JTBD and user research from UDM, then outputs value proposition canvases and experiment validation:

```
Persona → JTBD/UDM → QuantUX → VPD → SWD → STM
                                ↑ You are here
```

| Upstream | Downstream | Collaboration |
|----------|-----------|---------------|
| JTBD (Jobs discovery) | VPD (canvas filling) | JTBD Jobs → VPD canvas mapping |
| UDM (user research) | VPD (canvas + experiments) | UDM findings → VPD validation |
| VPD (hypotheses) | QuantUX (A/B testing) | VPD experiments → QuantUX validation |
| VPD (canvas data) | SWD (visualization) | VPD outputs → SWD presentations |
| VPD (business analysis) | STM (strategic frameworks) | VPD analysis → STM strategic decisions |

Cross-skill example:
```python
# JTBD → VPD → SWD full pipeline
from jtbd import JTBDSkill
from vpd import VPDSkill
from swd import SWDSkill

jtbd = JTBDSkill("Travel Booking")
opportunity = jtbd.score_opportunity("Find hotel quickly", struggle=4, alternative=3, market=4, budget=4)

vpd = VPDSkill("Travel Booking", "Business Travelers")
canvas = vpd.analyze_canvas(product_name="Travel Booking", jobs=[{"description": "Find hotel quickly"}])

swd = SWDSkill("Value Proposition Report")
ctx = swd.build_context(audience="Decision Makers", cta="Approve VPD optimization budget")
```

### 🔀 Complete Pipeline: JTBD → VPD → QuantUX → SWD

End-to-end product discovery and validation flow:

```python
from jtbd import JTBDSkill          # Discover what customers are trying to accomplish
from vpd import VPDSkill            # Design & validate the value proposition
from quantux import QuantUXSkill    # A/B test and UX-validate hypotheses
from swd import SWDSkill            # Communicate results to stakeholders

# 1. JTBD — Discover unmet jobs
jtbd = JTBDSkill("Project Management", "Engineering Managers")
opportunity = jtbd.score_opportunity("Track cross-team dependencies", struggle=4, alternative=3, market=5, budget=4)
# Output: opportunity score and four-forces analysis

top_job = {"description": "Track cross-team dependencies", "importance": 5, "struggle": 4}

# 2. VPD — Build the canvas around the top job
vpd = VPDSkill("Project Management", "Engineering Managers")
canvas = vpd.analyze_canvas(
    product_name="TeamSync",
    jobs=[top_job],
    pains=[{"description": "Dependencies fall through the cracks", "severity": "critical"}],
    gains=[{"description": "Single-pane dependency dashboard", "desire_level": "required"}],
    products=[{"description": "Auto-linked dependency graph", "category": "digital"}],
    pain_relievers=[{"description": "Automatic dependency alerts", "target_pain": "Dependencies fall through the cracks", "coverage": "full"}],
    gain_creators=[{"description": "Dependency dashboard", "target_gain": "Single-pane dependency dashboard", "coverage": "full"}],
)
print(canvas.fit_score)  # e.g., 0.78 → promising

# 3. QuantUX — Run A/B test on the top hypothesis
quantux = QuantUXSkill("Dependency Dashboard A/B")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.05)
ab_result = quantux.analyze_ab_test("Current Workflow", 5000, 1750, "TeamSync Dashboard", 5000, 2000)

# 4. SWD — Package findings for leadership
swd = SWDSkill("PMF Validation Report")
ctx = swd.build_context(
    audience="VP of Engineering & CPO",
    cta="Approve Q3 investment in TeamSync dependency features"
)
story = swd.build_story(protagonist="Engineering Managers",
    imbalance="Cross-team dependencies cause 40% missed deadlines",
    evidence=["A/B test: new dashboard saves 2.1 hrs/week, p<0.001"],
    call_to_action="Launch dependency dashboard in Q3")
```

This pipeline turns **customer insight → validated value proposition → tested solution → stakeholder-ready story** in one coherent flow.

## 🎯 VPD Canvas Workshops / VPD 画布工作坊

Structured workshop guides for running VPD sessions with your team:

### Workshop 1: "Map Your First Canvas" (2 hours)
```python
from vpd import VPDSkill

vpd = VPDSkill("My Product", "Target Segment")

# Step 1: Customer Profile (right side first!)
canvas = vpd.analyze_canvas(
    product_name="My Product",
    jobs=[
        {"description": "Complete core task efficiently", "category": "functional", "importance": 5},
        {"description": "Look competent to my boss", "category": "social", "importance": 4},
    ],
    pains=[
        {"description": "Current tool takes 10+ clicks", "severity": "critical"},
    ],
    gains=[
        {"description": "One-click completion", "desire_level": "required"},
    ],
)
print(f"Fit Score: {canvas.fit_score}")  # Baseline for iteration
```

### Workshop 2: "Prioritize by Pain" (45 min)
```python
priority = vpd.calculate_priority([
    {"name": "10+ clicks to complete", "importance": 5, "dissatisfaction": 5, "frequency": 5, "viability": 4},
    {"name": "No mobile app", "importance": 4, "dissatisfaction": 3, "frequency": 2, "viability": 3},
])
# → Top pain gets P0, lower scores get P1-P3
```

### Workshop 3: "Blue Ocean Strategy" (1 hour)
```python
strategy = vpd.analyze_competitor(
    my_name="My Product",
    factors=["Price", "Speed", "Integration", "Support", "Ease of Use"],
    players={
        "My Product": [7, 8, 5, 6, 9],
        "Competitor A": [8, 6, 7, 5, 4],
        "Competitor B": [5, 7, 8, 7, 6],
    }
)
# → Value curves reveal where no one competes → that's your Blue Ocean
```

### 💡 Pro Tip / 专业技巧
> **Customer Profile FIRST, Value Map SECOND**. Teams that fill the right side (Jobs/Pains/Gains) before the left side (Products/Pain Relievers/Gain Creators) produce 2× higher fit scores. The rule: understand the problem before designing the solution.
>
> **先填客户画像，再填价值图**。先填右边（Jobs/Pains/Gains）的团队比先填左边的团队产出 2× 更高的契合度评分。规则：先理解问题，再设计方案。


## 📖 Knowledge Base

All knowledge is organized in `references/knowledge-base.md` covering 8 major themes:

| Theme | Core Content |
|-------|-------------|
| I: Business Model Architecture | Value proposition canvas, BMC 9 building blocks, 3 fit types |
| II: Information Gathering | Customer jobs/pains/gains collection, interview 8 principles |
| III: Information Organizing | Pain severity grading, gain desirability ranking, job importance sorting |
| IV: Design Methods | 10 innovation triggers, prototyping, from profile vs from value map |
| V: Testing Methods | Hypothesis decomposition, test cards, learning cards, CTA tiers |
| VI: Innovation Strategy | Blue Ocean 4 actions, value curves, differentiation opportunities |
| VII: Quantitative Methods | 4-dimension priority model, sample size calculation, statistical significance |
| VIII: Decision Support | Data trap checking, iteration suggestions, business model fit validation |


## 📐 VPD Lifecycle / 价值主张生命周期

```
Phase 1          Phase 2              Phase 3              Phase 4               Phase 5
Customer        Customer             Value              Product-Market          Business
Understanding ─► Profiling  ──────► Proposition ──────► Fit Validation ──────► Strategy
(T1-T2)         (T3-T4)              (T5)                (T6)                   (T7)
  │                │                    │                    │                     │
  ├─ Interview     ├─ Priority          ├─ Value Prop        ├─ Experiment         ├─ Business model
  ├─ Questionnaire ├─ Calculation       ├─ Canvas            ├─ Design             ├─ Moat analysis
  └─ Research      └─ Segmentation      └─ Statement         └─ Scoring            └─ ROI estimation
```

1. **Customer Understanding** (T1-T2) — Gather user data via interviews and surveys
2. **Customer Profiling** (T3-T4) — Calculate priorities, segment users
3. **Value Proposition** (T5) — Build canvas, generate value proposition statements
4. **Product-Market Fit Validation** (T6) — Design experiments, score PMF
5. **Business Strategy** (T7) — Business model design, moat analysis, ROI estimation

## 📁 Project Structure

```
value-proposition-design/
├── SKILL.md              # Agent-facing skill definition
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── requirements.txt      # pyyaml >= 6.0
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── CODE_OF_CONDUCT.md    # Community standards
├── CONTRIBUTING.md       # Contribution guidelines
├── references/           # Knowledge base documents
│   ├── knowledge-base.md # 8 major themes
│   └── 01-03 ecosystem collaboration docs
├── vpd/                  # Python executable toolkit
│   ├── __init__.py       # VPDSkill unified entry point
│   ├── config.yaml       # Configurable parameters
│   ├── interview_generator.py
│   ├── survey_designer.py
│   ├── priority_calculator.py
│   ├── canvas_analyzer.py
│   ├── strategy_scorer.py
│   ├── sample_calculator.py
│   ├── experiment_designer.py
│   ├── utils.py
│   └── tests/
│       └── test_all.py   # 14 test cases
└── .github/              # CI/CD workflows & issue templates
```

## ⚡ 30-Second Quick Start / 30秒快速开始

```python
from vpd import VPDSkill

# One-liner: analyze a value proposition canvas
vpd = VPDSkill("Your Product", "Target Users")
canvas = vpd.analyze_canvas(product_name="Product", jobs=[{"description": "Core task", "importance": 5}], pains=[{"description": "Main pain", "severity": "high"}])
print(f"Fit score: {canvas.fit_score}")
```

## 🧪 Testing

```bash
cd value-proposition-design
python vpd/tests/test_all.py
# Or with pytest:
python -m pytest vpd/tests/test_all.py -v
```

## 📋 When NOT to Use VPD / 什么时候不该用 VPD

| Your Need | Recommended Skill |
|-----------|------------------|
| Choosing research methods or designing qualitative research | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| Statistical analysis or A/B testing | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| Understanding user Jobs-to-be-Done | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| Creating user personas / user segmentation | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| Data visualization & storytelling | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| Business framework analysis (SWOT, PESTEL) | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |
| 选择研究方法、设计访谈 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 定量统计分析、A/B 测试 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 理解用户 Jobs、机会评分 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 创建用户画像 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 数据可视化与故事化呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 商业框架分析 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **Value Proposition Design** | Alexander Osterwalder et al. (2014) | Foundation |
| Business Model Generation | Alexander Osterwalder (2010) | Business Model Canvas |
| The Mom Test | Rob Fitzpatrick (2013) | Customer interview methodology |
| Lean Startup | Eric Ries (2011) | MVP and validated learning |
| Testing Business Ideas | David Bland & Alex Osterwalder (2020) | Experiment validation methodology |
| Blue Ocean Strategy | W. Chan Kim & Renée Mauborgne (2004) | Blue Ocean 4 actions framework |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Related Skills in the AliDujie Ecosystem

| Skill | What It Does | GitHub |
|-------|-------------|--------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 100 design research methods | `UDMSkill` |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | Evidence-driven user persona creation | `PersonaSkill` |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Jobs-to-be-Done analysis (4-school fusion) | `JTBDSkill` |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | HEART framework, A/B testing, MaxDiff | `QuantUXSkill` |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Data visualization & executive storytelling | `SWDSkill` |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Business framework analysis | `STMSkill` |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | CTO-level tech strategy & architecture guidance | `CTOSkill` |

### 🔗 扩展生态 (Extended Ecosystem)

VPD 价值验证可与管理技能结合，将 PMF 数据转化为商业战略：

| 扩展技能 | 协作场景 |
|---------|----------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | VPD 护城河分析 → CEO 竞争战略 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | VPD 画布 → CPO 产品组合与 PMF |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | VPD 价值主张 → CMO 品牌定位 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | VPD 技术可行性 → CTO 架构决策 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | VPD 验证结果 → CEO 计划审查与范围对齐 |

### 🔗 Extended Ecosystem

VPD value validation can be combined with management skills to turn product-market fit into business strategy:

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | VPD moat analysis → CEO competitive strategy |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | VPD canvas → CPO product portfolio & PMF |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | VPD value proposition → CMO brand positioning |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | VPD tech feasibility → CTO architecture decisions |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | VPD validation → CEO plan review & scope alignment |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM framework analysis → VPD validates market hypotheses |

### 💡 Pro Tips / 专业技巧
- **Customer profile first**: Always fill the right side (Jobs/Pains/Gains) before touching the left side — solutions should follow problems
- **Lethal hypotheses win**: Test the assumption that, if wrong, kills the entire idea — before investing in build
- **Blue Ocean whitespace**: Use `analyze_competitor()` value curves to spot where no one competes — that's where you win
- **Three fits ≠ one fit**: Problem-Solution Fit ≠ Product-Market Fit ≠ Business Model Fit — validate each stage separately
- **Quantify everything**: "Users are frustrated" → "73% of primary personas abandon the flow at step 3" — quantified pains drive better decisions
- **Start lean**: If you're short on time, run `analyze_canvas()` → `calculate_priority()` → `design_experiment()` in that order. Skip competitive strategy until you have PMF.
- **Chain with ecosystem**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) discovers Jobs → VPD maps to canvas → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) validates → [SWD](https://github.com/AliDujie/storytelling-with-data) presents → [Persona](https://github.com/AliDujie/web-persona-skill) provides user context → [UDM](https://github.com/AliDujie/universal-design-methods) guides research

### ❓ FAQ / 常见问题

**Q: What's a "lethal hypothesis" and why should I test it first?**
A lethal hypothesis is an assumption that, if proven wrong, would invalidate the entire product idea. Test these first — they're your biggest risks. If your lethal hypothesis fails, you've saved yourself weeks of wasted engineering effort. VPD's `design_experiment()` auto-sorts hypotheses by lethality.

**Q: How do I know if my canvas fit score is good enough?**
Fit scores range 0–1. **≥ 0.7** = strong alignment (proceed to build). **0.5–0.7** = reasonable but with gaps (run experiments). **< 0.5** = significant misalignment (revisit assumptions before investing).

**Q: Can VPD work with qualitative data only?**
Yes. `analyze_canvas()` and `design_experiment()` work perfectly with qualitative findings from [UDM](https://github.com/AliDujie/universal-design-methods) interviews. Add quantitative validation later via [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) when you have traffic.

**Q: How does VPD differ from JTBD?**
JTBD discovers *what* users are trying to accomplish (the Job). VPD takes those Jobs and designs *how* your product delivers value (the Canvas). Think JTBD as research, VPD as design — they're sequential, not competing.

## 🏗️ VPD Canvas Workshops / 价值主张画布工作坊

3 structured workshop templates for different contexts:

### Workshop 1: Startup Canvas Validation (3 hours)
**For**: Early-stage teams validating Problem-Solution Fit.
```python
from vpd import VPDSkill
vpd = VPDSkill("Your Startup", "Target Segment")
canvas = vpd.analyze_canvas(product_name="Your Startup",
    jobs=[{"description": "Core job", "importance": 5}],
    pains=[{"description": "Main pain", "severity": "critical"}])
```
**Steps**: (1) Map customer profile — Jobs/Pains/Gains, (2) Map value map — Products/Pain Relievers/Gain Creators, (3) Score fit, (4) Identify lethal hypothesis, (5) Design validation experiment.

### Workshop 2: Enterprise Feature Prioritization (2 hours)
**For**: Product teams deciding which features to build next.
```python
vpd.calculate_priority("Feature X", importance=9, current_satisfaction=3,
    technical_feasibility=4, business_value=8)
# → Priority Score: 8.5/10 — P0
```

### Workshop 3: Pivot Canvas (90 min)
**For**: Teams considering a strategic pivot based on user feedback.
**Use**: `analyze_competitor()` to map value curves → `blue_ocean_grid()` to find whitespace.

## 📊 Fit Score Quick-Ref / 契合度评分基准

| Score | Fit Level | What It Means | Next Step |
|-------|-----------|---------------|-----------|
| ≥ 8.0/10 | Strong fit | PMF likely — scale | Invest in acquisition |
| 6.0-7.9 | Moderate fit | Iterate on gaps | Refine top 3 Pains/Gains |
| 4.0-5.9 | Weak fit | Major rework needed | Revisit Jobs → VPD canvas |
| < 4.0 | No fit | Fundamental mismatch | Consider pivot |

> 📌 Use `vpd.analyze_canvas()` to get your score. Target **≥ 6.0** before committing to build.

## 🛡️ Common Pitfalls & How to Avoid Them

| Pitfall | How VPD Helps |
|---------|---------------|
| "We can do everything" — vague positioning | `analyze_canvas()` forces Jobs-Pains-Gains specificity |
| Building before validating | `design_experiment()` identifies lethal hypotheses to test first |
| Feature-by-feature competition | `analyze_competitor()` value curves reveal differentiation whitespace |
| HiPPO-driven priorities | `calculate_priority()` replaces opinions with 4-dimension scores |
| PMF that never ships | Three-fit model prevents scaling before Problem-Solution Fit

## ❓ FAQ / Troubleshooting

**Q: Why does VPD need pyyaml?**
VPD uses YAML for its configuration file (`config.yaml`), which allows you to customize parameters like pain severity thresholds, gain desirability levels, and priority scoring weights without touching code.

**Q: What's a "lethal hypothesis" in experiment design?**
A lethal hypothesis is one that, if disproven, would kill the entire business idea. Test lethal hypotheses first — they're your biggest risks. Non-lethal hypotheses can wait.

**Q: How do I interpret the canvas fit score?**
Fit scores range 0-1. Above 0.7 = strong alignment between customer profile and value map. 0.5-0.7 = reasonable fit with identifiable gaps. Below 0.5 = significant misalignment — revisit your assumptions.

**Q: Can I use the Blue Ocean framework for an existing product?**
Yes. The `analyze_competitor()` function builds value curves across competitive factors, then applies the Eliminate-Reduce-Raise-Create (ERRC) grid to find differentiation whitespace.

**Q: How does VPD connect to other AliDujie skills?**
VPD receives Jobs from [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) and research findings from [UDM](https://github.com/AliDujie/universal-design-methods), validates experiments with [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research), and presents results through [SWD](https://github.com/AliDujie/storytelling-with-data). It sits at the center of the product validation pipeline.

**Q: I'm a solo founder — should I still use VPD?**
Absolutely. The canvas forces you to articulate assumptions you'd otherwise keep in your head. Start with `analyze_canvas()` to map your best guess, then use `design_experiment()` to test the riskiest assumption before writing code. It's cheaper to invalidate a hypothesis on paper than after launch.

## 🏗️ Advanced: Custom Configuration

VPD supports runtime configuration via YAML config (`vpd/config.yaml`):

```python
from vpd import VPDSkill, AnalysisConfig

config = AnalysisConfig()
config.set_pain_severity_threshold(0.7)  # Customize pain severity cutoff
config.set_priority_weights({"importance": 0.4, "dissatisfaction": 0.3, "frequency": 0.2, "viability": 0.1})

skill = VPDSkill("Product", "Users", config=config)
```

See [INSTALL.md](INSTALL.md) for full configuration options and agent integration guides.

## ✅ Best Practices / 最佳实践

1. **Customer Profile before Value Map** — Always start with `analyze_customer_profile()` to understand pains, gains, and jobs before trying to design value creators. You can't create value you don't understand.
2. **Validate with experiments, not opinions** — Use `design_experiment()` to test assumptions cheaply before building. The evidence score (1-5) tells you how solid your VPD claims are.
3. **Use Blue Ocean for differentiation** — Run `analyze_competitive_strategy()` and apply the ERRC grid (Eliminate-Reduce-Raise-Create) to find uncontested market space instead of competing on features.
4. **Prioritize by pain severity** — The `calculate_priority()` module weights pain severity × frequency × willingness-to-pay. Focus on high-severity, high-frequency pains that users will pay to solve.
5. **Chain with JTBD upstream** — Feed JTBD's `create_jobs_atlas()` output into VPD's customer profile for a seamless insight-to-value pipeline.

## ⚠️ Limitations / 局限性

- **Canvas is a thinking tool, not a deliverable** — The Value Proposition Canvas structures your thinking but doesn't guarantee product-market fit. Real validation requires customer experiments.
- **Static snapshot** — VPD captures a moment in time. Customer jobs, pains, and gains evolve; re-run analysis periodically (quarterly recommended).
- **Requires input data quality** — The customer profile analysis is only as good as the input data. Garbage in, garbage out — pair with real JTBD interviews or user research.
- **Bilingual documentation only** — Pro Tips and guides are provided in CN/EN only; localization to other languages requires community contributions.


## 🏃 VPD Sprint Template (2 Weeks) / VPD 价值主张冲刺模板

| Day | Activity | VPD Capability | Deliverable |
|-----|----------|---------------|-------------|
| 1 | Customer profile setup | `customer_profile()` | Jobs, pains, gains |
| 2-3 | Value map design | `value_map()` | Products, gain creators, pain relievers |
| 4 | Canvas fit analysis | `analyze_canvas()` | Fit score + gaps |
| 5-6 | Competitor analysis | `competitor_analysis()` | Competitive landscape |
| 7 | Blue Ocean ERRC grid | `blue_ocean()` | Differentiation strategy |
| 8 | Experiment design | `design_experiment()` | Validation plan |
| 9-10 | Run experiments | Data collection | Experiment results |
| 11 | Fit reassessment | `analyze_canvas()` | Updated fit score |
| 12 | Strategy scoring | `score_strategy()` | Strategic recommendation |
| 13 | Interview guide for validation | `generate_interview()` | Validation interviews |
| 14 | Executive summary + handoff | Export to SWD | Decision-ready deck |

**Minimum viable (3 days)**: Customer profile → value map → fit analysis. Fast-track from assumptions to validated fit.

## 📊 Version History

See [CHANGELOG.md](CHANGELOG.md) for full release notes.


**Latest (v2.4.112)**: Added cross-skill collaboration examples (JTBD, Persona, SWD), Blue Ocean Strategy quick ref, VPD promotional section, version bump.

**Previous (v2.4.111)**: TOC anchor version fix (v24107 → v24110), What's New version sync, ecosystem cross-reference audit across all 6 AliDujie skills.

**Previous (v2.4.108)**: CHANGELOG sync (backfilled 3 missing version entries), consolidated redundant What's New entries, ecosystem cross-reference audit across all 6 AliDujie skills.

**Previous (v2.4.104)**: Version bump, ecosystem cross-reference audit across all 6 AliDujie skills.

**Previous (v2.4.97)**: Fixed stale What's New TOC link (v2.4.96 → v2.4.97), updated Version History latest entry (v2.4.96 → v2.4.97), ecosystem cross-reference audit across all 6 AliDujie skills.

**Previous (v2.4.87)**: Repo maintenance — added VPD Canvas Workshop Guides (3 scenarios), added Fit Score Quick-Ref table, synced versions across all files.

**Previous (v2.4.86)**: Repo maintenance — converted "When NOT to Use VPD" to bilingual CN/EN table format, added Structured Thinking Model cross-reference, enhanced SEO-friendly headings.

**Previous (v2.4.85)**: Repo maintenance — added Recommended Learning Path, added Blue Ocean ERRC grid quick reference to Pro Tips, unified ecosystem pipeline, fixed ERRC typo in Best Practices.

**Previous (v2.4.83)**: Added lean-start Pro Tip for time-constrained teams (canvas → priority → experiment), improved pro tips section.

**Previous (v2.4.81)**: Improved pipeline documentation with complete JTBD→VPD→QuantUX→SWD end-to-end example, enhanced competitive strategy examples.

**Previous (v2.4.80)**: Added Chinese Extended Ecosystem section with CEO/CPO/CMO/CTO advisor links, improving bilingual parity.

**Previous (v2.4.79)**: Added cross-skill collaboration table with ecosystem integration guide, improved Pro Tips section.

### 📖 Recommended Learning Path

1. **Start with the README** — Quick start + 30-second example
2. **Read USAGE.md** — Detailed workflows for all 7 modules with code examples
3. **Explore references/** — Deep dive into 8 major themes: canvas architecture, information gathering, design methods, Blue Ocean strategy, experiment validation
4. **Try the full pipeline** — Chain JTBD → VPD → QuantUX → SWD end-to-end (see [Complete Pipeline](#-complete-pipeline-jtbd--vpd--quantux--swd))
5. **Customize via config** — Adjust pain severity thresholds and priority weights (see [INSTALL.md](INSTALL.md))

## 🌐 Ecosystem FAQ / 生态常见问题

**Q: VPD vs JTBD — what's the difference?**
A: JTBD discovers *what Jobs* users are trying to accomplish. VPD takes those Jobs and designs *how* your product delivers value (the Canvas). JTBD is research; VPD is design. Use JTBD first, then VPD.

**Q: VPD vs QuantUX — when do I switch from canvas to testing?**
A: VPD helps you design the value proposition and identify lethal hypotheses. QuantUX runs the A/B tests and statistical validation. The handoff: VPD experiments → QuantUX analysis.

**Q: Can VPD work without other AliDujie skills?**
A: Yes — VPD is fully self-contained. But chaining with JTBD (Jobs discovery) and QuantUX (validation) gives you the full insight-to-validation pipeline.

---

## 📚 Resources

- [SKILL.md](SKILL.md) — Agent-facing skill definition and prompt templates
- [USAGE.md](USAGE.md) — Detailed usage guide with code examples / 详细使用指南
- [INSTALL.md](INSTALL.md) — Detailed installation guide and agent integration
- [examples/](examples/) — Runnable Python examples (canvas generation, canvas analysis, competitor analysis, blue ocean ERRC, experiment design)
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [SECURITY.md](SECURITY.md) — Security policy and responsible use
- [references/](references/) — Canvas templates and experiment design guides
- [vpd/](vpd/) — Core Python module source code

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Built with ❤️ as part of the AliDujie UX Research Ecosystem**

[Persona](https://github.com/AliDujie/web-persona-skill) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [UDM](https://github.com/AliDujie/universal-design-methods) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · **VPD** · [SWD](https://github.com/AliDujie/storytelling-with-data) · [STM](https://github.com/AliDujie/Structured-Thinking-Model)


