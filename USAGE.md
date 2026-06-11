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
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Strategic framework | VPD business analysis → STM strategic framework → STM decision support |

> 💡 **Recommended chain:** JTBD (discover Jobs) → UDM (research) → **VPD** (map canvas + validate) → QuantUX (confirm) → SWD (present) → STM (strategic decision)

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

## ⛔ When NOT to Use VPD / 何时不使用

VPD is the product-market validation layer — map Jobs to value, test hypotheses, and analyze competition. Use other AliDujie skills when:

| Need | Use Instead | Why |
|------|-------------|-----|
| Create user personas, user segmentation | [Web Persona](https://github.com/AliDujie/web-persona-skill) | Evidence-driven persona creation |
| Choose research methods, run interviews | [UDM](https://github.com/AliDujie/universal-design-methods) | 100 methods, interview guides, usability tests |
| Understand user Jobs, opportunity scoring | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD interviews feed VPD canvas |
| Quantitative A/B testing, HEART metrics | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) | Statistical validation of VPD hypotheses |
| Data visualization, executive stories | [SWD](https://github.com/AliDujie/storytelling-with-data) | VPD canvas → SWD executive narrative |

> 💡 **Better together**: JTBD discovers Jobs → VPD maps to canvas → QuantUX validates → SWD presents → STM structures strategic decisions.

## 📎 Related Documents

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Full documentation, API reference, ecosystem diagram |
| [SKILL.md](SKILL.md) | Agent-facing skill definition and trigger rules |
| [INSTALL.md](INSTALL.md) | Installation guide with troubleshooting |
| [CHANGELOG.md](CHANGELOG.md) | Version history and what's new |
| [references/knowledge-base.md](references/knowledge-base.md) | Full methodology reference (8 chapters) |
| [references/04-ecosystem-collaboration.md](references/04-ecosystem-collaboration.md) | Cross-skill workflows for all 6 ecosystem skills |

### C-Suite Skills for Commercialization / 管理层技能

After VPD validates product-market fit, extend into commercial strategy:

| Skill | Use when... |
|-------|-------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Need competitive strategy, moat building |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | Need product portfolio, PMF assessment |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | Need brand positioning, messaging |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | Need technical feasibility, architecture decisions |

## 💡 Best Practices / 最佳实践

1. **Customer Profile before Value Map — always**
   Fill the right side (Jobs/Pains/Gains) before touching the left side (Products/Pain Relievers/Gain Creators). Solutions should follow problems, not precede them.
   *先填客户画像再填价值图。先理解问题再设计方案，永远不要反过来。*

2. **Test lethal hypotheses first — fail fast, learn faster**
   Use `design_experiment()` with `lethality="lethal"` to identify the assumption that, if wrong, kills the entire product idea. Test it before writing any code.
   *先测"致命假设"——如果这个假设是错的，整个产品就不可行。在写代码之前先验证。*

3. **Blue Ocean whitespace beats feature parity**
   Use `analyze_competitor()` value curves + ERRC grid (Eliminate-Reduce-Raise-Create) to find where no one competes — that's your Blue Ocean, not another feature checkbox.
   *用价值曲线+ERRC 网格找蓝海空间，而不是功能清单上的另一个勾。*

4. **Three fits ≠ one fit — validate each stage**
   Problem-Solution Fit ≠ Product-Market Fit ≠ Business Model Fit. Don't skip stages. A canvas that looks great on paper (PSF) still needs market validation (PMF) and revenue proof (BMF).
   *三种契合度不是一回事——纸上契合≠市场契合≠商业模式契合，逐级验证。*

5. **Quantify everything — "frustrated" → "73% abandon at step 3"**
   Vague pains drive vague solutions. "Users are frustrated" becomes actionable when you add: "73% of primary personas abandon the flow at step 3, losing ¥200/order."
   *量化一切——「用户沮丧」变成「73% 的首要角色在第 3 步流失，每单损失 200 元」才是可行动的洞察。*

6. **Chain JTBD → VPD → QuantUX for full validation**
   JTBD discovers high-opportunity Jobs → VPD maps them to canvas → QuantUX validates with A/B tests. Each skill's output is the next skill's input.
   *JTBD 发现 Jobs → VPD 映射画布 → QuantUX A/B 验证——每个技能的产出都是下一个的输入。*

## 🔗 Extended Ecosystem / 扩展生态

VPD value validation can be combined with management skills to turn product-market fit into business strategy:

| Extended Skill | Collaboration Scenario |
|---------------|------------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | VPD moat analysis → CEO competitive strategy / VPD 护城河分析 → CEO 竞争战略 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | VPD canvas → CPO product portfolio & PMF / VPD 画布 → CPO 产品组合 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | VPD value proposition → CMO brand positioning / VPD 价值主张 → CMO 品牌定位 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | VPD tech feasibility → CTO architecture decisions / VPD 技术可行性 → CTO 架构决策 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | VPD validation → CEO plan review & scope alignment / VPD 验证 → CEO 计划审查 |

## ❓ FAQ / Troubleshooting

**Q: My canvas fit score is low — what should I do first?**
Look at which dimension scores lowest (Jobs-Pains alignment, Gains coverage, or Differentiation). Fix the weakest link first — usually it's that you've defined too many Pains or not enough concrete Gains.
*契合度评分低时，先看哪个维度得分最低。通常问题在于痛点定义过多或收益不够具体。先修最弱的一环。*

**Q: How do I know if my value proposition is differentiated enough?**
Use `analyze_competitive_strategy()` to generate a value curve. If your curve overlaps heavily with competitors on every dimension, you're competing on features, not value. Apply the ERR grid (Eliminate-Reduce-Raise-Create) to find whitespace.
*用 `analyze_competitive_strategy()` 生成价值曲线。如果你的曲线在每个维度上都和竞品重叠，说明你在功能层面竞争而非价值层面。用 ERR 网格找差异化空间。*

**Q: Can I use VPD without doing JTBD first?**
You can, but you'll miss the deep "why" behind user needs. JTBD provides the Jobs that populate the canvas. Without it, you risk mapping surface-level features instead of real Jobs.
*可以不用 JTBD 就开始，但会错过用户行为背后的深层"为什么"。JTBD 提供的 Job 是画布的核心输入。*

**Q: How many experiments should I run to validate PMF?**
Start with one lethal hypothesis test — the assumption that, if wrong, would kill your product idea. Use `design_experiment()` to structure it. One well-designed test is worth ten vague surveys.
*从一个"致命假设"测试开始——如果这个假设是错的，产品就不可行。用 `design_experiment()` 结构化设计。一个好实验胜过十个模糊问卷。*

**Q: How does VPD chain with other skills?**
JTBD provides Jobs → VPD maps to canvas → QuantUX experiments validate → SWD presents results. See the ecosystem pipeline in README.md.
*JTBD 提供 Job→VPD 映射到画布→QuantUX 实验验证→SWD 呈现结果。*
