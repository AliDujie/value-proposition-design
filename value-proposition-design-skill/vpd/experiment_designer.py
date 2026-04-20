from dataclasses import dataclass, field
from vpd.utils import load_config


@dataclass
class Hypothesis:
    description: str
    hypothesis_type: str = "value_proposition"
    lethality: str = "lethal"
    evidence_strength: str = "none"

    def validate(self) -> None:
        valid_types = ["customer_profile", "value_proposition", "business_model"]
        if self.hypothesis_type not in valid_types:
            raise ValueError(f"hypothesis_type must be one of {valid_types}")
        valid_lethality = ["lethal", "important", "auxiliary"]
        if self.lethality not in valid_lethality:
            raise ValueError(f"lethality must be one of {valid_lethality}")
        valid_evidence = ["none", "weak", "medium", "strong"]
        if self.evidence_strength not in valid_evidence:
            raise ValueError(f"evidence_strength must be one of {valid_evidence}")


@dataclass
class TestCard:
    hypothesis: str
    test_method: str
    metric: str
    threshold: str
    falsification: str
    cta_level: str = "L2"
    duration_days: int = 14
    sample_size: int = 50


@dataclass
class LearningCard:
    hypothesis: str
    observed_result: str
    metric_actual: str
    metric_target: str
    validated: bool = False
    next_action: str = ""
    surprises: str = ""


EXPERIMENT_METHODS = [
    {"name": "客户访谈", "scenario": "探索工作/痛点/收益", "cost": "低", "duration": "1-2周", "evidence": "中"},
    {"name": "广告跟踪", "scenario": "测试市场兴趣", "cost": "低", "duration": "1-2周", "evidence": "中"},
    {"name": "登录页MVP", "scenario": "测试价值主张吸引力", "cost": "低", "duration": "1-2周", "evidence": "中高"},
    {"name": "A/B测试", "scenario": "比较方案优劣", "cost": "中", "duration": "2-4周", "evidence": "高"},
    {"name": "创新游戏", "scenario": "发现优先级和偏好", "cost": "低", "duration": "1天", "evidence": "中"},
    {"name": "模拟销售", "scenario": "测试购买意愿", "cost": "中", "duration": "2-4周", "evidence": "高"},
    {"name": "预售/众筹", "scenario": "测试真实付费意愿", "cost": "中", "duration": "4-8周", "evidence": "很高"},
    {"name": "真实MVP", "scenario": "测试产品-市场契合", "cost": "高", "duration": "4-12周", "evidence": "很高"},
]


class ExperimentDesigner:

    def __init__(self, config_path: str = ""):
        cfg = load_config(config_path)
        self._exp_cfg = cfg.get("experiment", {})
        self._cta_levels = self._exp_cfg.get("cta_levels", {})
        self._readiness = self._exp_cfg.get("investment_readiness", {}).get("levels", {})
        self.hypotheses: list[Hypothesis] = []
        self.test_cards: list[TestCard] = []
        self.learning_cards: list[LearningCard] = []

    def add_hypothesis(self, description: str, hypothesis_type: str = "value_proposition",
                       lethality: str = "lethal", evidence_strength: str = "none") -> Hypothesis:
        h = Hypothesis(description=description, hypothesis_type=hypothesis_type,
                       lethality=lethality, evidence_strength=evidence_strength)
        h.validate()
        self.hypotheses.append(h)
        return h

    def rank_hypotheses(self) -> list[dict]:
        lethality_order = {"lethal": 0, "important": 1, "auxiliary": 2}
        evidence_order = {"none": 0, "weak": 1, "medium": 2, "strong": 3}
        sorted_h = sorted(self.hypotheses, key=lambda h: (lethality_order.get(h.lethality, 9), evidence_order.get(h.evidence_strength, 9)))
        results = []
        for i, h in enumerate(sorted_h, 1):
            lethality_label = {"lethal": "🔴 致命", "important": "🟡 重要", "auxiliary": "🟢 一般"}.get(h.lethality, h.lethality)
            results.append({"priority": i, "description": h.description, "type": h.hypothesis_type,
                            "lethality": lethality_label, "evidence": h.evidence_strength})
        return results

    def create_test_card(self, hypothesis: str, test_method: str, metric: str,
                         threshold: str, falsification: str, cta_level: str = "L2",
                         duration_days: int = 14, sample_size: int = 50) -> TestCard:
        tc = TestCard(hypothesis=hypothesis, test_method=test_method, metric=metric,
                      threshold=threshold, falsification=falsification, cta_level=cta_level,
                      duration_days=duration_days, sample_size=sample_size)
        self.test_cards.append(tc)
        return tc

    def create_learning_card(self, hypothesis: str, observed_result: str,
                             metric_actual: str, metric_target: str,
                             validated: bool = False, next_action: str = "",
                             surprises: str = "") -> LearningCard:
        lc = LearningCard(hypothesis=hypothesis, observed_result=observed_result,
                          metric_actual=metric_actual, metric_target=metric_target,
                          validated=validated, next_action=next_action, surprises=surprises)
        self.learning_cards.append(lc)
        return lc

    def suggest_method(self, budget: str = "low", stage: str = "exploration") -> list[dict]:
        cost_filter = {"low": ["低"], "medium": ["低", "中"], "high": ["低", "中", "高"]}.get(budget, ["低", "中", "高"])
        return [m for m in EXPERIMENT_METHODS if m["cost"] in cost_filter]

    def investment_readiness_level(self, validated_count: int, total_count: int) -> dict:
        if total_count == 0:
            ratio = 0.0
        else:
            ratio = validated_count / total_count
        if ratio >= 0.9:
            level = 7
        elif ratio >= 0.7:
            level = 5
        elif ratio >= 0.5:
            level = 3
        elif ratio >= 0.2:
            level = 2
        else:
            level = 1
        return {"level": level, "description": self._readiness.get(level, ""),
                "validated_ratio": round(ratio * 100, 1)}

    def render_markdown(self) -> str:
        lines = ["# 实验设计方案", ""]
        ranked = self.rank_hypotheses()
        if ranked:
            lines.extend(["## 假设排序（按致命性优先）", "",
                          "| 优先级 | 假设描述 | 类型 | 致命性 | 当前证据 |",
                          "|:-----:|---------|------|:------:|:------:|"])
            for r in ranked:
                lines.append(f"| {r['priority']} | {r['description']} | {r['type']} | {r['lethality']} | {r['evidence']} |")

        for i, tc in enumerate(self.test_cards, 1):
            cta_info = self._cta_levels.get(tc.cta_level, {})
            cta_label = cta_info.get("label", tc.cta_level)
            lines.extend(["", f"## 测试卡 #{i}", "",
                          f"**假设**：{tc.hypothesis}", "",
                          f"**验证标准**：{tc.metric} ≥ {tc.threshold}", "",
                          f"**否定标准**：{tc.falsification}", "",
                          f"**实验方法**：{tc.test_method}", "",
                          f"**CTA层级**：{tc.cta_level} - {cta_label}", "",
                          f"**样本量**：{tc.sample_size}人", "",
                          f"**实验周期**：{tc.duration_days}天"])

        for i, lc in enumerate(self.learning_cards, 1):
            status = "✅ 假设被验证" if lc.validated else "❌ 假设被否定"
            lines.extend(["", f"## 学习卡 #{i}", "",
                          f"**假设**：{lc.hypothesis}", "",
                          f"**观察结果**：{lc.observed_result}", "",
                          f"**指标**：实际 {lc.metric_actual}（目标 ≥ {lc.metric_target}）", "",
                          f"**结论**：{status}", "",
                          f"**下一步**：{lc.next_action}"])
            if lc.surprises:
                lines.append(f"**意外发现**：{lc.surprises}")

        return "\n".join(lines)
