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

## 依赖

Python >= 3.9，无外部依赖。

## 许可

MIT License
