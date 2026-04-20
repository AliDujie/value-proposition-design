from dataclasses import dataclass, field
from vpd.sample_calculator import SampleCalculator


@dataclass
class SurveyHypothesis:
    description: str
    category: str = "customer_profile"

    def validate(self) -> None:
        valid = ["customer_profile", "value_proposition", "satisfaction"]
        if self.category not in valid:
            raise ValueError(f"category must be one of {valid}, got {self.category}")


@dataclass
class SurveyConfig:
    business_scenario: str
    target_customer: str
    hypotheses: list[SurveyHypothesis] = field(default_factory=list)
    survey_type: str = "客户概况验证"
    target_sample_size: int = 200
    channel: str = "线上"

    def validate(self) -> None:
        if not self.business_scenario:
            raise ValueError("business_scenario is required")
        if not self.target_customer:
            raise ValueError("target_customer is required")
        if not self.hypotheses:
            raise ValueError("at least one hypothesis is required")
        valid_types = ["客户概况验证", "价值主张验证", "满意度评估"]
        if self.survey_type not in valid_types:
            raise ValueError(f"survey_type must be one of {valid_types}, got {self.survey_type}")
        valid_channels = ["线上", "线下", "混合"]
        if self.channel not in valid_channels:
            raise ValueError(f"channel must be one of {valid_channels}, got {self.channel}")
        if self.target_sample_size < 10:
            raise ValueError(f"target_sample_size must be >= 10, got {self.target_sample_size}")
        for h in self.hypotheses:
            h.validate()


class SurveyDesigner:

    def __init__(self) -> None:
        self._config: SurveyConfig | None = None
        self._jobs: list[str] = []
        self._pains: list[str] = []
        self._gains: list[str] = []
        self._value_propositions: list[str] = []
        self._screening_criteria: list[str] = []
        self._alternatives: list[str] = []

    def configure(self, business_scenario: str, target_customer: str,
                  hypotheses: list[dict] | None = None,
                  survey_type: str = "客户概况验证",
                  target_sample_size: int = 200,
                  channel: str = "线上") -> SurveyConfig:
        hyps = []
        for h in (hypotheses or []):
            if isinstance(h, dict):
                hyps.append(SurveyHypothesis(
                    description=h.get("description", h.get("desc", "")),
                    category=h.get("category", "customer_profile"),
                ))
            elif isinstance(h, str):
                hyps.append(SurveyHypothesis(description=h))
            elif isinstance(h, SurveyHypothesis):
                hyps.append(h)
        cfg = SurveyConfig(
            business_scenario=business_scenario,
            target_customer=target_customer,
            hypotheses=hyps,
            survey_type=survey_type,
            target_sample_size=target_sample_size,
            channel=channel,
        )
        cfg.validate()
        self._config = cfg
        return cfg

    def set_jobs(self, jobs: list[str]) -> None:
        self._jobs = list(jobs)

    def set_pains(self, pains: list[str]) -> None:
        self._pains = list(pains)

    def set_gains(self, gains: list[str]) -> None:
        self._gains = list(gains)

    def set_value_propositions(self, vps: list[str]) -> None:
        self._value_propositions = list(vps)

    def set_screening_criteria(self, criteria: list[str]) -> None:
        self._screening_criteria = list(criteria)

    def set_alternatives(self, alternatives: list[str]) -> None:
        self._alternatives = list(alternatives)

    def _estimate_duration(self) -> int:
        q_count = self._estimate_question_count()
        return max(3, q_count // 2)

    def _estimate_question_count(self) -> int:
        count = 1
        count += max(2, len(self._jobs)) + 2
        count += max(2, len(self._pains)) + 2
        count += max(2, len(self._gains)) + 1
        if self._value_propositions:
            count += 2
        count += 3
        return count

    def _build_header(self) -> list[str]:
        cfg = self._config
        dur = self._estimate_duration()
        lines = [
            f"# {cfg.business_scenario} 用户调研问卷",
            "",
            f"问卷目标：验证{cfg.target_customer}在{cfg.business_scenario}中的工作、痛点和收益假设",
            f"目标样本量：{cfg.target_sample_size}份",
            f"预计填写时长：{dur}分钟",
            f"投放渠道：{cfg.channel}",
            f"问卷类型：{cfg.survey_type}",
            "",
        ]
        return lines

    def _build_screening(self) -> list[str]:
        cfg = self._config
        lines = [
            "---",
            "",
            "## Part 1：筛选题（1-2题）",
            "目的：确保受访者属于目标客户群",
            "",
        ]
        if self._screening_criteria:
            lines.append("Q1. 请问您是否符合以下条件？（单选）")
            for i, c in enumerate(self._screening_criteria):
                tag = "符合，继续" if i < len(self._screening_criteria) - 1 else "不符合，结束问卷"
                lines.append(f"□ {c}（{tag}）")
        else:
            lines.append(f"Q1. 您是否属于{cfg.target_customer}？（单选）")
            lines.append("□ 是（继续）")
            lines.append("□ 否（结束问卷）")
        lines.append("")
        return lines

    def _build_job_section(self, q_start: int) -> tuple[list[str], int]:
        cfg = self._config
        q = q_start
        lines = [
            "---",
            "",
            "## Part 2：客户工作重要性评估（3-5题）",
            "目的：验证哪些工作对客户最重要",
            "",
        ]
        jobs = self._jobs if self._jobs else [f"工作{i+1}" for i in range(3)]

        lines.append(f"Q{q}. 在{cfg.business_scenario}中，以下哪些事情是您需要完成的？（多选）")
        for j in jobs:
            lines.append(f"□ {j}")
        lines.append("□ 其他（请注明）____")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 请对以下工作按重要程度排序（1=最重要）：（排序题）")
        for j in jobs:
            lines.append(f"___ {j}")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 您完成最重要工作的频率是？（单选）")
        lines.append("□ 每天")
        lines.append("□ 每周2-3次")
        lines.append("□ 每周1次")
        lines.append("□ 每月2-3次")
        lines.append("□ 每月1次或更少")
        lines.append("")
        q += 1

        return lines, q

    def _build_pain_section(self, q_start: int) -> tuple[list[str], int]:
        q = q_start
        lines = [
            "---",
            "",
            "## Part 3：痛点严重度评估（4-6题）",
            "目的：量化各痛点的严重程度",
            "量表说明：使用5点李克特量表（1=完全不同意，5=完全同意）",
            "",
        ]
        pains = self._pains if self._pains else [f"痛点{i+1}" for i in range(3)]

        lines.append(f"Q{q}. 请评价以下问题对您的困扰程度：（矩阵量表题）")
        lines.append("")
        lines.append("| 痛点描述 | 1完全不困扰 | 2较少困扰 | 3一般 | 4比较困扰 | 5非常困扰 |")
        lines.append("|---------|:---------:|:-------:|:----:|:-------:|:-------:|")
        for p in pains:
            lines.append(f"| {p} | ○ | ○ | ○ | ○ | ○ |")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 在以上问题中，哪一个最让您难以忍受？（单选）")
        for p in pains:
            lines.append(f"□ {p}")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 您目前如何应对最严重的痛点？（单选）")
        lines.append("□ 忍受，没有好的替代方案")
        if self._alternatives:
            for alt in self._alternatives:
                lines.append(f"□ 使用{alt}")
        else:
            lines.append("□ 使用替代方案A")
            lines.append("□ 使用替代方案B")
        lines.append("□ 已经放弃这项工作")
        lines.append("□ 其他____")
        lines.append("")
        q += 1

        return lines, q

    def _build_gain_section(self, q_start: int) -> tuple[list[str], int]:
        cfg = self._config
        q = q_start
        lines = [
            "---",
            "",
            "## Part 4：收益期望评估（3-5题）",
            "目的：了解客户期望的结果和愿意付出的代价",
            "",
        ]
        gains = self._gains if self._gains else [f"收益{i+1}" for i in range(3)]

        lines.append(f"Q{q}. 如果{cfg.business_scenario}能得到改善，以下哪些结果对您最有价值？（最多选3项）")
        for g in gains:
            lines.append(f"□ {g}")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 您愿意为最重要的收益额外付费吗？（单选）")
        lines.append("□ 愿意，可以多付10%以内")
        lines.append("□ 愿意，但涨幅不能超过20%")
        lines.append("□ 不愿意额外付费")
        lines.append("□ 看具体方案再决定")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 请评价以下改善对您的吸引力：（矩阵量表题）")
        lines.append("")
        lines.append("| 收益描述 | 1完全没吸引力 | 2吸引力较小 | 3一般 | 4比较有吸引力 | 5非常有吸引力 |")
        lines.append("|---------|:----------:|:---------:|:----:|:----------:|:----------:|")
        for g in gains:
            lines.append(f"| {g} | ○ | ○ | ○ | ○ | ○ |")
        lines.append("")
        q += 1

        return lines, q

    def _build_vp_section(self, q_start: int) -> tuple[list[str], int]:
        if not self._value_propositions:
            return [], q_start
        q = q_start
        lines = [
            "---",
            "",
            "## Part 5：价值主张验证（2-3题）",
            "目的：测试具体价值主张方案的吸引力",
            "",
        ]
        vp_desc = self._value_propositions[0] if self._value_propositions else "核心价值"
        lines.append(f"Q{q}. 如果有一个产品/服务能{vp_desc}，您有多大可能会使用？（单选）")
        lines.append("□ 一定会用（9-10分）")
        lines.append("□ 很可能会用（7-8分）")
        lines.append("□ 可能会用（5-6分）")
        lines.append("□ 不太可能用（3-4分）")
        lines.append("□ 一定不会用（1-2分）")
        lines.append("")
        q += 1

        if len(self._value_propositions) >= 2:
            lines.append(f"Q{q}. 以下哪个方案最吸引您？（单选，用于A/B测试）")
            for i, vp in enumerate(self._value_propositions):
                lines.append(f"□ 方案{chr(65+i)}：{vp}")
            lines.append("□ 都不吸引我")
            lines.append("")
            q += 1

        return lines, q

    def _build_demographics(self, q_start: int) -> tuple[list[str], int]:
        cfg = self._config
        q = q_start
        lines = [
            "---",
            "",
            "## Part 6：人口统计学信息（2-3题）",
            "",
        ]
        lines.append(f"Q{q}. 您的年龄段：（单选）")
        lines.append("□ 18岁以下  □ 18-24岁  □ 25-34岁  □ 35-44岁  □ 45-54岁  □ 55岁以上")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 您的职业：（单选）")
        lines.append("□ 企业员工  □ 自由职业  □ 学生  □ 公务员/事业单位  □ 企业主  □ 其他____")
        lines.append("")
        q += 1

        lines.append(f"Q{q}. 您在{cfg.business_scenario}上的月均消费：（单选）")
        lines.append("□ 100元以下  □ 100-500元  □ 500-1000元  □ 1000-3000元  □ 3000元以上")
        lines.append("")
        q += 1

        return lines, q

    def _build_analysis_suggestions(self) -> list[str]:
        sc = SampleCalculator()
        sample_info = sc.minimum_sample_size(confidence=95, margin_of_error=0.05)
        lines = [
            "---",
            "",
            "## 数据分析建议",
            "",
            "### 分析方向",
            "- 各痛点的均值排序→确定痛点优先级",
            "- 工作重要性排序→确定关注的核心工作",
            "- 收益吸引力均值→确定价值主张方向",
            "- 交叉分析建议（如不同客户群的痛点差异）",
            "",
            "### 统计显著性要求",
            f"- 95%置信度下的最小样本量：{sample_info['sample_size']}份",
            f"- 误差范围：±{sample_info['margin_of_error'] * 100}%",
            "",
            "### 假设验证对照表",
            "",
            "| 假设 | 对应题目 | 验证标准 | 结果 |",
            "|------|---------|---------|------|",
        ]
        for i, h in enumerate(self._config.hypotheses):
            lines.append(f"| {h.description} | Q相关 | 均值≥4或占比≥60% | 待填写 |")
        lines.append("")
        return lines

    def generate(self) -> dict:
        if self._config is None:
            raise ValueError("please call configure() first")
        cfg = self._config
        q_count = self._estimate_question_count()
        sc = SampleCalculator()
        sample_info = sc.minimum_sample_size(confidence=95, margin_of_error=0.05)
        return {
            "business_scenario": cfg.business_scenario,
            "target_customer": cfg.target_customer,
            "survey_type": cfg.survey_type,
            "target_sample_size": cfg.target_sample_size,
            "channel": cfg.channel,
            "hypotheses_count": len(cfg.hypotheses),
            "estimated_questions": q_count,
            "estimated_duration_minutes": self._estimate_duration(),
            "min_sample_size_95": sample_info["sample_size"],
            "has_value_propositions": len(self._value_propositions) > 0,
            "parts": ["筛选题", "客户工作重要性评估", "痛点严重度评估", "收益期望评估"]
                     + (["价值主张验证"] if self._value_propositions else [])
                     + ["人口统计学信息"],
        }

    def render_markdown(self) -> str:
        if self._config is None:
            raise ValueError("please call configure() first")

        lines = self._build_header()
        lines.extend(self._build_screening())

        q = 2
        job_lines, q = self._build_job_section(q)
        lines.extend(job_lines)

        pain_lines, q = self._build_pain_section(q)
        lines.extend(pain_lines)

        gain_lines, q = self._build_gain_section(q)
        lines.extend(gain_lines)

        vp_lines, q = self._build_vp_section(q)
        lines.extend(vp_lines)

        demo_lines, q = self._build_demographics(q)
        lines.extend(demo_lines)

        lines.extend(self._build_analysis_suggestions())

        return "\n".join(lines)
