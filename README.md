# Value Proposition Design Skill

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--04--29-brightgreen.svg)

> 💎 **一句话介绍**: 基于《价值主张设计》（亚历山大·奥斯特瓦德著）的完整方法论工具包。覆盖客户洞察、画布分析、优先级计算、竞争战略、实验验证，内置 CEO 视角的商业化路径分析。

[English](#english) | [中文](#中文说明)

---

## 中文说明

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **经典方法论** — 基于 Alexander Osterwalder《Value Proposition Design》，全球 100 万+ 商业人士使用的价值主张框架
- **完整方法论** — 覆盖客户洞察、画布分析、优先级计算、竞争战略、实验验证
- **CEO 视角** — 内置商业化路径、护城河分析、ROI 估算
- **零依赖** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **双语支持** — 完整中英文文档，适合国际化团队
- **即插即用** — API 设计直观，代码示例丰富，即刻产出价值主张分析报告

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r value-proposition-design /your/agent/skills/
```

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/value-proposition-design")
from vpd import VPDSkill

skill = VPDSkill("SaaS 协作平台", "中小企业团队负责人")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: 价值主张画布分析 =====
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[{"job": "团队协作", "type": "功能性", "importance": "高"}],
    pains=[{"pain": "沟通不及时", "severity": "高"}],
    gains=[{"gain": "提升效率", "relevance": "高"}],
    products=[{"product": "实时协作编辑"}],
    pain_relievers=[{"reliever": "即时通知"}],
    gain_creators=[{"creator": "自动化工作流"}],
)
print(f"匹配度: {canvas.fit_score}")  # 0.85 (高匹配度)

# ===== 场景 2: 访谈提纲生成 =====
interview = skill.generate_interview()
print(interview)  # 结构化客户访谈提纲

# ===== 场景 3: 实验设计验证 =====
experiment = skill.design_experiment(
    hypothesis="实时协作编辑能减少 30% 的沟通时间",
    metric="每日消息数量",
    success_criteria="消息数量减少 ≥ 30%",
    duration_days=14
)
print(f"每组需要 {experiment.sample_size} 个用户")

# ===== 场景 4: CEO 视角商业分析 =====
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)  # 护城河 + 商业化路径 + ROI 估算
```

### 💡 核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **访谈提纲生成** | `interview.py` | 客户洞察访谈框架 |
| 2 | **调查问卷设计** | `survey.py` | 价值主张验证问卷 |
| 3 | **优先级计算** | `priority.py` | 痛点/收益优先级排序 |
| 4 | **价值主张画布** | `canvas.py` | 客户画像 × 价值地图 适配分析 |
| 5 | **竞争战略评分** | `strategy.py` | 差异化竞争评估 |
| 6 | **实验设计** | `experiment.py` | 价值假设验证实验 |
| 7 | **样本量计算** | `sample.py` | 统计显著性样本量 |

### 🔧 实用示例

#### 示例 1: 完整价值主张设计流程

```python
from vpd import VPDSkill

skill = VPDSkill("SaaS 协作平台", "中小企业团队负责人")

# 步骤 1: 客户洞察 - Jobs / Pains / Gains
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
print(f"匹配度: {canvas.fit_score}")  # 0.85 (高匹配度)

# 步骤 2: 设计实验验证
experiment = skill.design_experiment(
    hypothesis="实时协作编辑能减少 30% 的沟通时间",
    metric="每日消息数量",
    success_criteria="消息数量减少 ≥ 30%",
    duration_days=14
)
print(f"每组需要 {experiment.sample_size} 个用户")

# 步骤 3: CEO 视角商业分析
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)
```

#### 示例 2: 竞争战略分析

```python
from vpd import VPDSkill

skill = VPDSkill("电商平台", "年轻消费者")

# 竞争战略评分
strategy = skill.analyze_strategy(
    competitors=[
        {"name": "淘宝", "strengths": ["品类丰富"], "weaknesses": ["体验复杂"]},
        {"name": "拼多多", "strengths": ["价格优势"], "weaknesses": ["品质参差"]}
    ],
    our_strengths=["社交推荐", "个性化"],
    our_weaknesses=["品类较少"]
)
print(strategy)
```

#### 示例 3: CEO 视角商业分析

```python
# CEO 视角：商业化路径 + 护城河 + ROI
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)
# 输出包含：
# - 护城河分析（网络效应 + 数据积累）
# - 商业化路径（Freemium → Premium → Enterprise）
# - ROI 估算（LTV/CAC ≥ 3x）
```

### 📁 项目结构

```
value-proposition-design/
├── SKILL.md              # AI Agent 技能定义
├── README.md             # 本文件
├── pyproject.toml        # Python 包构建配置
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
└── README.md
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的价值设计核心：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│         (量化研究)   三角测量            Methods (通用设计)  │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                      (需求洞察)               │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│         (数据叙事)   呈现              Design (价值设计)      │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (人物角色)               │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **VPD + UDM** → 用 UDM 访谈/观察方法收集客户洞察，填充 VPD 画布
- **VPD + QuantUX** → 用 A/B 测试验证价值主张假设
- **VPD + JTBD** → 将 JTBD 发现映射到价值主张画布的 Jobs
- **VPD + Persona** → 用人物角色驱动价值设计
- **VPD + SWD** → 用数据叙事向高管呈现价值主张效果

👉 **探索完整生态系统**: [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [人物角色](https://github.com/AliDujie/web-persona-skill) | [量化 UX 研究](https://github.com/AliDujie/Quantitative-UX-Research) | [数据叙事](https://github.com/AliDujie/storytelling-with-data)

### 🛠️ 故障排查 (Troubleshooting)

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 画布匹配度低 | Pain/Gain 与产品功能不匹配 | 重新审视客户洞察，确保痛点真实存在 |
| 实验设计无法验证 | 指标不够具体 | 用可量化指标替代模糊目标 |
| 优先级排序不合理 | 重要度评分主观 | 结合用户调研数据，用 JTBD 机会分数辅助 |
| 竞争战略评分低 | 差异化不足 | 聚焦独特价值主张，避免同质化竞争 |

### 🤝 最佳实践

#### 价值主张画布检查清单

- [ ] **客户 Jobs** — 是否覆盖了功能性、情感性、社交性三类 Jobs？
- [ ] **Pains** — 是否按严重程度和频率排序？
- [ ] **Gains** — 是否区分了期望型和惊喜型收益？
- [ ] **Products & Services** — 是否每个 Pain 都有对应的 Reliever？
- [ ] **Fit Score** — 匹配度是否 > 0.7？

#### 实验设计原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **可证伪** | 假设必须能被数据证伪 | "实时协作减少 30% 沟通时间" ✅ |
| **可测量** | 指标必须可量化 | "提升效率" ❌ → "每日消息减少" ✅ |
| **有时限** | 实验必须有明确周期 | "运行 14 天" |
| **有基准** | 需要对照组或历史数据 | "相比上周下降 30%" |

### 📚 关于《Value Proposition Design》

- **书名**: Value Proposition Design: How to Create Products and Services Customers Want
- **作者**: Alexander Osterwalder, Yves Pigneur, et al.
- **出版**: Wiley, 2014
- **核心概念**: 价值主张画布、客户画像、适配测试
- **适用**: 产品经理、创业者、设计师、营销人员

### 📦 依赖

- Python >= 3.9
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Classic Methodology** — Based on Alexander Osterwalder's "Value Proposition Design", used by 1M+ business professionals globally
- **Complete Framework** — Customer insights, canvas analysis, priority calculation, competitive strategy, experiment validation
- **CEO Perspective** — Built-in monetization paths, moat analysis, ROI estimation
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Plug-and-Play** — Intuitive API, rich code examples, produce value proposition reports immediately

### 🚀 Quick Start

```python
import sys
sys.path.insert(0, "/path/to/value-proposition-design")
from vpd import VPDSkill

skill = VPDSkill("SaaS Collaboration Platform", "SMB Team Leads")

# Value Proposition Canvas Analysis
canvas = skill.analyze_canvas(
    product_name="TeamFlow",
    jobs=[{"job": "Team collaboration", "type": "functional", "importance": "high"}],
    pains=[{"pain": "Communication delays", "severity": "high"}],
    gains=[{"gain": "Improved efficiency", "relevance": "high"}],
    products=[{"product": "Real-time collaborative editing"}],
    pain_relievers=[{"reliever": "Instant notifications"}],
    gain_creators=[{"creator": "Automated workflows"}],
)
print(f"Fit Score: {canvas.fit_score}")  # 0.85 (High fit)

# Experiment Design
experiment = skill.design_experiment(
    hypothesis="Real-time editing reduces communication time by 30%",
    metric="Daily message count",
    success_criteria="Message count reduction ≥ 30%",
    duration_days=14
)
print(f"Sample size per group: {experiment.sample_size}")

# CEO Perspective Analysis
report = skill.generate_canvas(include_ceo_analysis=True)
print(report)  # Moat + Monetization + ROI
```

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — Persona creation
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Web Persona](https://github.com/AliDujie/web-persona-skill) | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)

### 📦 Dependencies

- Python >= 3.9
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

---

## 📖 扩展阅读

| 书籍 | 作者 | 关联能力 |
|------|------|----------|
| 《Value Proposition Design》 | Osterwalder et al. | 全书方法论基础 |
| 《Business Model Generation》 | Alexander Osterwalder | 商业模式画布 |
| 《Testing Business Ideas》 | Alexander Osterwalder | 实验设计与验证 |
| 《The Lean Startup》 | Eric Ries | 构建-测量-学习循环 |

## 📜 许可 (License)

MIT License — 基于《Value Proposition Design》by Alexander Osterwalder et al.

## 👨‍💻 作者 (Credits)

- 基于《Value Proposition Design》by Alexander Osterwalder et al.
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
### 🏷️ GitHub Topics (Recommended)

```
value-proposition-design vpd business-model python-toolkit
customer-insights canvas-analysis experiment-design openclaw-skill
value-proposition-design alicloud
```

### 📦 Dependencies

- Python >= 3.9
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

---

## 📜 许可 (License)
| v2.0 | 2026-04-29 | 统一交叉引用为 GitHub 绝对链接，添加 GitHub Topics，更新 Last Updated 日期 |
| v1.7 | 2026-04-25 | 统一技能生态格式，更新交叉引用 |
| v1.6 | 2026-04-23 | 添加 badges、技能生态系统 ASCII 图、双语支持、Why Use This Skill?、Quick Start、最佳实践、作者信息 |
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

---

*Last Updated: 2026-04-29 | AliDujie Skill Ecosystem*
