# Value Proposition Design (VPD) Skill

> **Build Products People Actually Want. Validate Before You Build.**

![Version](https://img.shields.io/badge/version-2.4.79-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Dependencies](https://img.shields.io/badge/Dependencies-pyyaml-lightgrey)

Based on *Value Proposition Design* by Alexander Osterwalder et al. (2014). A complete methodology skill covering customer insights, canvas analysis, priority calculation, competitive strategy, survey design, and experiment validation — with **7 executable modules** that produce structured deliverables for real business scenarios, plus CEO-level commercialization path and competitive moat analysis.

## 🌟 Why VPD?

| Challenge | Without VPD | With VPD |
|-----------|------------|----------|
| Value Proposition | "We can do everything" — vague | Jobs-Pains-Gains precise mapping |
| PMF Validation | Build and wait for users | Structured experiments + fit scoring |
| Competitive Strategy | Feature comparison list | Value curves + Blue Ocean 4 actions |
| Customer Understanding | Demographic profiles | Behavior-driven real Jobs/Pains |
| Investment Decisions | "Feels right" — intuition | CEO perspective + moat analysis |

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

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
