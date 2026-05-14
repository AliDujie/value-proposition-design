# VPD 跨技能协作指南

> 价值主张设计如何与 AliDujie 生态系统中的其他技能协作

---

## VPD 在生态系统中的位置

VPD 是 **产品-市场验证层**，处于研究（UDM/JTBD）和验证（QuantUX）之间：

```
UDM 用户研究 ──┐
               ├──► VPD 价值主张画布 ──► QuantUX 实验验证 ──► SWD 数据汇报
JTBD Jobs ─────┘
Persona 细分 ──┘
```

## 协作模式

### 模式 1: JTBD → VPD（需求到价值的映射）

JTBD 发现用户的核心 Jobs 和痛点，VPD 将其映射到价值主张画布：

| JTBD 输出 | → VPD 输入 | 画布位置 |
|-----------|-----------|---------|
| Functional Job | 客户工作（功能性） | 客户概况 |
| Emotional Job | 客户工作（情感性） | 客户概况 |
| Struggle intensity | 客户痛点严重度 | 客户概况 |
| Workaround | 客户现有替代方案 | 客户概况（隐含） |
| Opportunity Score | 价值主张优先级 | 价值图 |

### 模式 2: UDM → VPD（研究到设计的转化）

UDM 用户研究提供定性数据，VPD 将其转化为可测试的价值假设：

| UDM 输出 | → VPD 输入 | 使用方式 |
|----------|-----------|---------|
| 访谈发现 | 客户 Jobs/Pains/Gains | 填充画布右侧 |
| 可用性测试 | 痛点缓释方案 | 填充画布左侧 |
| 体验历程图 | 关键时刻 | 确定实验验证优先级 |
| SUS/NPS 数据 | 当前体验基线 | 设计改进目标 |

### 模式 3: VPD → QuantUX（假设到验证）

VPD 设计价值主张，QuantUX 提供统计验证：

| VPD 输出 | → QuantUX 输入 | 验证方法 |
|----------|---------------|---------|
| 价值主张画布 | A/B 测试假设 | 对比实验 |
| 实验设计 | 样本量计算 | 统计功效 |
| 优先级排序 | MaxDiff 分析 | 偏好测量 |
| 竞争战略 | 市场份额分析 | 基准测试 |

### 模式 4: VPD → SWD（数据到叙事）

VPD 实验结果通过 SWD 转化为决策叙事：

| VPD 输出 | → SWD 输入 | 呈现方式 |
|----------|-----------|---------|
| 契合度评分 | 数据仪表盘 | 指标可视化 |
| 实验结果 | 案例研究 | 三幕叙事 |
| 竞争分析 | 对比图表 | 雷达图/散点图 |
| 商业化路径 | 路线图 | 时间轴 |

## 端到端工作流示例

### 场景：旅行平台价值主张优化

```python
# === 阶段 1: 发现（UDM + JTBD）===
from udm import UDMSkill
from jtbd import JTBDSkill

udm = UDMSkill("旅行平台")
interview = udm.generate_interview("商旅用户深访", "contextual")

jtbd = JTBDSkill("旅行平台")
# JTBD 发现核心 Job: "快速找到性价比最优的差旅住宿"
# 机会评分: 8.2/10

# === 阶段 2: 价值设计（VPD）===
from vpd import VPDSkill

vpd = VPDSkill("旅行平台", "商旅用户")
canvas = vpd.analyze_canvas(
    product_name="商旅优选",
    jobs=["快速预订", "差旅报销", "价格最优"],
    pains=["搜索耗时", "价格不透明", "报销繁琐"],
    gains=["一键预订", "自动报销", "企业协议价"],
    products=["智能推荐", "差旅管理", "发票服务"],
    pain_relievers=["企业价直连", "自动行程单"],
    gain_creators=["差旅积分", "优先客服"]
)
# 契合度评分: 0.78

# === 阶段 3: 验证（QuantUX）===
from quantux import QuantUXSkill

quantux = QuantUXSkill("旅行平台")
sample_size = quantux.calculate_ab_sample_size(
    baseline=0.12,  # 当前转化率
    mde=0.02        # 期望提升 2%
)
print(f"需要 {sample_size} 样本量 per variant")

# === 阶段 4: 呈现（SWD）===
from swd import SWDSkill

swd = SWDSkill("Q2 价值主张优化汇报")
story = swd.build_story(
    protagonist="商旅用户",
    imbalance="差旅预订平均耗时 45 分钟",
    resolution="价值主张优化后降至 12 分钟"
)
```

## VPD 与其他技能的触发时机

| 当你... | 先做 | 然后用 VPD |
|---------|------|-----------|
| 有用户访谈数据但不知道怎么转化 | UDM | 画布填充 |
| 有 JTBD 机会但不知道怎么商业化 | JTBD | 竞争战略 + 商业化路径 |
| 有假设但不知道怎么验证 | 画布设计 | QuantUX 实验 |
| 有实验结果但不知道怎么汇报 | VPD 实验 | SWD 叙事 |
| 需要确定目标用户是谁 | — | Persona 先定义细分 |

## VPD 独立使用场景

虽然 VPD 与其他技能协作效果最佳，但也可独立使用：

- **竞品分析**：用竞争战略画布评估竞品价值主张
- **内部工作坊**：用画布工具引导团队对齐价值认知
- **投资人材料**：用商业化路径展示市场机会
- **产品路线图**：用优先级排序确定开发顺序

## 进阶：VPD 的 CEO 视角

VPD 内置 CEO 级商业决策支持：

| 模块 | CEO 关注 | 输出 |
|------|---------|------|
| 商业化路径 | 如何赚钱？ | 三阶段商业化路线图 |
| 护城河分析 | 如何防止竞争？ | 四种护城河评估 |
| ROI 估算 | 投入产出比？ | 投入 vs 预期回报估算 |
| 竞争战略 | 如何胜出？ | 蓝海四项行动框架 |

---

*本文档是 AliDujie VPD 技能生态系统的补充参考。*

## 🔗 生态系统中 VPD 的关键接口

VPD 在研究流程中扮演 **转化层** 的角色——将用户需求转化为可测试的商业假设：

```
用户洞察 (JTBD/Persona) → VPD 价值主张 → 实验验证 (QuantUX) → 数据呈现 (SWD)
```

| 上游技能 | 输入到 VPD | 下游技能 | VPD 输出 |
|---------|------------|---------|----------|
| JTBD | Jobs, Pains, Gains | QuantUX | 实验假设 |
| Persona | 角色细分需求 | SWD | ROI 分析 |
| UDM | 用户需求数据 | STM | 竞争战略 |
