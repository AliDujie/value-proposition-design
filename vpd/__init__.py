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

    def render_all(self) -> str:
        if not self._sections:
            return f"# {self.business_scenario} - {self.target_customer}\n\n尚未执行任何模块，请先调用 generate_interview / generate_survey / calculate_priority 等方法。"
        section_titles = {
            "interview": "访谈提纲",
            "survey": "调研问卷",
            "priority": "优先级矩阵",
            "canvas": "价值主张画布",
            "competitor": "竞争战略分析",
            "experiment": "实验设计方案",
            "sample": "样本量计算",
        }
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
