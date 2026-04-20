from dataclasses import dataclass, field
from typing import Optional
from vpd.utils import load_config


@dataclass
class PriorityItem:
    name: str
    importance: int
    dissatisfaction: int
    frequency: int
    viability: int
    competition_coverage: Optional[str] = None

    @property
    def raw_score(self) -> float:
        return self.importance * self.dissatisfaction * self.frequency * self.viability

    @property
    def normalized_score(self) -> float:
        return self.raw_score / 625.0 * 100.0

    def final_score(self, coverage_multipliers: dict) -> float:
        multiplier = 1.0
        if self.competition_coverage and self.competition_coverage in coverage_multipliers:
            multiplier = coverage_multipliers[self.competition_coverage]
        return self.normalized_score * multiplier

    def grade(self, thresholds: dict, coverage_multipliers: dict) -> str:
        score = self.final_score(coverage_multipliers)
        for level in ["P0", "P1", "P2", "P3"]:
            if score >= thresholds.get(level, 0):
                return level
        return "P3"


class PriorityCalculator:

    def __init__(self, config_path: str = ""):
        cfg = load_config(config_path)
        self._priority_cfg = cfg.get("priority", {})
        self._dimensions = self._priority_cfg.get("dimensions", {})
        self._thresholds = self._priority_cfg.get("grade_thresholds", {"P0": 60, "P1": 30, "P2": 15, "P3": 0})
        self._coverage = self._priority_cfg.get("competition_coverage", {"not_covered": 1.5, "partially_covered": 1.0, "fully_covered": 0.5})
        self._items: list[PriorityItem] = []

    @property
    def dimension_anchors(self) -> dict:
        return {k: v.get("anchors", {}) for k, v in self._dimensions.items()}

    def add_item(self, name: str, importance: int, dissatisfaction: int, frequency: int, viability: int, competition_coverage: Optional[str] = None) -> PriorityItem:
        for val, label in [(importance, "importance"), (dissatisfaction, "dissatisfaction"), (frequency, "frequency"), (viability, "viability")]:
            if not 1 <= val <= 5:
                raise ValueError(f"{label} must be between 1 and 5, got {val}")
        item = PriorityItem(name=name, importance=importance, dissatisfaction=dissatisfaction, frequency=frequency, viability=viability, competition_coverage=competition_coverage)
        self._items.append(item)
        return item

    def clear(self) -> None:
        self._items.clear()

    def rank(self) -> list[dict]:
        ranked = sorted(self._items, key=lambda x: x.final_score(self._coverage), reverse=True)
        results = []
        for idx, item in enumerate(ranked, 1):
            score = item.final_score(self._coverage)
            results.append({
                "rank": idx,
                "name": item.name,
                "importance": item.importance,
                "dissatisfaction": item.dissatisfaction,
                "frequency": item.frequency,
                "viability": item.viability,
                "competition_coverage": item.competition_coverage,
                "raw_score": item.raw_score,
                "normalized_score": round(item.normalized_score, 1),
                "final_score": round(score, 1),
                "grade": item.grade(self._thresholds, self._coverage),
            })
        return results

    def render_markdown(self, title: str = "优先级评估矩阵", evaluation_type: str = "痛点") -> str:
        ranked = self.rank()
        if not ranked:
            return f"# {title}\n\n暂无评估数据。"

        lines = [
            f"# {title}",
            "",
            f"评估日期：待填写",
            f"评估维度：{evaluation_type}",
            f"评估对象数量：{len(ranked)}项",
            "",
            "## 评分明细",
            "",
            f"| 排名 | 评估对象 | 重要性(I) | 不满意度(D) | 频率(F) | 可行性(V) | 差异化(C) | 最终得分 | 优先级 |",
            f"|:----:|---------|:---------:|:----------:|:------:|:--------:|:--------:|:------:|:-----:|",
        ]

        for r in ranked:
            cov = r["competition_coverage"] or "-"
            cov_label = {"not_covered": "1.5", "partially_covered": "1.0", "fully_covered": "0.5"}.get(cov, "-")
            lines.append(f"| {r['rank']} | {r['name']} | {r['importance']} | {r['dissatisfaction']} | {r['frequency']} | {r['viability']} | {cov_label} | {r['final_score']} | {r['grade']} |")

        lines.extend([
            "",
            "## 优先级分级标准",
            "",
            "| 等级 | 分数范围 | 建议行动 |",
            "|:----:|:-------:|---------|",
            f"| P0 | ≥{self._thresholds.get('P0', 60)}分 | 立即行动：这是核心机会，应最优先投入资源 |",
            f"| P1 | {self._thresholds.get('P2', 15)}-{self._thresholds.get('P0', 60) - 1}分 | 重点关注：纳入近期规划，分配专项资源 |",
            f"| P2 | {self._thresholds.get('P3', 0)}-{self._thresholds.get('P2', 15) - 1}分 | 持续观察：纳入中期规划，等待时机 |",
            f"| P3 | <{self._thresholds.get('P2', 15)}分 | 暂时搁置：当前不值得投入，定期重新评估 |",
        ])

        p0_items = [r for r in ranked if r["grade"] == "P0"]
        p1_items = [r for r in ranked if r["grade"] == "P1"]

        if p0_items or p1_items:
            lines.extend(["", "## 决策建议", ""])
            lines.append("### 核心发现")
            if p0_items:
                top_names = "、".join(r["name"] for r in p0_items[:3])
                lines.append(f"最高优先级项目：{top_names}，建议立即投入资源。")
            if p1_items:
                p1_names = "、".join(r["name"] for r in p1_items[:3])
                lines.append(f"重点关注项目：{p1_names}，建议纳入近期规划。")

        return "\n".join(lines)
