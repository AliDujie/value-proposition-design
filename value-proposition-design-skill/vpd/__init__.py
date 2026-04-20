"""
Value Proposition Design (VPD) - Python工具包

基于《价值主张设计》方法论的可执行计算工具，提供6大核心模块：
- InterviewGenerator: 访谈提纲生成器（五阶段结构，B2B/B2C，八大原则）
- SurveyDesigner: 问卷设计器（六Part结构，李克特量表，A/B测试）
- PriorityCalculator: 优先级计算（4维评分，P0-P3分级）
- CanvasAnalyzer: 价值主张画布分析（契合度诊断）
- StrategyScorer: 竞争战略画布（蓝海分析）
- SampleCalculator: 样本量计算（统计显著性）
- ExperimentDesigner: 实验设计（测试卡/学习卡）

用法示例:
    from vpd import InterviewGenerator
    ig = InterviewGenerator()
    ig.configure("飞猪国内酒店预订", "25-35岁商旅用户")
    print(ig.render_markdown())

    from vpd import PriorityCalculator
    calc = PriorityCalculator()
    calc.add_item("价格不透明", importance=5, dissatisfaction=5, frequency=4, viability=4)
    print(calc.render_markdown())
"""

from vpd.interview_generator import InterviewGenerator, InterviewConfig
from vpd.survey_designer import SurveyDesigner, SurveyConfig, SurveyHypothesis
from vpd.priority_calculator import PriorityCalculator, PriorityItem
from vpd.canvas_analyzer import CanvasAnalyzer, Job, Pain, Gain, Product, PainReliever, GainCreator
from vpd.strategy_scorer import StrategyScorer
from vpd.sample_calculator import SampleCalculator
from vpd.experiment_designer import ExperimentDesigner, Hypothesis, TestCard, LearningCard

__all__ = [
    "InterviewGenerator", "InterviewConfig",
    "SurveyDesigner", "SurveyConfig", "SurveyHypothesis",
    "PriorityCalculator", "PriorityItem",
    "CanvasAnalyzer", "Job", "Pain", "Gain", "Product", "PainReliever", "GainCreator",
    "StrategyScorer",
    "SampleCalculator",
    "ExperimentDesigner", "Hypothesis", "TestCard", "LearningCard",
]
