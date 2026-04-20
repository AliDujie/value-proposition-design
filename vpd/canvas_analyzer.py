from dataclasses import dataclass, field
from typing import Optional
from vpd.utils import load_config


@dataclass
class Job:
    description: str
    category: str
    importance: int = 3

    def validate(self) -> None:
        valid = ["functional", "social", "emotional", "supporting"]
        if self.category not in valid:
            raise ValueError(f"category must be one of {valid}, got {self.category}")
        if not 1 <= self.importance <= 5:
            raise ValueError(f"importance must be 1-5, got {self.importance}")


@dataclass
class Pain:
    description: str
    severity: str
    quantified_metric: str = ""

    def validate(self) -> None:
        valid = ["critical", "severe", "moderate", "minor"]
        if self.severity not in valid:
            raise ValueError(f"severity must be one of {valid}, got {self.severity}")


@dataclass
class Gain:
    description: str
    desire_level: str
    quantified_metric: str = ""

    def validate(self) -> None:
        valid = ["required", "expected", "desired", "unexpected"]
        if self.desire_level not in valid:
            raise ValueError(f"desire_level must be one of {valid}, got {self.desire_level}")


@dataclass
class Product:
    description: str
    category: str

    def validate(self) -> None:
        valid = ["tangible", "intangible", "digital", "financial"]
        if self.category not in valid:
            raise ValueError(f"category must be one of {valid}, got {self.category}")


@dataclass
class PainReliever:
    description: str
    target_pain: str
    coverage: str = "full"

    def validate(self) -> None:
        if self.coverage not in ["full", "partial", "none"]:
            raise ValueError(f"coverage must be full/partial/none, got {self.coverage}")


@dataclass
class GainCreator:
    description: str
    target_gain: str
    coverage: str = "full"

    def validate(self) -> None:
        if self.coverage not in ["full", "partial", "none"]:
            raise ValueError(f"coverage must be full/partial/none, got {self.coverage}")


class CanvasAnalyzer:

    def __init__(self, config_path: str = ""):
        cfg = load_config(config_path)
        self._canvas_cfg = cfg.get("canvas", {})
        self._thresholds = self._canvas_cfg.get("fit_thresholds", {"excellent": 80, "good": 60, "fair": 40, "poor": 0})
        self.customer_name: str = ""
        self.product_name: str = ""
        self.jobs: list[Job] = []
        self.pains: list[Pain] = []
        self.gains: list[Gain] = []
        self.products: list[Product] = []
        self.pain_relievers: list[PainReliever] = []
        self.gain_creators: list[GainCreator] = []

    def add_job(self, description: str, category: str, importance: int = 3) -> Job:
        job = Job(description=description, category=category, importance=importance)
        job.validate()
        self.jobs.append(job)
        return job

    def add_pain(self, description: str, severity: str, quantified_metric: str = "") -> Pain:
        pain = Pain(description=description, severity=severity, quantified_metric=quantified_metric)
        pain.validate()
        self.pains.append(pain)
        return pain

    def add_gain(self, description: str, desire_level: str, quantified_metric: str = "") -> Gain:
        gain = Gain(description=description, desire_level=desire_level, quantified_metric=quantified_metric)
        gain.validate()
        self.gains.append(gain)
        return gain

    def add_product(self, description: str, category: str) -> Product:
        product = Product(description=description, category=category)
        product.validate()
        self.products.append(product)
        return product

    def add_pain_reliever(self, description: str, target_pain: str, coverage: str = "full") -> PainReliever:
        pr = PainReliever(description=description, target_pain=target_pain, coverage=coverage)
        pr.validate()
        self.pain_relievers.append(pr)
        return pr

    def add_gain_creator(self, description: str, target_gain: str, coverage: str = "full") -> GainCreator:
        gc = GainCreator(description=description, target_gain=target_gain, coverage=coverage)
        gc.validate()
        self.gain_creators.append(gc)
        return gc

    def _match_pains(self) -> dict:
        pain_descs = {p.description for p in self.pains}
        relieved_targets = {}
        for pr in self.pain_relievers:
            relieved_targets[pr.target_pain] = pr.coverage

        full, partial, uncovered = 0, 0, 0
        details = []
        for pain in self.pains:
            cov = relieved_targets.get(pain.description, "none")
            if cov == "full":
                full += 1
                details.append({"pain": pain.description, "severity": pain.severity, "status": "🟢 完全覆盖"})
            elif cov == "partial":
                partial += 1
                details.append({"pain": pain.description, "severity": pain.severity, "status": "🟡 部分覆盖"})
            else:
                uncovered += 1
                details.append({"pain": pain.description, "severity": pain.severity, "status": "🔴 未覆盖"})

        total = len(self.pains) or 1
        rate = (full + partial * 0.5) / total * 100
        return {"full": full, "partial": partial, "uncovered": uncovered, "coverage_rate": round(rate, 1), "details": details}

    def _match_gains(self) -> dict:
        created_targets = {}
        for gc in self.gain_creators:
            created_targets[gc.target_gain] = gc.coverage

        full, partial, uncovered = 0, 0, 0
        details = []
        for gain in self.gains:
            cov = created_targets.get(gain.description, "none")
            if cov == "full":
                full += 1
                details.append({"gain": gain.description, "desire_level": gain.desire_level, "status": "🟢 完全覆盖"})
            elif cov == "partial":
                partial += 1
                details.append({"gain": gain.description, "desire_level": gain.desire_level, "status": "🟡 部分覆盖"})
            else:
                uncovered += 1
                details.append({"gain": gain.description, "desire_level": gain.desire_level, "status": "🔴 未覆盖"})

        total = len(self.gains) or 1
        rate = (full + partial * 0.5) / total * 100
        return {"full": full, "partial": partial, "uncovered": uncovered, "coverage_rate": round(rate, 1), "details": details}

    def analyze_fit(self) -> dict:
        pain_match = self._match_pains()
        gain_match = self._match_gains()

        job_count = len(self.jobs)
        pain_count = len(self.pains)
        gain_count = len(self.gains)
        product_count = len(self.products)
        pr_count = len(self.pain_relievers)
        gc_count = len(self.gain_creators)

        overall = (pain_match["coverage_rate"] + gain_match["coverage_rate"]) / 2.0

        if overall >= self._thresholds["excellent"]:
            fit_level = "优秀"
        elif overall >= self._thresholds["good"]:
            fit_level = "良好"
        elif overall >= self._thresholds["fair"]:
            fit_level = "一般"
        else:
            fit_level = "不足"

        has_problem_solution = pain_count > 0 and pr_count > 0 and pain_match["coverage_rate"] >= 50
        has_product_market = has_problem_solution and overall >= 60

        critical_uncovered = [d for d in pain_match["details"] if d["status"] == "🔴 未覆盖" and d["severity"] in ("critical", "severe")]
        required_uncovered = [d for d in gain_match["details"] if d["status"] == "🔴 未覆盖" and d["desire_level"] == "required"]

        gaps = []
        for cp in critical_uncovered:
            gaps.append(f"🔴 严重痛点未覆盖：{cp['pain']}")
        for rg in required_uncovered:
            gaps.append(f"🔴 必需收益未覆盖：{rg['gain']}")

        return {
            "overall_score": round(overall, 1),
            "fit_level": fit_level,
            "pain_coverage": pain_match,
            "gain_coverage": gain_match,
            "customer_profile_count": {"jobs": job_count, "pains": pain_count, "gains": gain_count},
            "value_map_count": {"products": product_count, "pain_relievers": pr_count, "gain_creators": gc_count},
            "fit_types": {
                "problem_solution": has_problem_solution,
                "product_market": has_product_market,
            },
            "critical_gaps": gaps,
        }

    def render_markdown(self) -> str:
        fit = self.analyze_fit()
        lines = [
            f"# 价值主张画布分析报告",
            "",
            f"客户群：{self.customer_name or '待填写'}",
            f"产品/服务：{self.product_name or '待填写'}",
            "",
            f"## 整体契合度评分：{fit['overall_score']}/100 ({fit['fit_level']})",
            "",
        ]

        lines.extend([
            "## 客户概况（Customer Profile）",
            "",
            f"### 客户工作（Jobs to be Done）：{fit['customer_profile_count']['jobs']}项",
            "",
        ])
        cat_labels = self._canvas_cfg.get("customer_profile", {}).get("jobs", {}).get("labels", {})
        for job in self.jobs:
            label = cat_labels.get(job.category, job.category)
            stars = "⭐" * job.importance
            lines.append(f"- {stars} [{label}] {job.description}")

        lines.extend(["", f"### 客户痛点（Pains）：{fit['customer_profile_count']['pains']}项", ""])
        sev_labels = self._canvas_cfg.get("customer_profile", {}).get("pains", {}).get("labels", {})
        for pain in self.pains:
            label = sev_labels.get(pain.severity, pain.severity)
            metric = f" | 量化指标：{pain.quantified_metric}" if pain.quantified_metric else ""
            lines.append(f"- {label} | {pain.description}{metric}")

        lines.extend(["", f"### 客户收益（Gains）：{fit['customer_profile_count']['gains']}项", ""])
        des_labels = self._canvas_cfg.get("customer_profile", {}).get("gains", {}).get("labels", {})
        for gain in self.gains:
            label = des_labels.get(gain.desire_level, gain.desire_level)
            metric = f" | 量化指标：{gain.quantified_metric}" if gain.quantified_metric else ""
            lines.append(f"- [{label}] {gain.description}{metric}")

        lines.extend(["", "---", "", "## 价值图（Value Map）", ""])
        lines.append(f"### 产品和服务：{fit['value_map_count']['products']}项")
        lines.append("")
        prod_labels = self._canvas_cfg.get("value_map", {}).get("products", {}).get("labels", {})
        for prod in self.products:
            label = prod_labels.get(prod.category, prod.category)
            lines.append(f"- [{label}] {prod.description}")

        lines.extend(["", f"### 痛点缓释方案：{fit['value_map_count']['pain_relievers']}项", ""])
        pc = fit["pain_coverage"]
        lines.append(f"| 客户痛点 | 严重度 | 覆盖状态 |")
        lines.append(f"|---------|:------:|:------:|")
        for d in pc["details"]:
            lines.append(f"| {d['pain']} | {d['severity']} | {d['status']} |")

        lines.extend(["", f"### 收益创造方案：{fit['value_map_count']['gain_creators']}项", ""])
        gc = fit["gain_coverage"]
        lines.append(f"| 客户收益 | 期望层级 | 覆盖状态 |")
        lines.append(f"|---------|:------:|:------:|")
        for d in gc["details"]:
            lines.append(f"| {d['gain']} | {d['desire_level']} | {d['status']} |")

        lines.extend([
            "",
            "---",
            "",
            "## 契合度明细",
            "",
            f"| 维度 | 客户侧条目数 | 已覆盖 | 部分覆盖 | 未覆盖 | 覆盖率 |",
            f"|------|:---------:|:-----:|:------:|:-----:|:-----:|",
            f"| 核心痛点 | {len(self.pains)} | {pc['full']} | {pc['partial']} | {pc['uncovered']} | {pc['coverage_rate']}% |",
            f"| 期望收益 | {len(self.gains)} | {gc['full']} | {gc['partial']} | {gc['uncovered']} | {gc['coverage_rate']}% |",
            "",
        ])

        lines.extend([
            "## 契合类型判断",
            "",
            f"- [{'x' if fit['fit_types']['problem_solution'] else ' '}] 问题-方案契合：是否有依据表明理解了客户的工作/痛点/收益？",
            f"- [{'x' if fit['fit_types']['product_market'] else ' '}] 产品-市场契合：是否有证据表明产品真正创造了客户价值？",
            "",
        ])

        if fit["critical_gaps"]:
            lines.extend(["## 关键缺口（Gap Analysis）", ""])
            for gap in fit["critical_gaps"]:
                lines.append(gap)
            lines.append("")

        lines.extend([
            "## 优化建议",
            "",
            f"基于缺口分析，给出3-5条具体的价值主张优化方向建议，按优先级排序。",
        ])

        return "\n".join(lines)
