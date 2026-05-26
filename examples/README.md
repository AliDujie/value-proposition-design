# Value Proposition Design — Runnable Examples

Zero-dependency Python examples demonstrating VPD capabilities. Each script is standalone.

## Quick Start

```bash
PYTHONPATH=. python examples/01_canvas_analysis.py
PYTHONPATH=. python examples/02_blue_ocean.py
PYTHONPATH=. python examples/03_experiment_design.py
```

## Examples

| Script | What It Shows |
|--------|--------------|
| `01_canvas_analysis.py` | Value Proposition Canvas analysis with Jobs-Pains-Gains mapping |
| `02_blue_ocean.py` | Blue Ocean Strategy analysis with ERRC grid and value curve |
| `03_experiment_design.py` | Experiment design for PMF validation with hypothesis testing |

## Try Before You Decide

```bash
PYTHONPATH=. python -c "
from vpd import VPDSkill
skill = VPDSkill('My Product')
result = skill.analyze_canvas(jobs=['Quick onboarding'], pains=['Complex setup'], gains=['Time savings'])
print(result)
"
```
