# VPD Runnable Examples / 可运行示例

These examples demonstrate Value Proposition Design capabilities with real-world scenarios.
这些示例用真实场景演示价值主张设计能力。

## Quick Start / 快速开始

```bash
cd examples/
python 01_canvas_analysis.py
python 02_competitor_analysis.py
python 03_blue_ocean.py
python 04_experiment_design.py
python 05_canvas_generation.py
```

All examples use **zero dependencies** — pure Python standard library only.
所有示例使用**零依赖** — 仅 Python 标准库。

## Available Examples / 可用示例

### Expected Output Preview / 输出预览

```
>>> Value Proposition Canvas: FreshMart (Efficient Users)
>>>
>>>  Customer Jobs: "Quickly order groceries and get them delivered"
>>>  Pains: "Takes too many clicks to find items", "Delivery times are unreliable"
>>>  Gains: "Same-day delivery", "Personalized recommendations"
>>>  Fit Score: 6.8/10 — Moderate fit. Consider addressing top 2 pains.
```

### 01_canvas_analysis.py
Analyze a complete Value Proposition Canvas with all 7 components and fit scoring.
分析包含全部 7 个组件的完整价值主张画布并评估契合度。

**Use when / 适用场景**: Deep-diving into problem-solution fit with structured canvas analysis.

```bash
python 01_canvas_analysis.py
```

### 02_competitor_analysis.py
Competitive positioning analysis across key factors.
跨关键因素的竞争定位分析。

**Use when / 适用场景**: Understanding your value proposition vs. competitors.

```bash
python 02_competitor_analysis.py
```

### 03_blue_ocean.py
Competitive analysis with Blue Ocean ERRC Grid (Eliminate-Reduce-Raise-Create).
使用蓝海 ERRC 网格（消除-减少-提升-创造）进行竞争分析。

**Use when / 适用场景**: Finding whitespace in a crowded market.

```bash
python 03_blue_ocean.py
```

### 04_experiment_design.py
Design and evaluate value proposition experiments.
设计和评估价值主张实验。

**Use when / 适用场景**: Testing hypotheses about your value proposition before scaling.

```bash
python 04_experiment_design.py
```

### 05_canvas_generation.py
Generate a complete Value Proposition Canvas with fit analysis.
生成完整的价值主张画布并分析契合度。

**Use when / 适用场景**: Designing or evaluating a product-market fit proposition.

```bash
python 05_canvas_generation.py
```

## Tips / 提示

- All examples use relative imports — just run from the `examples/` directory
- No `pip install` required — VPD is zero-dependency
- Feed JTBD insights into VPD canvas jobs/pains/gains for alignment
- See [USAGE.md](../USAGE.md) for detailed API documentation

## 🔗 Ecosystem Integration / 生态集成

VPD is the "value" layer of the AliDujie UX Research Ecosystem. Chain it with other skills:

- **Persona → VPD**: [Persona](https://github.com/AliDujie/web-persona-skill) user profiles → VPD canvas filling
- **JTBD → VPD**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) customer jobs → VPD pains/gains mapping
- **UDM → VPD**: [UDM](https://github.com/AliDujie/universal-design-methods) research pain points → VPD pain relievers
- **VPD → QuantUX**: VPD experiment design → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) validation
- **VPD → SWD**: VPD canvas scores → [SWD](https://github.com/AliDujie/storytelling-with-data) value proposition stories
- **VPD → STM**: VPD competitive analysis → [STM](https://github.com/AliDujie/Structured-Thinking-Model) strategic frameworks

See the [full pipeline example](../README.md#complete-pipeline-example) in README.md for a 7-skill end-to-end workflow.
