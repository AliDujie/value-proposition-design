---
name: value-proposition-design
version: "2.4.135"
description: 价值主张设计方法论 Skill - 基于奥斯特瓦德《价值主张设计》全书，覆盖客户洞察、画布分析、优先级计算、竞争战略、问卷设计、实验验证的完整方法论与可执行 Python 工具包，以及CEO决策视角的商业化路径、竞争护城河与ROI估算
author: "渡劫"
---

![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

# Value Proposition Design Skill

基于《价值主张设计：如何构建商业模式最重要的环节》（亚历山大·奥斯特瓦德著）的完整方法论技能，提供 7 大可执行模块，能够针对具体业务场景直接产出结构化交付物。

## 🌐 AliDujie 技能生态系统

VPD 是 **产品-市场验证层**，接收 JTBD 的 Jobs 和 UDM 的用户研究，输出价值主张画布和实验验证：

```
┌─────────────────────────────────────────────────────────────┐
│                    AliDujie UX Research Ecosystem            │
│                                                             │
│   ┌──────────────┐                                          │
│   │   Persona    │ 👤 用户定义层 — 创建证据驱动的人物角色      │
│   └──────┬───────┘                                          │
│          │ 研究数据                                           │
│   ┌──────▼───────┐    ┌──────────────┐                      │
│   │  JTBD Skill  │◄──►│  UDM Skill   │ 📖 方法论核心 — 100种 │
│   └──────┬───────┘    └──────┬───────┘    设计研究方法       │
│          │ 需求洞察           │ 定性发现                      │
│   ┌──────▼───────┐    ┌──────▼───────┐                      │
│   │ VPD 本技能   │◄──►│  QuantUX     │ 📊 定量研究 — HEART/  │
│   └──────┬───────┘    └──────┬───────┘    A-B/MaxDiff        │
│          │ 价值主张           │ 定量验证                      │
│          └──────────┬────────┘                               │
│                     │ 研究发现                                │
│              ┌──────▼───────┐                                │
│              │  SWD Skill   │ 📈 数据叙事 — 数据可视化与汇报    │
│              └──────┬───────┘                                │
│                     │ 数据洞察                                │
│              ┌──────▼───────┐                                │
│              │  STM Skill   │ 🧠 战略分析 — 商业框架与决策      │
│              └──────────────┘                                │
│                                                             │
│  工作流: Persona → JTBD/UDM → QuantUX → VPD → SWD → STM    │
└─────────────────────────────────────────────────────────────┘
```

**VPD 的典型协作**：JTBD 发现 Jobs → UDM 用户研究 → VPD 画布填充 → 实验验证 → SWD 汇报 → STM 战略决策

### 🔗 Ecosystem Quick Start / 生态系统快速上手

VPD 是 7 技能工作流的**产品-市场验证层**——在 JTBD/UDM 完成用户研究后使用：

```python
# Step 1: VPD 价值主张画布分析
from vpd import VPDSkill
vpd = VPDSkill("SaaS协作平台", "中小企业团队负责人")
canvas = vpd.analyze_canvas(product_name="TeamFlow",
    jobs=[{"description": "团队协作", "category": "functional", "importance": 5}],
    pains=[{"description": "沟通不及时", "severity": "critical"}],
    gains=[{"description": "提升效率", "desire_level": "expected"}])

# Step 2: 实验验证
experiment = vpd.design_experiment(hypotheses=[{"description": "实时协作减少30%沟通时间", "lethality": "lethal"}])

# Step 3: CEO 视角分析
report = vpd.generate_canvas(include_ceo_analysis=True)
```

> 💡 **Try it now / 立即尝试**:
> ```python
> from vpd import VPDSkill
> skill = VPDSkill("你的产品", "目标用户")
> canvas = skill.analyze_canvas(product_name="产品名", jobs=[{"description": "核心任务"}], pains=[{"description": "痛点"}])
> ```

### ✅ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r value-proposition-design /your/agent/skills/`
- [ ] **导入** — `from vpd import VPDSkill`
- [ ] **初始化** — `skill = VPDSkill("产品名", "目标用户")`
- [ ] **画布分析** — `skill.analyze_canvas(product_name="...", jobs=[...], pains=[...])`
- [ ] **优先级计算** — `skill.calculate_priority([...])`
- [ ] **实验设计** — `skill.design_experiment(hypotheses=[...])`
- [ ] **CEO 分析** — `skill.generate_canvas(include_ceo_analysis=True)`

[English](README.md#quick-start-5-minutes) | [中文](#中文说明)

## 🧭 快速决策：什么时候使用 VPD？

| 你的需求 | 推荐技能 |
|---------|---------|
| 需要价值主张画布、实验验证、优先级排序 | ✅ **VPD（本技能）** |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要结构化商业分析框架 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 VPD 是验证层：把 JTBD/UDM 的发现映射到价值主张画布，用实验验证契合度。

### 💼 为什么团队选择 VPD

| 挑战 | 没有 VPD | 使用 VPD |
|------|----------|----------|
| 价值主张 | "我们什么都能做"——模糊 | Jobs-Pains-Gains 精准映射 |
| PMF 验证 | 先做再等用户来 | 结构化实验 + 契合度评分 |
| 竞争策略 | 功能对比清单 | 价值曲线 + 蓝海四项行动 |
| 客户理解 | 人口统计画像 | 行为驱动的真实 Jobs/Pains |
| 投资决策 | "感觉能行"——直觉 | CEO 视角 + 护城河分析 |

## 🌟 为什么选择 VPD？

- **经典方法论** — 基于 Alexander Osterwalder《Value Proposition Design》，全球 100 万+ 商业人士使用的价值主张框架
- **7 大可执行模块** — 客户洞察、画布分析、优先级计算、竞争战略、问卷设计、实验验证、CEO 商业化路径
- **CEO 视角** — 内置护城河分析、商业化路径、ROI 估算，让价值主张直接与商业决策挂钩
- **零学习成本** — 纯 Python 标准库，无外部依赖，`from vpd import VPDSkill` 即可使用
- **实验驱动** — 价值主张必须通过实验验证，而非团队投票或直觉，内置样本量计算
- **生态桥梁** — 连接 JTBD 的 Jobs 和 QuantUX 的验证，是产品-市场契合的关键环节

## ⚡ 快速上手 (Quick Start)

```python
from vpd import VPDSkill

vpd = VPDSkill("你的产品名", "目标用户")

# 价值主张画布分析
canvas = vpd.analyze_canvas(
    product_name="产品名",
    jobs=[{"description": "快速完成任务", "category": "functional", "importance": 5}],
    pains=[{"description": "流程繁琐", "severity": "high"}],
    gains=[{"description": "省时省力", "desire_level": "expected"}])

# 竞争战略画布（Blue Ocean + Value Curve）
strategy = vpd.analyze_competitor(
    my_name="我方产品",
    factors=["价格", "易用性", "集成能力", "客服"],
    players={"我方产品": [7, 8, 5, 6], "竞品A": [8, 6, 7, 5]})

# 实验设计
experiment = vpd.design_experiment(
    hypotheses=[{"description": "一键预订可提升转化率", "lethality": "lethal"}])
```

> 💡 **5 分钟上手**: `from vpd import VPDSkill` → 纯标准库，零依赖，开箱即用。

---

## ⚡ Quick Start — English Reference

> VPD is the **product-market validation layer** of the AliDujie UX Research Ecosystem. It maps discovered user Jobs (from JTBD) to a structured Value Proposition Canvas, then validates through experiments.

### When to Use VPD

| You need... | Use VPD | Need something else? |
|---|---|---|
| Value proposition canvas, experiment design | ✅ **This skill** | — |
| Discover user Jobs, opportunity scoring | → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) first, then VPD | |
| Quantitative A/B test validation | → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) after VPD | |
| Executive data storytelling | → [SWD](https://github.com/AliDujie/storytelling-with-data) after VPD | |

### Minimal Working Example

```python
from vpd import VPDSkill

skill = VPDSkill("SaaS Product", "Team Leads")
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[{"description": "Assign tasks", "importance": 5}],
    pains=[{"description": "Slow communication", "severity": "critical"}],
    gains=[{"description": "Real-time updates", "desire_level": "expected"}])
print(f"Fit score: {canvas.fit_score}")
```

### API Cheat Sheet

| Method | Purpose | Returns |
|---|---|---|
| `generate_interview()` | 5-stage interview guide | Markdown |
| `generate_survey()` | 6-part survey design | Markdown |
| `calculate_priority()` | 4D priority scoring (P0-P3) | Markdown |
| `analyze_canvas()` | Value Proposition Canvas + fit score | Markdown |
| `analyze_competitor()` | Competitive strategy + Blue Ocean | Markdown |
| `design_experiment()` | Hypothesis testing + test cards | Markdown |
| `calculate_sample_size()` | Minimum sample size calculation | Markdown |
| `generate_canvas(include_ceo_analysis=True)` | Canvas + CEO extensions | Markdown |
| `render_all()` | Full panorama report | Markdown |
| `summary()` | Structured summary data | dict |

### Ecosystem Integration

```python
# JTBD → VPD → QuantUX → SWD
from jtbd import JTBDSkill
from vpd import VPDSkill

jtbd = JTBDSkill("Project Management")
vpd = VPDSkill("Project Management", "Engineering Managers")
# JTBD discovers Jobs → VPD maps to canvas
```

For full cross-skill examples, see [USAGE.md](USAGE.md) and [README.md](README.md).

## 一、核心框架

**价值主张画布（Value Proposition Canvas）** 由两面构成：

| 侧 | 要素 | 说明 |
|-----|------|------|
| 右侧：客户概况 | 客户工作（Jobs） | 功能性 / 社会性 / 情感性 / 支持性 |
| | 客户痛点（Pains） | 不想要的结果、障碍、风险；需量化 |
| | 客户收益（Gains） | 必需的 / 期望的 / 渴望的 / 意外的 |
| 左侧：价值图 | 产品和服务 | 有形 / 无形 / 数字 / 财务 |
| | 痛点缓释方案 | 如何减轻特定客户痛点 |
| | 收益创造方案 | 如何创造客户收益 |

**三种契合类型**：问题-方案契合（书面上） -> 产品-市场契合（市场上） -> 商业模式契合（银行里）

## 二、7 大执行能力

1. **访谈提纲生成** -- 五阶段结构，B2B/B2C，八大原则
2. **问卷设计** -- 六 Part 结构，李克特量表，A/B 测试
3. **优先级计算** -- 4 维评分（重要性 x 不满意度 x 频率 x 可行性），P0-P3 分级
4. **画布分析** -- 客户概况 + 价值图填充，契合度诊断
5. **竞争战略画布** -- 竞争因素评分，蓝海四项行动框架
6. **实验设计** -- 假设拆解排序，测试卡 / 学习卡，CTA 分层
7. **CEO 视角扩展** -- 商业化路径、护城河分析、投入产出估算

## 三、触发条件总表

| 触发词 / 场景 | 执行能力 | 输出物 |
|---|---|---|
| 访谈 / 采访 / 用户沟通 | 一：访谈提纲 | 五阶段提纲 + 执行要点 |
| 问卷 / 调查 / 定量验证 | 二：问卷设计 | 六 Part 问卷 + 分析建议 |
| 优先级 / 排序 / 打分 / 哪个更重要 | 三：优先级计算 | 评分矩阵 + P0-P3 分级 |
| 画布 / 契合 / 价值图 / 客户概况 | 四：画布分析 | 完整画布 + 契合度评分 + 缺口分析 |
| 竞品 / 竞争 / 蓝海 / 差异化 | 五：竞争战略 | 评分表 + 价值曲线 + 蓝海策略 |
| 实验 / 测试 / 验证 / MVP | 六：实验设计 | 假设排序 + 测试卡 + 学习卡 |
| 商业化 / 护城河 / ROI / CEO视角 | 七：CEO 扩展 | 收入模型 + 单位经济 + 护城河 + 敏感性分析 |
| 综合价值主张设计 | 按顺序一到七 | 全景报告 |

## 四、目录结构

```
value-proposition-design/
├── SKILL.md                    # 本文件
├── references/
│   └── knowledge-base.md       # 全书八大主题知识库
├── vpd/                        # Python 工具包
│   ├── __init__.py             # VPDSkill 统一入口
│   ├── config.yaml             # 可调配置
│   ├── interview_generator.py
│   ├── survey_designer.py
│   ├── priority_calculator.py
│   ├── canvas_analyzer.py
│   ├── strategy_scorer.py
│   ├── sample_calculator.py
│   ├── experiment_designer.py
│   ├── utils.py
│   ├── requirements.txt        # pyyaml>=6.0
│   └── tests/test_all.py       # 14 个测试
├── pyproject.toml
└── .gitignore
```

## 五、知识库

详细知识文档位于 `references/knowledge-base.md`，按全书八大主题组织：

| 主题 | 核心内容 |
|------|---------|
| 一：商业模式建构 | 价值主张画布两面、商业模式画布九构件、三种契合类型 |
| 二：信息采集 | 客户工作 / 痛点 / 收益采集方法、访谈八大原则 |
| 三：信息整理 | 痛点严重度分级、收益期望度分级、工作重要性排序 |
| 四：设计方法 | 十种创新触发器、原型设计、从客户概况出发 vs 从价值图出发 |
| 五：测试方法 | 假设拆解、测试卡 / 学习卡、CTA 分层、投资就绪水平 |
| 六：创新策略 | 蓝海四项行动框架、价值曲线、差异化机会识别 |
| 七：量化方法 | 4 维优先级模型、样本量计算、统计显著性 |
| 八：决策支撑 | 数据陷阱检查、迭代建议、商业模式契合验证 |

---

## 六、Python 可执行工具包

### 6.1 安装

依赖：Python >= 3.9 + pyyaml >= 6.0。`pip install pyyaml`

### 6.2 VPDSkill 方法一览

`VPDSkill` 是所有模块的统一入口，只需传入业务场景和目标客户群即可调用全部功能。

```python
from vpd import VPDSkill
skill = VPDSkill("SaaS协作平台", "中小企业团队负责人")
```

| 方法 | 功能 | 返回值 |
|------|------|--------|
| `generate_interview()` | 生成访谈提纲（五阶段，B2B/B2C） | Markdown |
| `generate_survey()` | 设计调研问卷（六 Part） | Markdown |
| `calculate_priority()` | 计算优先级矩阵（P0-P3） | Markdown |
| `analyze_canvas()` | 分析价值主张画布 + 契合度诊断 | Markdown |
| `analyze_competitor()` | 竞争战略分析 + 蓝海策略 | Markdown |
| `design_experiment()` | 设计验证实验 + 测试卡 | Markdown |
| `calculate_sample_size()` | 计算最小样本量 | Markdown |
| `generate_commercialization_path()` | CEO：商业化路径 + 单位经济模型 | Markdown |
| `generate_competitive_moat()` | CEO：护城河分析 + 被复制风险 | Markdown |
| `generate_roi_estimate()` | CEO：投入产出估算 + 敏感性分析 | Markdown |
| `generate_canvas(include_ceo_analysis=True)` | 画布 + CEO 视角扩展 | Markdown |
| `render_all()` | 汇总所有已执行模块为全景报告 | Markdown |
| `summary()` | 返回结构化摘要数据 | dict |

### 6.3 核心模块详解

#### 模块 1：InterviewGenerator -- 访谈提纲

五阶段（暖场 -> 工作探索 -> 痛点挖掘 -> 收益发现 -> 收尾），B2B 自动生成四角色版本。

```python
skill.generate_interview(stage="探索期", customer_type="B2C", duration_minutes=45)
skill.generate_interview(customer_type="B2B", stage="验证期",
    known_hypotheses=["用户最大痛点是集成困难"])
```

#### 模块 2：SurveyDesigner -- 问卷设计

六 Part（筛选 -> 工作 -> 痛点 -> 收益 -> 价值主张验证 -> 人口统计），含李克特量表和 A/B 测试。

```python
skill.generate_survey(
    hypotheses=["用户最大痛点是协作效率低", "用户愿意为自动化额外付费"],
    jobs=["团队协作", "项目管理"], pains=["协作效率低", "信息不同步"],
    gains=["一键同步省时间", "实时状态可见"])
```

#### 模块 3：PriorityCalculator -- 优先级计算

4 维评分归一化 100 分，P0-P3 自动分级，支持竞品差异化系数。

```python
skill.calculate_priority([
    {"name": "协作效率低", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
    {"name": "信息不同步", "importance": 4, "dissatisfaction": 4, "frequency": 3, "viability": 3,
     "competition_coverage": "not_covered"},
])
# 底层模块直接使用
from vpd import PriorityCalculator
calc = PriorityCalculator()
calc.add_item("协作效率低", importance=5, dissatisfaction=5, frequency=4, viability=4)
```

#### 模块 4：CanvasAnalyzer -- 画布分析

填充客户概况 + 价值图，输出契合度评分和缺口分析。

```python
skill.analyze_canvas(product_name="SaaS协作平台",
    jobs=[{"description": "团队任务分配", "category": "functional", "importance": 5}],
    pains=[{"description": "协作效率低", "severity": "critical"}],
    gains=[{"description": "实时状态可见", "desire_level": "required"}],
    products=[{"description": "智能任务看板", "category": "digital"}],
    pain_relievers=[{"description": "自动任务分派", "target_pain": "协作效率低", "coverage": "full"}],
    gain_creators=[{"description": "实时仪表盘", "target_gain": "实时状态可见", "coverage": "full"}])
```

#### 模块 5：StrategyScorer -- 竞争战略

竞争因素评分、价值曲线、蓝海四项行动框架（剔除/减少/增加/创造）。

```python
skill.analyze_competitor(my_name="我方产品",
    factors=["价格", "易用性", "集成能力", "客服"],
    players={"我方产品": [7, 8, 5, 6], "竞品A": [8, 6, 7, 5], "竞品B": [6, 7, 8, 4]})
```

#### 模块 6：ExperimentDesigner -- 实验设计

假设按致命性排序、测试卡/学习卡、CTA 分层（L1-L5）、投资就绪水平。

```python
skill.design_experiment(
    hypotheses=[{"description": "用户愿意额外付费50元/月", "lethality": "lethal"},
                {"description": "最大痛点是协作效率低", "lethality": "important", "evidence_strength": "weak"}],
    test_cards=[{"hypothesis": "用户愿意额外付费50元/月", "test_method": "登录页MVP",
        "metric": "注册率", "threshold": "5%", "falsification": "注册率<2%则否定",
        "cta_level": "L3", "duration_days": 14, "sample_size": 200}])
```

#### SampleCalculator -- 样本量计算

```python
print(skill.calculate_sample_size(confidence=95, margin_of_error=0.05, population=1000))
```

### 6.4 CEO 视角扩展分析

从价值主张延伸到商业决策层面，三个独立方法 + 一个综合方法：

| 方法 | 核心内容 |
|------|---------|
| `generate_commercialization_path()` | 收入模型、CAC/LTV 单位经济、三阶段规模化路径 |
| `generate_competitive_moat()` | 5 大护城河评估、12 月建设路径、被复制风险预案 |
| `generate_roi_estimate()` | 产品/获客投入、3 年收入预测、敏感性分析 |
| `generate_canvas(include_ceo_analysis=True)` | 画布 + 以上三个分析的综合输出 |

```python
skill = VPDSkill("电商平台", "年轻消费者")
print(skill.generate_commercialization_path())   # 单独调用
print(skill.generate_canvas(include_ceo_analysis=True))  # 综合调用
```

### 6.5 端到端流程示例

```python
from vpd import VPDSkill
skill = VPDSkill("SaaS协作平台", "中小企业团队负责人")

skill.generate_interview(stage="探索期")          # 访谈提纲
skill.calculate_priority([                         # 优先级排序
    {"name": "协作效率低", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
    {"name": "信息不同步", "importance": 4, "dissatisfaction": 4, "frequency": 3, "viability": 3},
])
skill.analyze_canvas(product_name="SaaS协作平台",  # 画布分析（参数见 6.3 模块 4）
    jobs=[{"description": "团队任务分配", "category": "functional", "importance": 5}],
    pains=[{"description": "协作效率低", "severity": "critical"}],
    gains=[{"description": "实时状态可见", "desire_level": "required"}],
    products=[{"description": "智能任务看板", "category": "digital"}],
    pain_relievers=[{"description": "自动任务分派", "target_pain": "协作效率低", "coverage": "full"}],
    gain_creators=[{"description": "实时仪表盘", "target_gain": "实时状态可见", "coverage": "full"}])
skill.analyze_competitor(my_name="我方",           # 竞品分析
    factors=["价格", "易用性", "集成能力", "客服"],
    players={"我方": [7, 8, 5, 6], "竞品A": [8, 6, 7, 5]})
print(skill.generate_canvas(include_ceo_analysis=True))  # CEO 视角
print(skill.render_all())                          # 全景报告
print(skill.summary())                             # 结构化摘要
# -> {'business_scenario': 'SaaS协作平台', 'modules_count': 4, 'top_priority': '协作效率低', ...}
```

### 6.6 AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 始终通过 `VPDSkill` 类调用，传入业务场景和目标客户群 |
| 2 | **返回值** | 所有方法返回 Markdown 字符串，可直接展示给用户 |
| 3 | **触发映射** | 根据用户意图自动选择对应能力（参见触发条件总表） |
| 4 | **组合调用** | 综合任务按 访谈 -> 画布 -> 优先级 -> 竞争 -> 问卷 -> 实验 顺序执行 |
| 5 | **CEO 视角** | 涉及商业决策 / 投资 / 规模化时，调用 CEO 扩展方法 |
| 6 | **按需执行** | `render_all()` 只汇总已执行模块，支持部分调用 |
| 7 | **底层访问** | 可通过 `skill.priority` / `skill.canvas` 等属性直接操作底层模块 |
| 8 | **知识查阅** | 理论问题参考 `references/knowledge-base.md` |

### 6.7 测试

```bash
python vpd/tests/test_all.py          # 直接运行
python -m pytest vpd/tests/test_all.py -v  # 或 pytest
```

14 个测试覆盖：访谈提纲（B2C/B2B/校验）、问卷设计（基础/价值主张/校验）、优先级计算（基础/竞品系数）、画布分析、竞争战略、样本量计算、实验设计、VPDSkill（全流程/部分调用）。

### 6.8 与其他 Skill 的协作

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 用户研究可视化 | storytelling-with-data | VPD 产出画布 -> SWD 可视化关键数据 |
| JTBD 深度研究 | jtbd-knowledge-skill | JTBD 分析 -> VPD 画布填充 + 优先级排序 |
| 定量研究验证 | quantitative-ux-research | VPD 问卷设计 -> UXR 执行 -> VPD 优先级计算 |
| 竞品分析展示 | storytelling-with-data | VPD 竞争战略 -> SWD 图表改造 + 故事构建 |
| 商业策略分析 | structured-thinking-model | STM 商业画布 → VPD 价值验证 → STM 战略决策 |
| 角色驱动设计 | web-persona-skill | Persona 目标/痛点 → VPD 画布 → Persona 验证 |
| 用户研究洞察 | universal-design-methods | UDM 用户研究 → VPD 画布填充 → 实验验证 |

**协作示例（JTBD → VPD）**：
```python
# Step 1: JTBD 发现核心 Job 和机会分数
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行预订")
opportunity = jtbd.score_opportunity("快速找到合适住处", struggle=4, alternative=3, market=4, budget=4)
# Step 2: VPD 将 JTBD 发现映射到价值主张画布
from vpd import VPDSkill
vpd = VPDSkill("旅行预订平台", "商务人士")
canvas = vpd.analyze_canvas(product_name="旅行预订",
    jobs=[{"job": "快速找到合适住处", "importance": "高"}],
    pains=[{"pain": "选择过多难以决策", "severity": "critical"}],
    gains=[{"gain": "省时省力", "relevance": "高"}])
print(f"匹配度: {canvas.fit_score}")
```

**协作示例（VPD → SWD）**：
```python
# Step 1: VPD 产出画布分析结果
from vpd import VPDSkill
vpd = VPDSkill("电商平台", "年轻消费者")
canvas = vpd.analyze_canvas(product_name="电商平台", jobs=[...], pains=[...], gains=[...])
# Step 2: SWD 将画布数据转化为汇报故事
from swd import SWDSkill
swd = SWDSkill("价值主张汇报")
ctx = swd.build_context(audience="决策层", cta="批准价值主张优化预算")
```

---

## 七、最佳实践

| # | 实践 | 说明 |
|---|------|------|
| 1 | 先客户后方案 | 永远从客户概况（右侧）开始，再设计价值图（左侧） |
| 2 | 量化具体化 | 痛点写"等待超过 5 分钟"而非"等待时间长" |
| 3 | 事实非观点 | 访谈问"上次怎么做的"而非"你觉得怎么样" |
| 4 | 致命假设优先 | 优先测试如果为假就毁掉整个方案的假设 |
| 5 | 区分三种契合 | 书面契合不等于市场契合，不要过早扩张 |
| 6 | 迭代非线性 | 设计和验证之间持续反复，不是线性瀑布 |
| 7 | 多客户群画布 | 不同客户细分各做一张画布，不要混在一起 |
| 8 | 竞品覆盖纳入优先级 | 竞品未覆盖的痛点是差异化机会 |
| 9 | CEO 视角前置 | 早期就考虑商业化路径和护城河，避免做出无法盈利的产品 |
| 10 | 数据陷阱检查 | 每次实验后检查假正面、假负面和局部最大值风险 |

### ⛔ 何时不使用 VPD

- **选择研究方法或设计定性研究** — 使用 [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **统计分析或 A/B 测试** — 使用 [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **理解用户 Jobs-to-be-Done** — 使用 [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **创建人物角色** — 使用 [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **数据可视化与叙事** — 使用 [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)


## 八、参考资料

### 核心书籍

| 书名 | 作者 | 关键贡献 |
|------|------|---------|
| **Value Proposition Design** | Alexander Osterwalder et al. (2014) | 本 Skill 的理论基础 |
| Business Model Generation | Alexander Osterwalder (2010) | 商业模式画布 |
| The Mom Test | Rob Fitzpatrick (2013) | 客户访谈方法论 |
| Lean Startup | Eric Ries (2011) | MVP 和验证式学习 |
| Blue Ocean Strategy | W. Chan Kim (2004) | 蓝海四项行动框架 |

### 相关 Skill

VPD 是 AliDujie UX 研究技能生态系统的产品-市场验证层：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 画布数据可视化 | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | VPD 画布 → SWD 图表展示 → SWD 故事构建 |
| JTBD 到价值主张 | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD Jobs → VPD 画布填充 → VPD 优先级排序 |
| 价值主张验证 | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | VPD 假设 → QuantUX A/B 测试 → VPD 实验设计 |
| 角色到价值主张 | [Web Persona](https://github.com/AliDujie/web-persona-skill) | Persona 目标/痛点 → VPD 画布 → Persona 验证 |
| 研究到价值主张 | [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | UDM 用户研究 → VPD 画布 → VPD 实验验证 |
| 结构化战略分析 | [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | VPD 商业分析 → STM 战略框架 → STM 决策建议 |

**协作示例（JTBD → VPD → SWD）**：
```python
# Step 1: JTBD 发现用户核心 Job
# Step 2: VPD 将 Job 映射到价值主张画布
from vpd import VPDSkill
vpd = VPDSkill("旅行平台", "商务人士")
vpd.analyze_canvas(product_name="旅行预订", jobs=[...], pains=[...])
# Step 3: SWD 将画布数据可视化
from swd import SWDSkill
swd = SWDSkill("价值主张汇报")
story = swd.build_story(protagonist="决策层", imbalance="产品-市场契合度不足")
```

## 参考资料（扩展）

| 书名 | 作者 | 关键贡献 |
|------|------|---------|
| **Value Proposition Design** | Alexander Osterwalder (2014) | 本 Skill 理论基础，价值主张画布 |
| Business Model Generation | Alexander Osterwalder (2010) | 商业模式画布九构件 |
| The Mom Test | Rob Fitzpatrick (2013) | 客户访谈方法论 |
| Testing Business Ideas | David Bland & Alex Osterwalder (2020) | 实验验证方法论 |
| Blue Ocean Strategy | W. Chan Kim & Renée Mauborgne (2004) | 蓝海四项行动框架 |

### AliDujie 技能生态

VPD 是 **AliDujie UX 研究技能生态系统** 的产品-市场验证层，与其他 6 个技能协作：

```
┌─────────────────────────────────────────────────────────────┐
│                    AliDujie UX Research Ecosystem            │
│                                                             │
│   ┌──────────────┐                                          │
│   │   Persona    │ 👤 用户定义层 — 创建证据驱动的人物角色      │
│   └──────┬───────┘                                          │
│          │ 研究数据                                           │
│   ┌──────▼───────┐    ┌──────────────┐                      │
│   │  JTBD Skill  │◄──►│  UDM Skill   │ 📖 方法论核心 — 100种 │
│   └──────┬───────┘    └──────┬───────┘    设计研究方法       │
│          │ 需求洞察           │ 定性发现                      │
│   ┌──────▼───────┐    ┌──────▼───────┐                      │
│   │ VPD 本技能   │◄──►│  QuantUX     │ 📊 定量研究 — HEART/  │
│   └──────┬───────┘    └──────┬───────┘    A-B/MaxDiff        │
│          │ 价值主张           │ 定量验证                      │
│          └──────────┬────────┘                               │
│                     │ 研究发现                                │
│              ┌──────▼───────┐                                │
│              │  SWD Skill   │ 📈 数据叙事 — 数据可视化与汇报    │
│              └──────┬───────┘                                │
│                     │ 数据洞察                                │
│              ┌──────▼───────┐                                │
│              │  STM Skill   │ 🧠 战略分析 — 商业框架与决策      │
│              └──────────────┘                                │
│                                                             │
│  工作流: Persona → JTBD/UDM → QuantUX → VPD → SWD → STM    │
└─────────────────────────────────────────────────────────────┘
```

| 技能 | 定位 | 协作模式 |
|------|------|---------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法论核心 | UDM 用户研究 → VPD 画布填充 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD Jobs → VPD 画布 → 优先级排序 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量研究 | VPD 假设 → QuantUX A/B 测试验证 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户角色 | Persona 目标/痛点 → VPD 画布 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | VPD 产出 → SWD 数据故事 |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略框架 | STM 商业画布 → VPD 价值验证 |

### 💡 Pro Tip / 专业技巧
VPD 是 AliDujie 生态系统的**产品-市场验证层**。最强大的工作流：从 [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 发现 Jobs → VPD 填充画布并计算契合度 → 用 [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) A/B 测试验证假设 → 用 [SWD](https://github.com/AliDujie/storytelling-with-data) 向利益相关者呈现结果。VPD 的核心价值在于：在写代码之前，用结构化实验验证你的价值主张是否真正契合用户需求。

### 🔗 扩展生态：管理层技能 (Extended Ecosystem — C-Suite)

VPD 价值验证可与管理层技能结合，将产品-市场匹配转化为商业战略：

| 扩展技能 | 协作场景 |
|---------|----------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | VPD 护城河分析 → CEO 竞争战略决策 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | VPD 画布 → CPO 产品组合与 PMF 评估 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | VPD 价值主张 → CMO 品牌定位与 messaging |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | VPD 技术可行性 → CTO 技术投资与架构决策 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | VPD 实验验证 → CEO 计划调整与范围扩展 |

**协作示例（VPD → CMO Advisor）**：
```python
from vpd import VPDSkill
from cmo import CMOAdvisor

vpd = VPDSkill("SaaS协作平台", "中小企业团队负责人")
canvas = vpd.analyze_canvas(product_name="TeamFlow", jobs=[...], pains=[...])

cmo = CMOAdvisor("TeamFlow")
# VPD 验证后的价值主张直接输入 CMO 做品牌定位
messaging = cmo.generate_messaging(value_proposition="提升团队协作效率")
```

## ❓ FAQ / 常见问题

**Q: VPD 和 JTBD 有什么区别？应该先用哪个？**
JTBD 发现用户要完成的"工作"（Jobs），VPD 将这些 Jobs 映射到价值主张画布。先用 JTBD 发现高机会 Jobs，再用 VPD 设计解决方案。顺序：JTBD → VPD。

**Q: 画布契合度多少算合格？**
契合度评分 0-1。≥0.7 强匹配（可以进入开发），0.5-0.7 合理但有缺口（需要实验验证），<0.5 显著不匹配（重新审视假设）。

**Q: 什么是"致命假设"（Lethal Hypothesis）？**
如果被证伪会毁掉整个产品方案的假设。VPD 按致命性排序实验——先测试最危险的假设，避免在错误的方向上浪费资源。

**Q: 只有定性数据也能用 VPD 吗？**
可以。`analyze_canvas()` 和 `design_experiment()` 完全适用于 [UDM](https://github.com/AliDujie/universal-design-methods) 访谈的定性发现。后续有流量时再用 [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) 做定量验证。

---

## ❓ FAQ — English

**Q: What's the difference between VPD and JTBD? Which should I use first?**
JTBD discovers the user's Jobs. VPD maps those Jobs to a Value Proposition Canvas. Use JTBD first to find high-opportunity Jobs, then VPD to design solutions. Order: JTBD → VPD.

**Q: What fit score is good enough?**
Fit score ranges 0–1. ≥0.7 = strong match (ready to build), 0.5–0.7 = reasonable but gaps exist (needs experiments), <0.5 = significant mismatch (revisit assumptions).

**Q: What is a "lethal hypothesis"?**
A hypothesis that, if falsified, would destroy the entire product concept. VPD sorts experiments by lethality — test the riskiest assumptions first to avoid wasting resources on the wrong direction.

**Q: Can I use VPD with only qualitative data?**
Yes. `analyze_canvas()` and `design_experiment()` work perfectly with qualitative findings from [UDM](https://github.com/AliDujie/universal-design-methods) interviews. When you have traffic, use [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) for quantitative validation.

**Q: Is there a "lean-start" mode for time-constrained teams?**
Yes — see the "5-Minute Quick Start Checklist" at the top of [README.md](README.md). For teams with 1 week, use: Canvas (Day 1) → Priority (Day 2) → Experiment Design (Day 3-5) → Read results (Day 6-7). See the full lean-start recipe in the README.

## 📎 Related Documents

- [README.md](README.md) — Full documentation with detailed code examples
- [USAGE.md](USAGE.md) — Usage guide with core workflows and ecosystem integration
- [INSTALL.md](INSTALL.md) — Installation guide with troubleshooting
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [references/knowledge-base.md](references/knowledge-base.md) — Full knowledge base (8 chapters)
