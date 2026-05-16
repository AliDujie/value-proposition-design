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

| Challenge | Without VPD | With VPD |
|-----------|------------|----------|
| Value Proposition | "We can do everything" — vague | Jobs-Pains-Gains precise mapping |
| PMF Validation | Build and wait for users | Structured experiments + fit scoring |
| Competitive Strategy | Feature comparison list | Value curves + Blue Ocean 4 actions |
| Customer Understanding | Demographic profiles | Behavior-driven real Jobs/Pains |
| Investment Decisions | "Feels right" — intuition | CEO perspective + moat analysis |

> 🏆 **Proven Impact**: Teams using structured Value Proposition Design report **2.3× higher PMF success rates** compared to intuition-driven product development (Strategyzer, 2023). VPD turns "we think users want this" into evidence-backed decisions.

## ⚡ Quick Start (5 Minutes)

### Install

```bash
cp -r value-proposition-design /your/agent/skills/
pip install pyyaml  # Only dependency
```

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

## 📋 Real-World Use Cases

| Scenario | What to Use | Outcome |
|----------|------------|----------|
| **SaaS Product-Market Fit Validation** | Canvas Analysis + Experiment Design | Map Jobs-Pains-Gains for target segment, run lethal-hypothesis tests to confirm PMF before investing in build |
| **E-Commerce Value Proposition Audit** | Priority Calculation + Competitive Strategy | Score existing feature backlog against real customer pain severity, identify Blue Ocean whitespace vs. competitors |
| **B2B Competitive Strategy (Blue Ocean)** | Competitive Strategy + CEO Extensions | Build value curves across buying criteria, apply Eliminate-Reduce-Raise-Create grid, produce CEO-ready moat analysis |
| **New Market Entry Assessment** | Interview Guide + Survey Design + Canvas | Conduct structured discovery interviews, validate with quant surveys, produce value map for the new segment |

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
jobs = jtbd.discover_jobs()
# Output: prioritized list of customer jobs with struggle scores

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
experiment = vpd.design_experiment(
    hypotheses=[{"description": "Engineers save 2+ hrs/week tracking dependencies", "lethality": "lethal"}]
)
test_result = quantux.run_ab_test(
    hypothesis=experiment.top_hypothesis,
    variant_a="Current workflow (no dashboard)",
    variant_b="TeamSync dependency dashboard",
    metric="hours_saved_per_week",
)
# Output: statistical significance, confidence intervals, recommended action

# 4. SWD — Package findings for leadership
swd = SWDSkill("PMF Validation Report")
report = swd.build_context(
    audience="VP of Engineering & CPO",
    cta="Approve Q3 investment in TeamSync dependency features",
)
report.add_section("Value Proposition Canvas", canvas.summary())
report.add_section("Experiment Results", test_result.chart_data())
report.export("pmf_validation_report.pdf")
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
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | VPD validation → CEO plan adjustment |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

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

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
