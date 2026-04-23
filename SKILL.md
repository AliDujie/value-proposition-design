---
name: value-proposition-design
description: 价值主张设计方法论 Skill - 基于奥斯特瓦德《价值主张设计》全书，覆盖客户洞察、画布分析、优先级计算、竞争战略、问卷设计、实验验证的完整方法论与可执行 Python 工具包
---

# Value Proposition Design Skill

基于《价值主张设计：如何构建商业模式最重要的环节》（亚历山大·奥斯特瓦德著）的完整方法论技能，提供 7 大可执行模块，能够针对具体业务场景直接产出结构化交付物。

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

依赖：Python >= 3.8 + pyyaml >= 6.0。`pip install pyyaml`

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

| Skill | 协作方式 |
|-------|---------|
| storytelling-with-data | VPD 画布数据 -> SWD 图表展示与故事构建 |
| jtbd-knowledge-skill | JTBD 研究结果 -> VPD 画布填充与优先级排序 |
| quantitative-ux-research | VPD 问卷设计 -> UXR 定量执行与分析 |
