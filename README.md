# Value Proposition Design — Knowledge Base & Skill

> 🎯 **创造客户想要的产品和服务**

[中文说明](#中文说明) | [English](#english)

---

## 中文说明

### 🌟 为什么使用这个技能？

- **经典框架** — 基于亚历山大·奥斯特瓦德《价值主张设计》，商业模式画布作者作品
- **八大模块** — 覆盖从客户洞察到价值放大的完整生命周期
- **实战工具** — Python 工具包支持画布创建、契合度分析、实验设计
- **双语支持** — 完整中英文文档，适合国际化团队
- **零依赖** — 纯 Python 标准库，5 分钟上手

### 🚀 5 分钟快速开始

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r skills/value-proposition-design ~/.aoneclaw/skills/
```

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/value-proposition-design")
from vpd import VPDSkill

# 初始化技能
skill = VPDSkill("我的产品")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: 创建客户概况 =====
skill.add_customer_segment("忙碌的职场人士")
skill.add_customer_job("快速解决午餐")
skill.add_pain_point("外卖配送慢", severity=4)
skill.add_pain_point("选择困难", severity=3)
skill.add_gain("希望健康", priority=3)
skill.add_gain("希望便捷", priority=5)
print(skill.render_customer_profile())

# ===== 场景 2: 设计价值主张 =====
skill.add_product_service("智能订餐 App")
skill.add_pain_reliever("30 分钟必达", addresses="外卖配送慢")
skill.add_pain_reliever("AI 推荐套餐", addresses="选择困难")
skill.add_gain_creator("营养分析", creates="希望健康")
skill.add_gain_creator("一键复购", creates="希望便捷")
print(skill.render_value_map())

# ===== 场景 3: 评估契合度 =====
fit_report = skill.assess_fit()
print(fit_report)  # 问题 - 解决方案契合度分析

# ===== 场景 4: 设计实验验证 =====
skill.add_experiment("落地页 A/B 测试", type="landing_page", metric="转化率")
skill.add_experiment("用户访谈", type="interview", metric="洞察数量")
print(skill.render_experiment_board())

# ===== 场景 5: 商业模式画布 =====
bmc = skill.build_business_model_canvas()
print(bmc)  # 9 大模块完整画布
```

### 💡 知识库内容

| 模块 | 核心内容 | 关键产出 |
|------|---------|---------|
| **商业模式建构工作原理** | 价值主张画布、商业模式画布、三种契合类型 | 画布模板、契合度评估 |
| **信息采集方法** | 六种客户洞察技巧、采访八大原则、B2B 多角色采集 | 访谈提纲、观察指南 |
| **信息整理方法** | 客户概况绘制最佳实践、分级排序、模式定义 | 客户画像、痛点优先级 |
| **升级迭代方法** | 原型创建 10 大原则、设计 - 验证 - 重复循环 | 原型计划、迭代路线 |
| **支撑业务决策** | 成功价值主张 10 大特性、战略画布、六顶思考帽 | 决策框架、评估清单 |
| **创新方法论** | 五种设计约束点、六种创新方法、推动 vs 拉动 | 创新机会、策略选择 |
| **量化分析方法** | 10 大测试原则、实验库工具集、CTA 分层、五个数据陷阱 | 实验设计、指标体系 |
| **价值放大核心理念** | 三层价值放大架构、多重契合、持续重塑 | 增长策略、扩张计划 |

### 📁 文件结构

```
value-proposition-design/
├── skills/value-proposition-design/
│   └── SKILL.md                 # AI Agent 技能定义
├── vpd/                         # Python 工具包（纯标准库）
│   ├── __init__.py              # VPDSkill 统一入口
│   ├── config.py                # 全局配置与常量
│   ├── utils.py                 # 工具函数
│   ├── canvas.py                # 价值主张画布引擎
│   ├── fit.py                   # 契合度分析
│   ├── experiment.py            # 实验设计引擎
│   └── bmc.py                   # 商业模式画布
├── knowledge-base.md            # 完整知识库文档（八大模块 + 术语表）
├── pyproject.toml
├── requirements.txt
└── README.md                    # 本文件
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的一部分：

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 种设计研究方法
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done 理论、进步力量分析
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — 量化研究、HEART 框架、A/B 测试
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — 人物角色创建、用户细分
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — 数据叙事、可视化设计

**推荐工作流**：
1. 用 JTBD 理解用户动机
2. 用 Web-Persona 创建用户画像
3. **用本技能设计价值主张和商业模式** ← 从洞察到方案
4. 用 Universal-Design-Methods 验证方案
5. 用 Quantitative-UX-Research 量化指标
6. 用 Storytelling-with-Data 向利益相关者呈现

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

### 📚 关于《Value Proposition Design》

- **书名**: Value Proposition Design: How to Create Products and Services Customers Want
- **作者**: Alexander Osterwalder, Yves Pigneur, Greg Bernarda, Alan Smith
- **出版**: Wiley, 2014
- **地位**: 商业模式画布作者作品，全球创业者必读
- **适用**: 创业者、产品经理、战略顾问、业务负责人

### 📜 许可

本技能仅供内部学习和研究使用。

### 👨‍💻 作者

- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

---

## English

### 🌟 Why Use This Skill?

- **Classic Framework** — Based on Alexander Osterwalder's "Value Proposition Design", from the Business Model Canvas author
- **Eight Modules** — Covering the complete lifecycle from customer insights to value amplification
- **Practical Tools** — Python toolkit for canvas creation, fit analysis, experiment design
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Zero Dependencies** — Pure Python standard library, 5-minute setup

### 🚀 5-Minute Quick Start

#### Step 1: Install

```bash
cp -r skills/value-proposition-design ~/.aoneclaw/skills/
```

#### Step 2: Import

```python
from vpd import VPDSkill
skill = VPDSkill("My Product")
```

#### Step 3: Use

```python
# Create customer profile
skill.add_customer_segment("Busy professionals")
skill.add_customer_job("Quick lunch solution")
skill.add_pain_point("Slow delivery", severity=4)
skill.add_gain("Want healthy", priority=3)

# Design value proposition
skill.add_product_service("Smart food ordering App")
skill.add_pain_reliever("30-min delivery", addresses="Slow delivery")
skill.add_gain_creator("Nutrition analysis", creates="Want healthy")

# Assess fit
print(skill.assess_fit())
```

### 💡 Knowledge Base Contents

| Module | Core Content | Key Outputs |
|--------|-------------|-------------|
| **Business Model Construction** | Value Proposition Canvas, Business Model Canvas, Three Fit types | Canvas templates, fit assessment |
| **Information Collection** | Six insight techniques, Eight interview principles, B2B multi-role | Interview guides, observation guides |
| **Information Organization** | Customer profile best practices, ranking, pattern definition | Customer profiles, pain point priorities |
| **Upgrade & Iteration** | 10 prototyping principles, Design-Validate-Repeat cycle | Prototype plans, iteration roadmap |
| **Business Decision Support** | 10 characteristics, Strategic canvas, Six Thinking Hats | Decision frameworks, evaluation checklists |
| **Innovation Methodology** | Five design constraints, Six innovations, Push vs Pull | Innovation opportunities, strategy choices |
| **Quantitative Analysis** | 10 testing principles, Experiment library, CTA layering, Five data traps | Experiment designs, metric systems |
| **Value Amplification** | Three-layer architecture, Multiple fits, Continuous reinvention | Growth strategies, expansion plans |

### 📁 File Structure

```
value-proposition-design/
├── skills/value-proposition-design/SKILL.md
├── vpd/                         # Python toolkit
├── knowledge-base.md            # Complete knowledge base
└── README.md                    # This file
```

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — Persona creation
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

### 📚 About the Book

- **Title**: Value Proposition Design: How to Create Products and Services Customers Want
- **Authors**: Alexander Osterwalder, Yves Pigneur, Greg Bernarda, Alan Smith
- **Publisher**: Wiley, 2014
- **Status**: Essential reading for entrepreneurs worldwide
- **For**: Entrepreneurs, Product Managers, Strategy Consultants, Business Leaders

### 📜 License

This skill is for internal learning and research use only.

### 👨‍💻 Author

- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫
