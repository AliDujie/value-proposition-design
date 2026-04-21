"""
Value Proposition Design (VPD) - Python工具包

基于《价值主张设计》方法论的可执行计算工具，提供6大核心模块和统一入口类 VPDSkill。

统一入口:
    from vpd import VPDSkill
    skill = VPDSkill("飞猪国内酒店预订", "25-35岁商旅用户")
    print(skill.generate_interview())
    print(skill.render_all())

独立模块:
    - InterviewGenerator: 访谈提纲生成器（五阶段结构，B2B/B2C，八大原则）
    - SurveyDesigner: 问卷设计器（六Part结构，李克特量表，A/B测试）
    - PriorityCalculator: 优先级计算（4维评分，P0-P3分级）
    - CanvasAnalyzer: 价值主张画布分析（契合度诊断）
    - StrategyScorer: 竞争战略画布（蓝海分析）
    - SampleCalculator: 样本量计算（统计显著性）
    - ExperimentDesigner: 实验设计（测试卡/学习卡）
"""

from typing import Optional
from vpd.interview_generator import InterviewGenerator, InterviewConfig
from vpd.survey_designer import SurveyDesigner, SurveyConfig, SurveyHypothesis
from vpd.priority_calculator import PriorityCalculator, PriorityItem
from vpd.canvas_analyzer import CanvasAnalyzer, Job, Pain, Gain, Product, PainReliever, GainCreator
from vpd.strategy_scorer import StrategyScorer
from vpd.sample_calculator import SampleCalculator
from vpd.experiment_designer import ExperimentDesigner, Hypothesis, TestCard, LearningCard


class VPDSkill:

    def __init__(self, business_scenario: str, target_customer: str) -> None:
        self.business_scenario = business_scenario
        self.target_customer = target_customer
        self.interview = InterviewGenerator()
        self.survey = SurveyDesigner()
        self.priority = PriorityCalculator()
        self.canvas = CanvasAnalyzer()
        self.competitor = StrategyScorer()
        self.experiment = ExperimentDesigner()
        self.sample = SampleCalculator()
        self.canvas.customer_name = target_customer
        self._sections: dict[str, str] = {}

    def generate_interview(self, known_hypotheses: Optional[list[str]] = None,
                           duration_minutes: int = 45, customer_type: str = "B2C",
                           stage: str = "探索期") -> str:
        self.interview.configure(
            business_scenario=self.business_scenario,
            target_customer=self.target_customer,
            known_hypotheses=known_hypotheses,
            duration_minutes=duration_minutes,
            customer_type=customer_type,
            stage=stage,
        )
        md = self.interview.render_markdown()
        self._sections["interview"] = md
        return md

    def generate_survey(self, hypotheses: list[str | dict],
                        jobs: Optional[list[str]] = None,
                        pains: Optional[list[str]] = None,
                        gains: Optional[list[str]] = None,
                        value_propositions: Optional[list[str]] = None,
                        alternatives: Optional[list[str]] = None,
                        survey_type: str = "客户概况验证",
                        target_sample_size: int = 200,
                        channel: str = "线上") -> str:
        self.survey.configure(
            business_scenario=self.business_scenario,
            target_customer=self.target_customer,
            hypotheses=hypotheses,
            survey_type=survey_type,
            target_sample_size=target_sample_size,
            channel=channel,
        )
        if jobs:
            self.survey.set_jobs(jobs)
        if pains:
            self.survey.set_pains(pains)
        if gains:
            self.survey.set_gains(gains)
        if value_propositions:
            self.survey.set_value_propositions(value_propositions)
        if alternatives:
            self.survey.set_alternatives(alternatives)
        md = self.survey.render_markdown()
        self._sections["survey"] = md
        return md

    def calculate_priority(self, items: list[dict],
                           title: str = "优先级评估矩阵",
                           evaluation_type: str = "痛点") -> str:
        self.priority.clear()
        for item in items:
            self.priority.add_item(
                name=item["name"],
                importance=item["importance"],
                dissatisfaction=item["dissatisfaction"],
                frequency=item["frequency"],
                viability=item["viability"],
                competition_coverage=item.get("competition_coverage"),
            )
        md = self.priority.render_markdown(title=title, evaluation_type=evaluation_type)
        self._sections["priority"] = md
        return md

    def analyze_canvas(self, product_name: str,
                       jobs: list[dict],
                       pains: list[dict],
                       gains: list[dict],
                       products: list[dict],
                       pain_relievers: list[dict],
                       gain_creators: list[dict]) -> str:
        self.canvas = CanvasAnalyzer()
        self.canvas.customer_name = self.target_customer
        self.canvas.product_name = product_name
        for j in jobs:
            self.canvas.add_job(j["description"], j["category"], j.get("importance", 3))
        for p in pains:
            self.canvas.add_pain(p["description"], p["severity"], p.get("quantified_metric", ""))
        for g in gains:
            self.canvas.add_gain(g["description"], g["desire_level"], g.get("quantified_metric", ""))
        for pr in products:
            self.canvas.add_product(pr["description"], pr["category"])
        for pr in pain_relievers:
            self.canvas.add_pain_reliever(pr["description"], pr["target_pain"], pr.get("coverage", "full"))
        for gc in gain_creators:
            self.canvas.add_gain_creator(gc["description"], gc["target_gain"], gc.get("coverage", "full"))
        md = self.canvas.render_markdown()
        self._sections["canvas"] = md
        return md

    def analyze_competitor(self, my_name: str,
                           factors: list[str],
                           players: dict[str, list[int]]) -> str:
        self.competitor = StrategyScorer()
        self.competitor.set_factors(factors)
        for name, scores in players.items():
            self.competitor.add_player(name, scores)
        md = self.competitor.render_markdown(my_name)
        self._sections["competitor"] = md
        return md

    def design_experiment(self, hypotheses: list[dict],
                          test_cards: Optional[list[dict]] = None) -> str:
        self.experiment = ExperimentDesigner()
        for h in hypotheses:
            self.experiment.add_hypothesis(
                description=h["description"],
                hypothesis_type=h.get("hypothesis_type", "value_proposition"),
                lethality=h.get("lethality", "lethal"),
                evidence_strength=h.get("evidence_strength", "none"),
            )
        for tc in (test_cards or []):
            self.experiment.create_test_card(
                hypothesis=tc["hypothesis"],
                test_method=tc["test_method"],
                metric=tc["metric"],
                threshold=tc["threshold"],
                falsification=tc["falsification"],
                cta_level=tc.get("cta_level", "L2"),
                duration_days=tc.get("duration_days", 14),
                sample_size=tc.get("sample_size", 50),
            )
        md = self.experiment.render_markdown()
        self._sections["experiment"] = md
        return md

    def calculate_sample_size(self, confidence: int = 95,
                              margin_of_error: float = 0.05,
                              proportion: float = 0.5,
                              population: int = 0) -> str:
        md = self.sample.render_markdown(confidence, margin_of_error, proportion, population)
        self._sections["sample"] = md
        return md

    def generate_commercialization_path(self) -> str:
        """
        生成商业化路径（CEO 视角）
        
        从价值主张延伸到收入模型、单位经济模型、规模化路径。
        """
        return f"""
## 商业化路径

---

### 收入模型

| 收入来源 | 定价策略 | 预计占比 | 验证状态 | 关键假设 |
|---------|---------|---------|---------|---------|
| 订阅收入 | XXX 元/月 | XX% | 未验证 | XXX |
| 交易佣金 | X% | XX% | 未验证 | XXX |
| 增值服务 | XXX 元/次 | XX% | 未验证 | XXX |

**定价逻辑**: 
- 基于成本：成本 XX 元，毛利率 XX%
- 基于价值：用户愿意支付 XXX 元（依据：XXX）
- 基于竞争：竞品定价 XXX 元，我们定价 XXX 元

---

### 单位经济模型（Unit Economics）

#### 获客成本 (CAC) 估算
| 渠道 | 预计 CAC | 转化率 | 回本周期 |
|------|---------|--------|---------|
| 内容营销 | XXX 元 | X% | X 个月 |
| 付费广告 | XXX 元 | X% | X 个月 |
| 推荐获客 | XXX 元 | X% | X 个月 |

**加权平均 CAC**: XXX 元

#### 生命周期价值 (LTV) 估算
| 指标 | 估算值 | 依据 |
|------|--------|------|
| 平均客单价 | XXX 元 | XXX |
| 年消费频次 | X 次 | XXX |
| 平均留存时长 | X 个月 | XXX |
| **LTV** | **XXX 元** | 客单价 × 频次 × 留存 |

#### LTV/CAC 健康度
- **LTV/CAC 比值**: XXX（健康标准 > 3）
- **评估**: 🟢 健康 / 🟡 可接受 / 🔴 需优化

---

### 规模化路径

#### Phase 1: 0-1 验证期（0-6 个月）
**目标**: 验证价值主张和收入模型
**关键指标**: 付费用户数 XXX，月收入 XXX 万，LTV/CAC > 2
**资源需求**: 资金 XXX 万，团队 X 人

#### Phase 2: 1-10 增长期（6-18 个月）
**目标**: 验证可重复的获客模型
**关键指标**: 月增长率 XX%，CAC 回收期 < X 个月
**资源需求**: 资金 XXX 万，团队 X 人

#### Phase 3: 10-100 扩张期（18-36 个月）
**目标**: 规模化扩张，建立护城河
**关键指标**: 市场份额 XX%，收入 XXX 万/月
**资源需求**: 资金 XXX 万，团队 X 人
"""

    def generate_competitive_moat(self) -> str:
        """
        生成护城河分析（差异化来源和可持续性）
        
        分析当前和未来的竞争优势来源，评估被复制风险。
        """
        return f"""
## 护城河分析

---

### 当前差异化来源

| 来源 | 强度 | 可持续性 | 说明 | 验证状态 |
|------|------|---------|------|---------|
| 技术壁垒 | 高/中/低 | X 年 | XXX | 未验证 |
| 网络效应 | 高/中/低 | - | XXX | 未验证 |
| 品牌认知 | 高/中/低 | X 年 | XXX | 未验证 |
| 转换成本 | 高/中/低 | - | XXX | 未验证 |
| 规模优势 | 高/中/低 | X 年 | XXX | 未验证 |

**护城河综合评估**: 🟢 宽护城河 / 🟡 中等 / 🔴 窄护城河

---

### 12 个月后理想护城河

| 目标护城河 | 当前状态 | 目标状态 | 建设路径 | 所需投入 |
|-----------|---------|---------|---------|---------|
| XXX | ⚪⚪⚪⚪⚪ | ⚪⚪⚪⚪⚪ | XXX | XXX 万 |

---

### 被复制风险评估

#### 最可能被复制的部分
1. **XXX**（原因：XXX）
   - 预计被复制时间：X 个月
   - 应对策略：XXX

#### 最难被复制的部分
1. **XXX**（原因：XXX）
   - 可持续性：X 年
   - 加强策略：XXX

---

### 竞争响应预案

| 竞争动作 | 概率 | 我们的响应 | 响应时间 |
|---------|------|-----------|---------|
| 竞品降价 XX% | 高/中/低 | XXX | X 周内 |
| 竞品推出类似功能 | 高/中/低 | XXX | X 周内 |
"""

    def generate_roi_estimate(self) -> str:
        """
        生成投入产出估算（资本分配意识）
        
        基于价值主张，估算实现所需的投入和预期回报。
        """
        return f"""
## 投入产出估算

---

### 实现投入估算

#### 产品开发投入
| 项目 | 工时 | 成本 (万) | 说明 |
|------|------|----------|------|
| 核心功能开发 | X 人月 | XXX | XXX |
| 用户体验设计 | X 人月 | XXX | XXX |
| 测试与优化 | X 人月 | XXX | XXX |
| **小计** | **X 人月** | **XXX** | - |

#### 市场获客投入
| 渠道 | 预算 (万) | 预计获客 | 预计 CAC |
|------|----------|---------|---------|
| 内容营销 | XXX | XXX 人 | XXX 元 |
| 付费广告 | XXX | XXX 人 | XXX 元 |
| **小计** | **XXX** | **XXX 人** | **XXX 元** |

**总投入估算**: XXX 万（12 个月）

---

### 预期回报估算

#### 收入预测（3 年）
| 年份 | 用户数 | 收入 (万) | 毛利率 | 净利润 |
|------|--------|----------|--------|--------|
| 第 1 年 | XXX | XXX | XX% | -XXX |
| 第 2 年 | XXX | XXX | XX% | XXX |
| 第 3 年 | XXX | XXX | XX% | XXX |

#### 关键财务指标
| 指标 | 估算值 | 健康标准 | 评估 |
|------|--------|---------|------|
| 盈亏平衡点 | 第 X 个月 | < 18 个月 | 🟢/🟡/🔴 |
| 投资回收期 | X 个月 | < 24 个月 | 🟢/🟡/🔴 |
| 3 年 ROI | XXX% | > 100% | 🟢/🟡/🔴 |

---

### 敏感性分析

| 变量 | 悲观情景 | 基准情景 | 乐观情景 |
|------|---------|---------|---------|
| 获客成本 | XXX 元 (+XX%) | XXX 元 | XXX 元 (-XX%) |
| 用户留存 | X 个月 (-XX%) | X 个月 | X 个月 (+XX%) |
| 客单价 | XXX 元 (-XX%) | XXX 元 | XXX 元 (+XX%) |
| **3 年 ROI** | **XX%** | **XXX%** | **XXX%** |
"""

    def generate_canvas(self, include_ceo_analysis: bool = True) -> str:
        """
        生成价值主张画布（含 CEO 决策模块）
        
        Args:
            include_ceo_analysis: 是否包含 CEO 视角扩展分析（默认 True）
        """
        canvas = self.canvas.render_markdown()
        
        if include_ceo_analysis:
            commercialization = self.generate_commercialization_path()
            moat = self.generate_competitive_moat()
            roi = self.generate_roi_estimate()
            return f"{canvas}\n\n---\n\n## CEO 视角扩展分析\n\n{commercialization}\n\n---\n\n{moat}\n\n---\n\n{roi}"
        else:
            return canvas

    def render_all(self) -> str:
        if not self._sections:
            return f"# {self.business_scenario} - {self.target_customer}\n\n尚未执行任何模块，请先调用 generate_interview / generate_survey / calculate_priority 等方法。"
        section_order = ["interview", "survey", "priority", "canvas", "competitor", "experiment", "sample"]
        parts = [
            f"# {self.business_scenario} - {self.target_customer} 价值主张设计全景报告",
            "",
            f"本报告包含 {len(self._sections)} 个分析模块的完整输出。",
            "",
            "---",
        ]
        for key in section_order:
            if key in self._sections:
                parts.append("")
                parts.append(self._sections[key])
                parts.append("")
                parts.append("---")
        return "\n".join(parts)

    def summary(self) -> dict:
        result = {
            "business_scenario": self.business_scenario,
            "target_customer": self.target_customer,
            "modules_executed": list(self._sections.keys()),
            "modules_count": len(self._sections),
        }
        if "priority" in self._sections:
            ranked = self.priority.rank()
            if ranked:
                result["top_priority"] = ranked[0]["name"]
                result["priority_items_count"] = len(ranked)
        if "canvas" in self._sections:
            fit = self.canvas.analyze_fit()
            result["canvas_fit_score"] = fit["overall_score"]
            result["canvas_fit_level"] = fit["fit_level"]
        if "competitor" in self._sections and self.competitor.factors:
            result["competitor_factors_count"] = len(self.competitor.factors)
            result["competitor_players_count"] = len(self.competitor.players)
        if "experiment" in self._sections:
            result["hypotheses_count"] = len(self.experiment.hypotheses)
            result["test_cards_count"] = len(self.experiment.test_cards)
        return result


__all__ = [
    "VPDSkill",
    "InterviewGenerator", "InterviewConfig",
    "SurveyDesigner", "SurveyConfig", "SurveyHypothesis",
    "PriorityCalculator", "PriorityItem",
    "CanvasAnalyzer", "Job", "Pain", "Gain", "Product", "PainReliever", "GainCreator",
    "StrategyScorer",
    "SampleCalculator",
    "ExperimentDesigner", "Hypothesis", "TestCard", "LearningCard",
]
