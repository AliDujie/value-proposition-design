# VPD 跨技能协作工作流

> Value Proposition Design × 6 相关技能的详细协作工作流
> VPD-Specific Cross-Skill Workflows for all 6 ecosystem skills

---

## 生态总览

VPD 是 7 技能生态系统的 **价值设计核心**，将用户研究转化为可验证的价值主张：

```
Persona (Who) → JTBD (What) → UDM (How) → VPD (Value) → QuantUX (Validate) → SWD (Present) → STM (Decide)
```

---

## 1. Persona → VPD：角色驱动的价值主张

### 数据流

| Persona 输出 | → VPD 输入 | 画布位置 |
|---------|-----------|---------|
| 角色画像（demographics + behaviors） | 客户细分（Customer Segment） | 客户概况 |
| 角色目标与动机 | 客户工作（Jobs） | 客户概况 |
| 角色痛点与挫折 | 客户痛点（Pains） | 客户概况 |
| 角色期望与收益 | 客户收益（Gains） | 客户概况 |
| 角色使用场景 | 产品与服务（Products & Services） | 价值图 |

### 协作工作流

```python
# Step 1: Persona 定义目标用户
from persona import PersonaSkill
persona = PersonaSkill("SaaS 协作平台")
profiles = persona.create(
    domain="团队协作工具",
    segment="中小企业团队负责人",
    evidence=["用户调研数据", "行为分析"])

# Step 2: 将 Persona 洞察转化为 VPD 画布
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "中小企业团队负责人")
canvas = vpd.analyze_canvas(
    product_name="TeamFlow",
    jobs=[
        {"description": "分配和跟踪团队任务", "category": "functional", "importance": 5},
        {"description": "获得团队掌控感", "category": "emotional", "importance": 4},
    ],
    pains=[
        {"description": "任务状态不透明，需要反复沟通", "severity": "critical"},
    ],
    gains=[
        {"description": "一眼看清团队进度", "desire_level": "expected"},
    ])

# Step 3: 验证 Persona 假设
# VPD 画布契合度低 → 重新审视 Persona 细分
if canvas.fit_score < 0.5:
    persona.refine(segment="更细的细分", evidence=["新数据"])
```

### 验证回路

VPD 画布契合度 < 0.5 → 返回 Persona 重新定义细分 → 更新 Persona 后重新填充画布

---

## 2. JTBD → VPD：从 Jobs 到价值画布

### 数据流

| JTBD 输出 | → VPD 输入 | 画布位置 |
|---------|-----------|---------|
| Functional / Emotional / Social Job | 客户工作（Jobs） | 客户概况 |
| Struggle intensity | 痛点严重度 | 客户概况 |
| Existing workarounds | 客户现有方案 | 价值图（参考） |
| Opportunity score | 画布元素优先级 | 优先级排序 |

### 协作工作流

```python
# Step 1: JTBD 发现高机会 Jobs
from jtbd import JTBDSkill
jtbd = JTBDSkill("SaaS 协作平台")

# 机会评分：挣扎度、替代方案、市场规模、预算
score = jtbd.score_opportunity(
    "跨团队依赖追踪",
    struggle=4, alternative=3, market=5, budget=4)
# → 如果 score ≥ 7，是好的价值主张候选

# Step 2: 将 JTBD 发现映射到 VPD 画布
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "工程经理")
canvas = vpd.analyze_canvas(
    product_name="TeamSync",
    jobs=[
        {"description": "追踪跨团队依赖关系", "importance": 5},
        {"description": "减少不必要的状态会议", "importance": 4},
    ],
    pains=[
        {"description": "依赖关系遗漏导致延期", "severity": "critical"},
        {"description": "过多的状态同步会议", "severity": "high"},
    ],
    gains=[
        {"description": "自动识别依赖风险", "desire_level": "required"},
    ])

# Step 3: 优先级排序
priority = vpd.calculate_priority([
    {"name": "依赖关系遗漏", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
    {"name": "状态会议过多", "importance": 4, "dissatisfaction": 4, "frequency": 5, "viability": 3},
])
```

### 验证回路

VPD 画布发现新痛点 → 返回 JTBD 重新访谈验证 → 更新 Opportunity Score → 调整 VPD 优先级

---

## 3. UDM → VPD：从研究数据到客户洞察

### 数据流

| UDM 输出 | → VPD 输入 | 使用方式 |
|---------|-----------|---------|
| 访谈发现（Contextual inquiry） | Jobs / Pains / Gains 列表 | 填充画布右侧 |
| 可用性测试发现 | 痛点缓释方案（Pain Relievers） | 填充画布左侧 |
| 体验历程图（Journey Map） | 关键时刻（Moments of Truth） | 确定实验验证优先级 |
| SUS / NPS 数据 | 当前体验基线 | 设计改进目标值 |

### 协作工作流

```python
# Step 1: UDM 执行用户研究
from udm import UDMSkill
udm = UDMSkill("SaaS 协作平台")

# 生成访谈提纲
interview = udm.generate_interview("工程经理深访", "contextual")

# 假设访谈发现：
# - 用户花在状态同步上的时间占工作日的 20%
# - 依赖遗漏是项目延期的第一大原因
# - 现有工具无法满足跨团队场景

# Step 2: 将研究发现转化为 VPD 画布
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "工程经理")
canvas = vpd.analyze_canvas(
    product_name="TeamSync",
    jobs=[{"description": "跨团队依赖追踪", "importance": 5}],
    pains=[{"description": "状态同步占用 20% 工作时间", "severity": "critical"}],
    gains=[{"description": "自动识别和预警依赖风险", "desire_level": "required"}])

# Step 3: 设计基于研究发现的实验
experiment = vpd.design_experiment(
    hypotheses=[
        {"description": "依赖风险预警能将项目延期减少 30%", "lethality": "lethal"},
        {"description": "用户愿意为跨团队功能支付 $10/月溢价", "lethality": "important"},
    ])
```

---

## 4. VPD → QuantUX：从假设到实验验证

### 数据流

| VPD 输出 | → QuantUX 输入 | 验证方法 |
|---------|-----------|---------|
| 价值主张假设 | A/B 测试假设 | 对照组实验 |
| 实验设计（测试卡/学习卡） | 实验参数 | 样本量计算 + 统计功效 |
| 画布契合度评分 | 基线指标 | HEART 框架测量 |
| 竞争战略评分 | MaxDiff 功能优先级 | 统计排序 |
| 优先级排序（P0-P3） | 实验优先级 | 多变量测试设计 |

### 协作工作流

```python
# Step 1: VPD 定义价值主张和假设
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "工程经理")
canvas = vpd.analyze_canvas(
    product_name="TeamSync",
    jobs=[{"description": "跨团队依赖追踪", "importance": 5}],
    pains=[{"description": "依赖遗漏导致延期", "severity": "critical"}],
    gains=[{"description": "自动风险预警", "desire_level": "required"}])

experiment = vpd.design_experiment(
    hypotheses=[
        {"description": "依赖风险预警提升准时交付率 30%", "lethality": "lethal"},
    ])

# Step 2: QuantUX 计算所需样本量并设计实验
from quantux import QuantUXSkill
quantux = QuantUXSkill("SaaS 协作平台")

# 计算 A/B 测试样本量
n = quantux.calculate_ab_sample_size(
    baseline=0.65,   # 当前准时交付率
    mde=0.10,         # 最小可检测效果 10%
    power=0.80,       # 统计功效
    alpha=0.05)       # 显著性水平

# 设计 HEART 指标体系
heart = quantux.heart_framework(
    happiness="用户满意度评分",
    engagement="日均活跃团队数",
    adoption="新功能使用率",
    retention="月度续费率",
    task_success="准时交付率")
```

### 验证回路

QuantUX 实验结果不显著 → 返回 VPD 重新设计假设或调整价值主张 → 重新实验

---

## 5. VPD → SWD：从数据到决策叙事

### 数据流

| VPD 输出 | → SWD 输入 | 呈现方式 |
|---------|-----------|---------|
| 画布契合度评分 | 数据仪表盘 | 指标可视化 |
| 实验结果（测试卡/学习卡） | 案例研究 | 三幕叙事结构 |
| 竞争战略（价值曲线） | 对比图表 | 雷达图/散点图 |
| CEO 扩展（商业化路径） | 路线图 | 时间轴可视化 |
| ROI 估算 | 商业案例 | 瀑布图/敏感性分析 |

### 协作工作流

```python
# Step 1: VPD 产出价值主张分析
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "工程经理")
canvas = vpd.analyze_canvas(product_name="TeamSync", jobs=[...], pains=[...], gains=[...])
strategy = vpd.analyze_competitor(
    my_name="TeamSync",
    factors=["依赖追踪", "实时协作", "集成能力", "定价"],
    players={"TeamSync": [9, 8, 7, 7], "竞品A": [6, 7, 8, 8], "竞品B": [5, 6, 7, 6]})

# Step 2: SWD 将分析结果转化为高管叙事
from swd import SWDSkill
swd = SWDSkill("PMF 评审")

# 构建故事上下文
context = swd.build_context(
    audience="VP of Product",
    cta="批准 TeamSync 依赖追踪功能进入开发")

# 推荐合适的图表类型
chart = swd.recommend_chart(
    data_type="comparison",
    category_count=3,
    purpose="competitive positioning")

# 构建完整故事
story = swd.build_story(
    protagonist="工程经理 Sarah",
    imbalance="项目延期率 40%，依赖遗漏是根因",
    call_to_action="批准 TeamSync 依赖追踪功能 Q3 上线",
    data_evidence=["契合度 0.78", "A/B 测试提升 25%", "ROI 预估 3.2x"])
```

---

## 6. VPD → STM：从价值验证到战略决策

### 数据流

| VPD 输出 | → STM 输入 | 战略框架 |
|---------|-----------|---------|
| 价值主张画布 | STM 商业画布 | 价值主张 → 商业模式 |
| 契合度评分 | 市场验证信号 | Go/No-Go 决策 |
| 竞争战略（蓝海四项行动） | 差异化定位 | 竞争战略矩阵 |
| CEO 扩展（护城河分析） | 护城河评估 | 可持续竞争优势 |
| ROI 估算 | 投资回报分析 | 资源分配决策 |

### 协作工作流

```python
# Step 1: VPD 完成价值验证
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "中小企业")

# 价值主张画布
canvas = vpd.analyze_canvas(
    product_name="TeamSync",
    jobs=[{"description": "一站式团队协作", "importance": 5}],
    pains=[{"description": "工具分散导致效率低下", "severity": "critical"}],
    gains=[{"description": "All-in-one 工作流", "desire_level": "expected"}])

# 竞争战略
strategy = vpd.analyze_competitor(
    my_name="TeamSync",
    factors=["集成度", "易用性", "价格", "客服"],
    players={"TeamSync": [9, 8, 7, 8], "Slack": [7, 9, 6, 7], "Teams": [8, 6, 8, 6]})

# CEO 视角分析
ceo_report = vpd.generate_canvas(include_ceo_analysis=True)
# → 包含商业化路径、护城河分析、ROI 估算

# Step 2: STM 进行结构化战略分析
from stm import STMSkill
stm = STMSkill("SaaS 协作平台战略")

# 使用 VPD 产出构建商业画布
business_canvas = stm.business_model_canvas(
    value_proposition="一站式团队协作平台，消除工具分散带来的效率损失",
    customer_segments="中小企业团队（10-100人）",
    channels="产品驱动增长 + 免费增值",
    revenue_streams="订阅制：$8/用户/月",
    cost_structure="研发 + 获客 + 基础设施")

# 竞争战略决策
competitive_analysis = stm.competitive_strategy(
    industry="团队协作 SaaS",
    differentiation="All-in-one 深度集成 vs 最佳单点工具组合",
    moat_sources=["网络效应", "转换成本", "数据积累"])

# Go/No-Go 决策框架
decision = stm.decision_framework(
    go_signals=[
        "VPD 契合度 ≥ 0.7",
        "A/B 测试统计显著",
        "LTV/CAC > 3"],
    no_go_signals=[
        "VPD 契合度 < 0.5",
        "实验结果不显著",
        "获客成本过高"])
```

### 验证回路

STM 战略分析发现商业模式不可持续 → 返回 VPD 调整价值主张或定价 → 重新验证

---

## 端到端 7 技能工作流

### 场景：SaaS 协作平台产品-市场验证

```python
# === Phase 1: 用户定义（Persona）===
from persona import PersonaSkill
persona = PersonaSkill("SaaS 协作平台")
profiles = persona.create(domain="团队协作工具", segment="中小企业团队负责人")
# → 定义了 3 个核心角色

# === Phase 2: 需求发现（JTBD）===
from jtbd import JTBDSkill
jtbd = JTBDSkill("SaaS 协作平台")
score = jtbd.score_opportunity("跨团队依赖追踪", struggle=4, alternative=3, market=5, budget=4)
# → 机会评分 8.2/10，高优先级

# === Phase 3: 用户研究（UDM）===
from udm import UDMSkill
udm = UDMSkill("SaaS 协作平台")
interview = udm.generate_interview("工程经理深访", "contextual")
# → 12 场访谈，发现关键痛点

# === Phase 4: 价值主张设计（VPD）=== ← 你在这里
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "中小企业")
canvas = vpd.analyze_canvas(
    product_name="TeamSync",
    jobs=[{"description": "跨团队依赖追踪", "importance": 5}],
    pains=[{"description": "工具分散导致效率低下", "severity": "critical"}],
    gains=[{"description": "All-in-one 工作流", "desire_level": "expected"}])
print(f"Fit score: {canvas.fit_score}")
# → 0.78，强匹配

priority = vpd.calculate_priority([
    {"name": "工具分散", "importance": 5, "dissatisfaction": 5, "frequency": 5, "viability": 4},
    {"name": "依赖遗漏", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
])

strategy = vpd.analyze_competitor(
    my_name="TeamSync",
    factors=["集成度", "易用性", "价格", "客服"],
    players={"TeamSync": [9, 8, 7, 8], "Slack": [7, 9, 6, 7], "Teams": [8, 6, 8, 6]})

experiment = vpd.design_experiment(
    hypotheses=[
        {"description": "一站式集成能将效率提升 30%", "lethality": "lethal"},
    ])

# === Phase 5: 实验验证（QuantUX）===
from quantux import QuantUXSkill
quantux = QuantUXSkill("SaaS 协作平台")
n = quantux.calculate_ab_sample_size(baseline=0.65, mde=0.10)
# → 每组需要 450 个用户

# === Phase 6: 数据叙事（SWD）===
from swd import SWDSkill
swd = SWDSkill("PMF 评审")
story = swd.build_story(
    protagonist="VP of Product",
    imbalance="工具碎片化导致效率低下",
    call_to_action="批准 TeamSync 进入开发")

# === Phase 7: 战略决策（STM）===
from stm import STMSkill
stm = STMSkill("SaaS 协作平台战略")
canvas = stm.business_model_canvas(
    value_proposition="一站式团队协作平台",
    customer_segments="中小企业（10-100人）",
    revenue_streams="订阅制：$8/用户/月")
```

---

## 协作最佳实践

### 1. 顺序原则

**研究 → 设计 → 验证 → 叙事 → 决策**

- JTBD/UDM 研究在前，VPD 设计在中，QuantUX 验证在后
- SWD 将验证结果转化为叙事，STM 基于叙事做决策
- **不要跳过步骤**：没有研究的画布是空中楼阁

### 2. 迭代原则

每个阶段都可能返回上游：

- VPD 契合度低 → 返回 JTBD/UDM 重新研究
- QuantUX 实验不显著 → 返回 VPD 调整假设
- STM 商业模式不可持续 → 返回 VPD 调整价值主张

### 3. 数据流原则

- **Persona** 提供"谁" → VPD 客户画像
- **JTBD** 提供"什么" → VPD Jobs
- **UDM** 提供"证据" → VPD Pains/Gains
- **VPD** 提供"假设" → QuantUX 实验
- **QuantUX** 提供"结果" → SWD 数据
- **SWD** 提供"故事" → STM 决策
- **STM** 提供"方向" → 下一轮迭代

### 4. CEO 视角

VPD 内置的 CEO 扩展（商业化路径、护城河、ROI）是连接产品验证与战略决策的桥梁：

- VPD CEO 分析 → STM 商业画布
- VPD 护城河分析 → STM 竞争战略
- VPD ROI 估算 → STM 投资回报分析

---

## 参考资料

- [02-ecosystem-workflows.md](02-ecosystem-workflows.md) — 跨技能协作模式详解
- [03-ecosystem-collaboration.md](03-ecosystem-collaboration.md) — VPD 与其他技能的数据流转
- [knowledge-base.md](knowledge-base.md) — VPD 完整方法论参考
