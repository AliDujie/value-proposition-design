# Value Proposition Design Skill

基于《价值主张设计：如何构建商业模式最重要的环节》（亚历山大·奥斯特瓦德著）的完整方法论工具包。

## 为什么使用

- **完整方法论** — 覆盖客户洞察、画布分析、优先级计算、竞争战略、实验验证
- **CEO 视角** — 内置商业化路径、护城河分析、ROI 估算
- **零依赖** — 纯 Python 标准库实现

## 快速开始

```python
from vpd import VPDSkill

skill = VPDSkill("SaaS 协作平台", "中小企业团队负责人")

# 生成访谈提纲
interview = skill.generate_interview()

# 价值主张画布分析
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[{"job": "团队协作", "type": "功能性", "importance": "高"}],
    pains=[{"pain": "沟通不及时", "severity": "高"}],
    gains=[{"gain": "提升效率", "relevance": "高"}],
    products=[{"product": "实时协作编辑"}],
    pain_relievers=[{"reliever": "即时通知"}],
    gain_creators=[{"creator": "自动化工作流"}],
)

# CEO 视角：商业化路径 + 护城河 + ROI
report = skill.generate_canvas(include_ceo_analysis=True)
```

## 文件结构

```
value-proposition-design/
├── SKILL.md              # AI Agent 技能定义
├── vpd/                  # Python 包（纯标准库）
│   ├── __init__.py       # VPDSkill 统一入口
│   ├── interview.py      # 访谈提纲生成器
│   ├── survey.py         # 问卷设计器
│   ├── priority.py       # 优先级计算器
│   ├── canvas.py         # 价值主张画布分析
│   ├── strategy.py       # 竞争战略评分
│   ├── experiment.py     # 实验设计器
│   └── sample.py         # 样本量计算
├── references/           # 知识库文档
│   └── knowledge-base.md
├── pyproject.toml
└── README.md
```

## 相关技能

- [Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill) — 人物角色创建与应用
- [Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods) — 100 种设计研究方法
- [Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research) — 量化研究与 HEART 框架
- [Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事与可视化

## 实际案例

### 案例 1：SaaS 产品价值主张画布

```python
from vpd import VPDSkill

skill = VPDSkill("SaaS 协作平台", "中小企业团队负责人")

# 价值主张画布分析
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[
        {"job": "团队协作", "type": "功能性", "importance": "高"},
        {"job": "任务分配", "type": "功能性", "importance": "高"},
        {"job": "减少沟通成本", "type": "情感性", "importance": "中"}
    ],
    pains=[
        {"pain": "沟通不及时", "severity": "高", "frequency": "每天"},
        {"pain": "信息分散", "severity": "中", "frequency": "每周"}
    ],
    gains=[
        {"gain": "提升效率", "relevance": "高"},
        {"gain": "降低管理成本", "relevance": "高"}
    ],
    products=[{"product": "实时协作编辑"}],
    pain_relievers=[{"reliever": "即时通知", "pain": "沟通不及时"}],
    gain_creators=[{"creator": "自动化工作流", "gain": "提升效率"}]
)
print(canvas.fit_score)  # 输出: 0.85 (高匹配度)
```

### 案例 2：实验设计与验证

```python
# 设计实验验证价值主张
experiment = skill.design_experiment(
    hypothesis="实时协作编辑能减少 30% 的沟通时间",
    metric="每日消息数量",
    success_criteria="消息数量减少 ≥ 30%",
    duration_days=14
)
print(experiment.sample_size)  # 输出: 每组需要 256 个用户
```

### 案例 3：CEO 视角商业分析

```python
# CEO 视角：商业化路径 + 护城河 + ROI
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)
# 输出包含：
# - 护城河分析（网络效应 + 数据积累）
# - 商业化路径（Freemium → Premium → Enterprise）
# - ROI 估算（LTV/CAC ≥ 3x）
```

## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 画布匹配度低 | Pain/Gain 与产品功能不匹配 | 重新审视客户洞察，确保痛点真实存在 |
| 实验设计无法验证 | 指标不够具体 | 用可量化指标替代模糊目标 |
| 优先级排序不合理 | 重要度评分主观 | 结合用户调研数据，用 JTBD 机会分数辅助 |
| 竞争战略评分低 | 差异化不足 | 聚焦独特价值主张，避免同质化竞争 |

## 扩展阅读

| 书籍 | 作者 | 关联能力 |
|------|------|----------|
| 《Value Proposition Design》 | Osterwalder et al. | 全书方法论基础 |
| 《Business Model Generation》 | Alexander Osterwalder | 商业模式画布 |
| 《Testing Business Ideas》 | Alexander Osterwalder | 实验设计与验证 |
| 《The Lean Startup》 | Eric Ries | 构建-测量-学习循环 |

## 技能生态导航

与其他 AliDujie 技能协同使用，构建完整用户体验研究体系：

| 关联技能 | 协同场景 | 工作流示例 |
|----------|----------|------------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 用户洞察收集 | UDM 访谈/观察 → VPD 画布填充 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 价值主张可视化呈现 | VPD 分析 → SWD 图表向高管汇报 |
| [Quantitative UX Research](https://github.com/AliDujie/quantitative-ux-research) | 数据驱动价值验证 | VPD 假设 → QuantUX A/B 测试验证 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD → 价值主张映射 | JTBD 发现 → VPD 画布 Jobs 填充 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 角色驱动价值设计 | Persona 角色 → VPD 客户画像 |

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

## 依赖

Python >= 3.9，无外部依赖。

## 许可

MIT License

---

*Last Updated: 2026-04-23 | AliDujie Skill Ecosystem*
