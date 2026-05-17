# Value Proposition Design (VPD) Skill — Usage Guide

> 价值主张设计 · 使用指南

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
