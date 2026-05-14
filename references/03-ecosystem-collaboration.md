# VPD 跨技能协作指南

> Value Proposition Design 如何与 AliDujie 生态系统中的其他技能协作

---

## VPD 在生态系统中的位置

VPD 是 7 技能工作流的 **价值设计核心**，将用户需求转化为可验证的价值主张：

```
Persona → JTBD → UDM → QuantUX → VPD (你在这里) → SWD
```

## VPD → 其他技能的数据流转

### VPD → QuantUX：从假设到实验验证

VPD 定义的价值假设是 QuantUX 实验设计的主要输入：

| VPD 输出 | → QuantUX 输入 | 验证方法 |
|---------|-----------|---------|
| 价值假设 | A/B 测试假设 | 对照组实验 |
| 实验设计 | 样本量计算 | 统计功效分析 |
| 适配度评分 | 基线指标 | HEART 框架测量 |
| 竞争分析 | MaxDiff 功能优先级 | 统计排序 |

**协作示例：**
```python
# Step 1: VPD 定义价值主张
from vpd import VPDSkill
vpd = VPDSkill("旅行平台", "25-35 岁商旅用户")
canvas = vpd.analyze_canvas(
    product_name="旅行平台",
    jobs=["快速找到性价比酒店"],
    pains=["搜索耗时", "信息不透明"],
    gains=["节省时间", "价格保障"]
)

# Step 2: 设计验证实验
experiment = vpd.design_experiment(
    hypothesis="AI 推荐能将搜索时间减少 50%",
    metric="平均搜索时长"
)

# Step 3: QuantUX 执行定量验证
from quantux import QuantUXSkill
quantux = QuantUXSkill("旅行平台")
# 计算所需样本量
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.03)
print(f"每组需要 {n} 个用户")
```

### VPD → SWD：从实验结果到数据叙事

VPD 的实验结果通过 SWD 转化为决策叙事：

| VPD 输出 | → SWD 呈现 |
|---------|-----------|
| 画布适配度 | 适配度仪表盘 |
| 竞争战略画布 | 价值曲线图 |
| 实验结果 | A/B 测试报告 |
| ROI 估算 | 商业案例演示 |

**协作示例：**
```python
from vpd import VPDSkill
from swd import SWDSkill

vpd = VPDSkill("旅行平台", "商旅用户")
experiment = vpd.design_experiment(
    hypothesis="AI 推荐能将搜索时间减少 50%",
    metric="平均搜索时长"
)

# 用 SWD 呈现实验结果
swd = SWDSkill("价值主张验证报告")
context = swd.build_context(
    audience="产品 VP",
    cta="批准 AI 推荐功能开发"
)
chart = swd.recommend_chart(data_type="comparison", category_count=2)
```

## 反向引用：其他技能 → VPD

### JTBD → VPD：从 Jobs 到价值画布

JTBD 发现的 Jobs 直接映射 VPD 画布输入：

| JTBD 输出 | → VPD 画布位置 |
|---------|---------------|
| Job 描述 | 客户工作 (Jobs) |
| 阻碍因素 | 客户痛点 (Pains) |
| 期望结果 | 客户收益 (Gains) |
| 机会评分 | 画布元素优先级 |

**协作示例：**
```python
from jtbd import JTBDSkill
from vpd import VPDSkill

# JTBD 发现 Jobs
jtbd = JTBDSkill("旅行平台")
score = jtbd.score_opportunity("快速完成预订", struggle=4, importance=5)

# 将 JTBD 发现转化为 VPD 画布
vpd = VPDSkill("旅行平台", "商旅用户")
canvas = vpd.analyze_canvas(
    product_name="旅行平台",
    jobs=["快速完成预订"],
    pains=["搜索耗时"],
    gains=["节省时间"]
)
```

### Persona → VPD：从角色到细分画布

Persona 角色指导 VPD 的客户画像和客户细分：

| Persona 输出 | → VPD 画布位置 |
|---------|---------------|
| 角色描述 | 客户画像 (Customer Profile) |
| 角色细分 | 细分画布 (Segment Canvas) |
| 角色目标 | Jobs to Be Done |
| 角色痛点 | Pain Points |

### UDM → VPD：从研究数据到客户洞察

UDM 的研究发现提供 VPD 画布的证据基础：

| UDM 输出 | → VPD 输入 |
|---------|-----------|
| 访谈数据 | Jobs/Pains/Gains 列表 |
| 可用性测试 | Pain Points 严重度 |
| 问卷数据 | 客户优先级 |
| 体验历程图 | 关键接触点 Pain/Gain |

### QuantUX → VPD：从验证到迭代

QuantUX 的实验结果驱动 VPD 画布迭代：

| QuantUX 输出 | → VPD 迭代 |
|---------|-----------|
| A/B 测试结果 | 价值主张假设更新 |
| CSat 数据 | Pain/Gain 优先级重排 |
| HEART 指标 | 价值适配度校准 |
| MaxDiff 结果 | 画布元素优先级排序 |

## 完整工作流示例

```python
# 从 JTBD 发现到 VPD 验证的完整流程
from jtbd import JTBDSkill
from vpd import VPDSkill
from quantux import QuantUXSkill
from swd import SWDSkill

project = "在线协作平台"

# 1. JTBD: 发现用户 Jobs
jtbd = JTBDSkill(project)
jtbd.add_force("push", "现有工具太分散", intensity=4)
jtbd.add_force("pull", "All-in-one 解决方案", intensity=5)

# 2. VPD: 设计价值主张
vpd = VPDSkill(project, "中小团队")
canvas = vpd.analyze_canvas(
    product_name=project,
    jobs=["团队协作", "文档管理"],
    pains=["工具分散", "信息孤岛"],
    gains=["一站式工作流", "实时协作"]
)

# 3. QuantUX: 验证价值假设
quantux = QuantUXSkill(project)
experiment = vpd.design_experiment(
    hypothesis="一站式工具能将效率提升 30%",
    metric="任务完成时间"
)
n = quantux.calculate_ab_sample_size(baseline=0.50, mde=0.05)

# 4. SWD: 呈现给决策者
swd = SWDSkill(f"{project} 商业案例")
story = swd.build_story(
    protagonist="产品团队",
    imbalance="工具碎片化导致效率低下",
    call_to_action="批准 All-in-one 平台开发"
)

print("✅ 价值主张验证完成！")
```

## 最佳实践

1. **先验证再构建** — 用实验验证价值假设，避免盲目开发
2. **JTBD 驱动** — 用 JTBD 发现的 Jobs 作为画布输入，确保价值主张基于真实需求
3. **迭代更新** — 每次实验结果都用来更新画布，持续精化
4. **CEO 视角** — 利用 VPD 内置的商业化路径和护城河分析，连接产品与市场
5. **跨团队协作** — 用 SWD 将验证结果呈现给利益相关者，获取决策支持
