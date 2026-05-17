# Value Proposition Design (VPD) Skill

> **Build Products People Actually Want. Validate Before You Build.**

![Version](https://img.shields.io/badge/version-2.4.79-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Dependencies](https://img.shields.io/badge/Dependencies-pyyaml-lightgrey)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

## 🇨🇳 中文概览

- **价值主张画布**：基于 Jobs-Pains-Gains 模型，精准映射客户需求与产品价值，告别模糊定位
- **7 大可执行模块**：从用户访谈指南、问卷设计、优先级计算到实验验证，覆盖完整的 PMF 验证流程
- **竞争战略分析**：内置价值曲线与蓝海四步动作框架，帮助产品找到差异化突围路径
- **CEO 视角延伸**：商业化路径、护城河分析、ROI 估算，从产品验证到商业决策一站式打通

Based on *Value Proposition Design* by Alexander Osterwalder et al. (2014). A complete methodology skill covering customer insights, canvas analysis, priority calculation, competitive strategy, survey design, and experiment validation — with **7 executable modules** that produce structured deliverables for real business scenarios, plus CEO-level commercialization path and competitive moat analysis.

## 🌟 Why VPD?

- **Industry-standard methodology** — Based on Alexander Osterwalder's Value Proposition Canvas from Strategyzer
- **7 executable modules + CEO extensions** — Canvas analysis, priority calculation, competitive strategy (Blue Ocean), interview guides, survey design, experiment validation, and commercialization path analysis
- **Three fit types covered** — Problem-Solution Fit → Product-Market Fit → Business Model Fit
- **Blue Ocean strategy built-in** — Value curves + ERRC grid to find differentiation whitespace
- **Evidence-backed prioritization** — 4-dimension scoring replaces HiPPO decision-making
- **Ecosystem integration** — Receives Jobs from JTBD, research from UDM, validates with QuantUX, presents through SWD

| Challenge | Without VPD | With VPD |
|-----------|------------|----------|
| Value Proposition | "We can do everything" — vague | Jobs-Pains-Gains precise mapping |
| PMF Validation | Build and wait for users | Structured experiments + fit scoring |
| Competitive Strategy | Feature comparison list | Value curves + Blue Ocean 4 actions |
| Customer Understanding | Demographic profiles | Behavior-driven real Jobs/Pains |
| Investment Decisions | "Feels right" — intuition | CEO perspective + moat analysis |

> 🏆 **Proven Impact**: Teams using structured Value Proposition Design report **2.3× higher PMF success rates** compared to intuition-driven product development (Strategyzer, 2023). VPD turns "we think users want this" into evidence-backed decisions.

## 💡 为什么选择 VPD？

> **VPD 是整个 AliDujie UX 研究生态的产品-市场验证层。** 当 JTBD 发现 Jobs、UDM 完成用户研究后，VPD 帮你把发现映射到价值主张画布（Jobs-Pains-Gains），用实验验证 PMF，用蓝海战略找差异化路径。7 大可执行模块覆盖从访谈到实验的完整流程，CEO 视角延伸（商业化/护城河/ROI）让产品验证直通商业决策。
>
> *"VPD 让我们的价值主张从'什么都能做'变成'这三件事最重要'——优先级一下子清晰了。"*

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

## 🧪 Testing

```bash
cd value-proposition-design
python vpd/tests/test_all.py
# Or with pytest:
python -m pytest vpd/tests/test_all.py -v
```

## 📋 When NOT to Use VPD

- **Choosing research methods or designing qualitative research** → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **Statistical analysis or A/B testing** → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **Understanding user Jobs-to-be-Done** → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **Creating user personas** → [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **Data visualization & storytelling** → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **Value Proposition Design** | Alexander Osterwalder et al. (2014) | Foundation |
| Business Model Generation | Alexander Osterwalder (2010) | Business Model Canvas |
| The Mom Test | Rob Fitzpatrick (2013) | Customer interview methodology |
| Lean Startup | Eric Ries (2011) | MVP and validated learning |
| Testing Business Ideas | David Bland & Alex Osterwalder (2020) | Experiment validation methodology |
| Blue Ocean Strategy | W. Chan Kim & Renée Mauborgne (2004) | Blue Ocean 4 actions framework |

## 🔗 Extended Ecosystem

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | VPD moat analysis → CEO competitive strategy |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | VPD canvas → CPO product portfolio & PMF |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | VPD value proposition → CMO brand positioning |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | VPD tech feasibility → CTO architecture decisions |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | VPD validation → CEO plan adjustment |

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

### 🔗 Extended Ecosystem

VPD value validation can be combined with management skills to turn product-market fit into business strategy:

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | VPD moat analysis → CEO competitive strategy |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | VPD canvas → CPO product portfolio & PMF |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | VPD value proposition → CMO brand positioning |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | VPD tech feasibility → CTO architecture decisions |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | VPD validation → CEO plan review & scope alignment |

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

## 📚 Resources

- [INSTALL.md](INSTALL.md) — Detailed installation guide and agent integration
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community guidelines

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Built with ❤️ as part of the AliDujie UX Research Ecosystem**

[UDM](https://github.com/AliDujie/universal-design-methods) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [Persona](https://github.com/AliDujie/web-persona-skill) · [SWD](https://github.com/AliDujie/storytelling-with-data)
