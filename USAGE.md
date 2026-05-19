# Value Proposition Design (VPD) Skill — Usage Guide

> 价值主张设计 · 使用指南

## 📐 Where VPD Fits in the Pipeline

```
Persona (Who) → JTBD (What) → UDM (Research) → QuantUX (Validate) → VPD (Value) → SWD (Present)
                                                                        ↑
                                                                  VPD sits here
```

- **After** JTBD discovers Jobs and UDM validates user needs
- **Before** QuantUX experiments confirm fit and SWD presents results
- **VPD** maps discovered needs to the Value Proposition Canvas (Jobs-Pains-Gains)

## ⚡ 5-Minute Quick Start / 5分钟快速开始

```bash
cp -r value-proposition-design /your/agent/skills/
pip install pyyaml  # Only dependency
```

```python
from vpd import VPDSkill
skill = VPDSkill("SaaS Product", "Team Leads")
canvas = skill.analyze_canvas(product_name="TeamFlow",
    jobs=[{"description": "Team task assignment", "importance": 5}],
    pains=[{"description": "Poor collaboration", "severity": "critical"}],
    gains=[{"description": "Real-time visibility", "desire_level": "required"}],
    products=[{"description": "Smart dashboard", "category": "digital"}])
print(canvas.fit_score)
```

## 🔑 Core Workflows / 核心工作流

### 1. Value Proposition Canvas / 价值主张画布

```python
from vpd import VPDSkill

skill = VPDSkill("E-commerce Platform", "Shoppers")

canvas = skill.analyze_canvas(
    product_name="ShopEasy",
    jobs=[
        {"description": "Find products quickly", "category": "functional", "importance": 5},
        {"description": "Feel confident in purchase", "category": "emotional", "importance": 4},
    ],
    pains=[
        {"description": "Too many options cause decision fatigue", "severity": "critical"},
        {"description": "Shipping cost surprise at checkout", "severity": "high"},
    ],
    gains=[
        {"description": "Personalized recommendations", "desire_level": "desired"},
        {"description": "Free shipping threshold", "desire_level": "required"},
    ],
    products=[{"description": "Smart search + filters", "category": "digital"}],
    pain_relievers=[{"description": "Curated collections", "target_pain": "Too many options cause decision fatigue", "coverage": "full"}],
    gain_creators=[{"description": "AI recommendations", "target_gain": "Personalized recommendations", "coverage": "partial"}],
)
print(canvas)
# → Fit score, gap analysis, recommendations
```

### 2. Priority Calculation / 优先级计算

```python
priority = skill.calculate_priority([
    {"name": "Decision fatigue", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
    {"name": "Shipping cost surprise", "importance": 4, "dissatisfaction": 4, "frequency": 3, "viability": 3},
])
# → P0-P3 grading with 4-dimension scoring
```

### 3. Competitive Strategy (Blue Ocean) / 竞争战略（蓝海）

```python
strategy = skill.analyze_competitor(
    my_name="ShopEasy",
    factors=["Price", "Selection", "Speed", "UX", "Support"],
    players={
        "ShopEasy": [7, 8, 6, 9, 7],
        "Competitor A": [8, 9, 5, 6, 8],
        "Competitor B": [6, 7, 8, 7, 5],
    }
)
# → Value curves + ERRC grid (Eliminate-Reduce-Raise-Create)
```

### 4. Experiment Design / 实验设计

```python
experiment = skill.design_experiment(
    hypotheses=[
        {"description": "Users will pay for premium recommendations", "lethality": "lethal"},
        {"description": "Main pain point is decision fatigue", "lethality": "important"},
    ]
)
# → Test cards, learning cards, CTA tiers
```

### 5. CEO Extensions / CEO 视角

```python
# Full canvas + commercialization + moat + ROI
report = skill.generate_canvas(include_ceo_analysis=True)
```

## 📋 Common Scenarios / 常见场景

| Scenario | Flow | APIs |
|----------|------|------|
| SaaS PMF validation | Canvas → Experiment → CEO report | `analyze_canvas()` → `design_experiment()` → `generate_canvas(include_ceo_analysis=True)` |
| Competitive differentiation | Competitor analysis → Blue Ocean | `analyze_competitor()` → ERRC grid |
| Feature prioritization | Priority calc → Canvas | `calculate_priority()` → `analyze_canvas()` |
| New market entry | Interview → Survey → Canvas | `generate_interview()` → `design_survey()` → `analyze_canvas()` |

## 🔗 Ecosystem Integration / 生态协作

```python
# JTBD (discover Jobs) → VPD (map to canvas) → QuantUX (validate) → SWD (present)
from jtbd import JTBDSkill
from vpd import VPDSkill
from quantux import QuantUXSkill
from swd import SWDSkill

jtbd = JTBDSkill("Project Management")
score = jtbd.score_opportunity("Track cross-team dependencies", struggle=4, alternative=3, market=5, budget=4)

vpd = VPDSkill("Project Management", "Engineering Managers")
canvas = vpd.analyze_canvas(product_name="TeamSync",
    jobs=[{"description": "Track dependencies", "importance": 5}],
    pains=[{"description": "Dependencies fall through cracks", "severity": "critical"}])

quantux = QuantUXSkill("Project Management")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.05)

swd = SWDSkill("PMF Report")
story = swd.build_story(protagonist="VP of Engineering",
    imbalance="40% missed deadlines from dependency issues",
    call_to_action="Launch dependency dashboard in Q3")
```

## 🧪 Testing / 测试

```bash
cd value-proposition-design
python vpd/tests/test_all.py
```

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history

---

## 🔑 Key Concepts Refresher / 关键概念速查

### Three Fit Types / 三种契合度

- **Problem-Solution Fit (on paper / 纸上契合)** — Your value map addresses the customer's Jobs, Pains, and Gains as stated. It looks good on the canvas but hasn't been tested with real users yet.
  *你的价值主张在画布上匹配了客户的 Jobs/Pains/Gains，但尚未用真实用户验证。*

- **Product-Market Fit (in the market / 市场中契合)** — Real users demonstrate willingness to adopt/pay for your solution through behavioral evidence (usage, retention, revenue). The hypothesis survives market contact.
  *真实用户通过行为证据（使用、留存、付费）证明愿意采纳你的方案——假设经受了市场检验。*

- **Business Model Fit (in the bank / 商业模型契合)** — Your value proposition generates sustainable, scalable revenue that exceeds costs. You have a profitable business model, not just happy users.
  *你的价值主张产生了可持续、可扩展且超过成本的收入——不仅用户满意，而且商业模式盈利。*

### ERRC Grid (Blue Ocean 4 Actions) / 蓝海四步动作框架

| Action | Meaning / 含义 | Question / 问题 |
|--------|---------------|-----------------|
| **Eliminate / 剔除** | Remove factors the industry competes on but customers don't value | 行业中哪些竞争要素客户其实不在乎？ |
| **Reduce / 减少** | Dial down factors that are over-served relative to customer needs | 哪些要素被过度服务了？ |
| **Raise / 提升** | Increase factors above industry standard where customers care most | 哪些要素应该远超行业标准？ |
| **Create / 创造** | Introduce entirely new factors the industry has never offered | 哪些要素是行业从未提供过的？ |

> The ERRC grid pushes you to **simultaneously pursue differentiation and low cost** — breaking the value-cost tradeoff. Use `analyze_competitor()` to generate your ERRC grid automatically.
> ERRC 网格推动你**同时追求差异化和低成本**——打破价值-成本权衡。使用 `analyze_competitor()` 自动生成你的 ERRC 网格。

## 🔗 Related Skills in the Ecosystem / 生态系统中的相关技能

VPD is the **product-market validation layer** — the bridge between research and experimentation:

| Skill | Role | How It Connects with VPD |
|-------|------|--------------------------|
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Demand insight | JTBD Jobs → VPD canvas filling → VPD priority ranking |
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Methodology core | UDM user research → VPD canvas data → experiment design |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Quantitative validation | VPD hypotheses → QuantUX A/B tests validate product-market fit |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | User definition | Persona goals/pains → VPD customer profile → persona validation |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Data storytelling | VPD canvas analysis → SWD chart selection → executive narrative |

> 💡 **Recommended chain:** JTBD (discover Jobs) → UDM (research) → **VPD** (map canvas + validate) → QuantUX (confirm) → SWD (present)

### Quick Cross-Skill Example / 跨技能示例

```python
from jtbd import JTBDSkill
from vpd import VPDSkill
from quantux import QuantUXSkill
from swd import SWDSkill

# JTBD discovers Jobs and opportunity scores
jtbd = JTBDSkill("Project Management")
score = jtbd.score_opportunity("Track dependencies", struggle=4, alternative=3, market=5, budget=4)

# VPD maps Jobs to Value Proposition Canvas
vpd = VPDSkill("Project Management", "Engineering Managers")
canvas = vpd.analyze_canvas(product_name="TeamSync",
    jobs=[{"description": "Track cross-team dependencies", "importance": 5}],
    pains=[{"description": "Dependencies fall through cracks", "severity": "critical"}])
print(f"Fit score: {canvas.fit_score}")

# QuantUX validates the hypothesis with A/B testing
quantux = QuantUXSkill("Project Management")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.05)

# SWD presents the fit analysis to leadership
swd = SWDSkill("PMF Review")
story = swd.build_story(protagonist="VP of Engineering",
    imbalance="40% missed deadlines from dependency issues",
    call_to_action="Launch dependency dashboard in Q3")
```
