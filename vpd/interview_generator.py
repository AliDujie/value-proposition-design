from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class InterviewConfig:
    business_scenario: str
    target_customer: str
    known_hypotheses: list[str] = field(default_factory=list)
    duration_minutes: int = 45
    customer_type: str = "B2C"
    stage: str = "探索期"

    def validate(self) -> None:
        if not self.business_scenario:
            raise ValueError("business_scenario is required")
        if not self.target_customer:
            raise ValueError("target_customer is required")
        valid_types = ["B2B", "B2C"]
        if self.customer_type not in valid_types:
            raise ValueError(f"customer_type must be one of {valid_types}, got {self.customer_type}")
        valid_stages = ["探索期", "验证期", "优化期"]
        if self.stage not in valid_stages:
            raise ValueError(f"stage must be one of {valid_stages}, got {self.stage}")
        if self.duration_minutes < 15 or self.duration_minutes > 120:
            raise ValueError(f"duration_minutes must be between 15 and 120, got {self.duration_minutes}")


STAGE_GOALS = {
    "探索期": "发现客户的工作、痛点和收益（开放式）",
    "验证期": "验证已有的价值主张假设（半结构化）",
    "优化期": "评估现有方案的契合度（结构化）",
}

B2B_ROLES = [
    {"role": "最终用户", "focus": "侧重功能性工作和日常痛点"},
    {"role": "经济购买者", "focus": "侧重成本、ROI和预算约束"},
    {"role": "决策者", "focus": "侧重战略价值和风险"},
    {"role": "影响者/建议者", "focus": "侧重评估标准和行业趋势"},
]

EIGHT_PRINCIPLES = [
    "采取初学者心态\u2014\u2014假设自己什么都不知道",
    "多听少说\u2014\u201480%时间让受访者说",
    '求得事实而非观点\u2014\u2014问\u201c上次您怎么做的\u201d而非\u201c您觉得怎么样\u201d',
    '问\u201c为什么\u201d探究动机\u2014\u2014至少追问3层',
    "目的是学习而非推销\u2014\u2014绝不介绍自己的产品",
    "不要太早提及解决方案\u2014\u2014让客户自由表达",
    "跟进保留联系信息\u2014\u2014为后续验证做准备",
    '总在最后留个门\u2014\u2014\u201c我还可以跟谁谈\uff1f\u201d',
]


class InterviewGenerator:

    def __init__(self) -> None:
        self._config: InterviewConfig | None = None

    def configure(self, business_scenario: str, target_customer: str,
                  known_hypotheses: list[str] | None = None,
                  duration_minutes: int = 45, customer_type: str = "B2C",
                  stage: str = "探索期") -> InterviewConfig:
        cfg = InterviewConfig(
            business_scenario=business_scenario,
            target_customer=target_customer,
            known_hypotheses=known_hypotheses or [],
            duration_minutes=duration_minutes,
            customer_type=customer_type,
            stage=stage,
        )
        cfg.validate()
        self._config = cfg
        return cfg

    def _time_allocation(self) -> dict[str, int]:
        cfg = self._config
        total = cfg.duration_minutes
        if total <= 30:
            return {"暖场与背景": 3, "工作探索": 8, "痛点挖掘": 8, "收益发现": 7, "收尾与拓展": 4}
        elif total <= 45:
            return {"暖场与背景": 5, "工作探索": 12, "痛点挖掘": 12, "收益发现": 10, "收尾与拓展": 5}
        else:
            return {"暖场与背景": 5, "工作探索": 15, "痛点挖掘": 15, "收益发现": 12, "收尾与拓展": 5}

    def _build_warmup(self, alloc: dict) -> list[str]:
        cfg = self._config
        t = alloc["暖场与背景"]
        lines = [
            f"## 阶段一：暖场与背景（{t}分钟）",
            "目的：建立信任，了解受访者基本情况",
            "",
            f"1. 请简单介绍一下您自己和您的{'工作' if cfg.customer_type == 'B2B' else '生活'}情况\uff1f",
            f"2. 您在{cfg.business_scenario}方面的日常是怎样的\uff1f",
        ]
        return lines

    def _build_job_exploration(self, alloc: dict) -> list[str]:
        cfg = self._config
        t = alloc["工作探索"]
        lines = [
            f"## 阶段二：工作探索（{t}分钟）",
            "目的：发现客户正在尝试完成的功能性、社会性和情感性工作",
            '原则：问\u201c做什么\u201d和\u201c为什么\u201d，不问\u201c想要什么\u201d',
            "",
            "### 功能性工作",
            f"3. 在{cfg.business_scenario}中，您通常需要完成哪些事情\uff1f",
            f"4. 请描述一下您最近一次完成相关工作的完整过程\uff1f",
            "5. 在这个过程中，哪些步骤是您必须亲自做的\uff1f",
            "",
            "### 社会性工作",
            f"6. 在{cfg.business_scenario}中，您希望在他人眼中呈现什么样的形象\uff1f",
            "7. 谁的看法对您在这件事上的决策影响最大\uff1f",
            "",
            "### 情感性工作",
            "8. 做这件事时，您最希望获得什么样的感受\uff1f",
            "9. 有没有什么让您感到安心或不安的因素\uff1f",
            "",
            "### 支持性工作（如适用）",
            f"10. 您是如何找到和选择相关产品/服务的\uff1f",
            "11. 购买后，您是如何开始使用的\uff1f遇到过什么困难吗\uff1f",
        ]
        return lines

    def _build_pain_discovery(self, alloc: dict) -> list[str]:
        cfg = self._config
        t = alloc["痛点挖掘"]
        lines = [
            f"## 阶段三：痛点挖掘（{t}分钟）",
            "目的：发现客户在完成工作过程中的障碍、风险和不满",
            "原则：追问具体事例，量化痛苦程度",
            "",
            "12. 在完成相关工作的过程中，最让您头疼/沮丧的是什么\uff1f",
            "13. 能具体描述一次让您特别不满意的经历吗\uff1f（追问：发生了什么\uff1f结果如何\uff1f）",
            "14. 有什么因素曾经阻止您完成某项工作或让您放弃\uff1f",
            "15. 在这个过程中，您最担心出现什么风险或错误\uff1f",
            "16. 如果用1-10分衡量这个痛点的严重程度，您会打几分\uff1f为什么\uff1f",
            "17. 目前您是怎么应对这些问题的\uff1f这些替代方案有什么不足\uff1f",
        ]
        return lines

    def _build_gain_discovery(self, alloc: dict) -> list[str]:
        cfg = self._config
        t = alloc["收益发现"]
        lines = [
            f"## 阶段四：收益发现（{t}分钟）",
            "目的：发现客户期望的结果和超出预期的惊喜",
            "原则：区分必需收益、期望收益、渴望收益和意外收益",
            "",
            "18. 对您来说，完成这项工作最理想的结果是什么\uff1f",
            '19. 什么情况下您会觉得这次体验\u300c超出预期\u300d\uff1f',
            f"20. 如果有一个魔法棒可以改变{cfg.business_scenario}中的一件事，您会改变什么\uff1f",
            '21. 您见过哪些竞品/替代方案让您觉得\u300c做得真好\u300d的地方\uff1f具体好在哪里\uff1f',
            f"22. 在{cfg.business_scenario}中，您愿意为什么样的改善额外付费\uff1f",
        ]
        return lines

    def _build_closing(self, alloc: dict) -> list[str]:
        cfg = self._config
        t = alloc["收尾与拓展"]
        lines = [
            f"## 阶段五：收尾与拓展（{t}分钟）",
            "目的：捕获遗漏信息，获取转介绍",
            "",
            f"23. 关于{cfg.business_scenario}，还有什么我们没聊到但您觉得重要的事情吗\uff1f",
            "24. 在您认识的人中，谁也经常做这项工作\uff1f我可以和他们聊聊吗\uff1f",
            "25. 如果我们后续有新的想法想请您看看，方便留个联系方式吗\uff1f",
        ]
        return lines

    def _build_hypotheses_section(self) -> list[str]:
        cfg = self._config
        if not cfg.known_hypotheses:
            return []
        lines = [
            "",
            "---",
            "",
            "## 附录：已知假设验证追问",
            "以下假设需在访谈中重点验证，可在相应阶段追问：",
            "",
        ]
        for i, h in enumerate(cfg.known_hypotheses, 1):
            lines.append(f"{i}. **假设**：{h}")
            lines.append(f"   - 追问：您是否遇到过这种情况\uff1f具体描述一下\uff1f")
            lines.append(f"   - 追问：这个问题对您的影响有多大（1-10分）\uff1f")
            lines.append("")
        return lines

    def _build_principles(self) -> list[str]:
        lines = [
            "",
            "---",
            "",
            "## 访谈执行要点",
            "",
            "### 八大原则（必须遵守）",
        ]
        for i, p in enumerate(EIGHT_PRINCIPLES, 1):
            lines.append(f"{i}. {p}")
        lines.extend([
            "",
            "### 执行建议",
            "- 两人一组：一人引导对话，一人记录",
            "- 记录方式：在空白客户概况框架上实时捕捉工作/痛点/收益",
            "- 每完成5次访谈后回顾，调整提纲侧重点",
        ])
        return lines

    def _build_b2b_versions(self) -> list[str]:
        cfg = self._config
        if cfg.customer_type != "B2B":
            return []
        lines = [
            "",
            "---",
            "",
            "## B2B多角色版本提纲要点",
            "",
            "B2B场景需为每个角色准备不同侧重的版本：",
            "",
        ]
        for role_info in B2B_ROLES:
            lines.append(f"### {role_info['role']}")
            lines.append(f"侧重方向：{role_info['focus']}")
            lines.append("")
            if role_info["role"] == "最终用户":
                lines.extend([
                    "- 重点追问功能性工作的具体流程和日常痛点",
                    "- 关注使用频率、操作困难和效率问题",
                    "- 了解当前替代方案的使用体验",
                ])
            elif role_info["role"] == "经济购买者":
                lines.extend([
                    "- 重点追问预算审批流程和成本考量",
                    "- 了解ROI评估标准和投资回报预期",
                    "- 关注总拥有成本（TCO）和隐性成本",
                ])
            elif role_info["role"] == "决策者":
                lines.extend([
                    "- 重点追问战略目标和组织级痛点",
                    "- 了解风险评估标准和合规要求",
                    "- 关注竞争优势和市场定位的影响",
                ])
            elif role_info["role"] == "影响者/建议者":
                lines.extend([
                    "- 重点追问行业趋势和技术评估标准",
                    "- 了解评估和推荐产品的决策框架",
                    "- 关注同行案例和最佳实践参考",
                ])
            lines.append("")
        return lines

    def generate(self) -> dict:
        if self._config is None:
            raise ValueError("please call configure() first")
        cfg = self._config
        alloc = self._time_allocation()
        recommended_count = max(10, cfg.duration_minutes // 5)
        goal = STAGE_GOALS.get(cfg.stage, cfg.stage)
        return {
            "business_scenario": cfg.business_scenario,
            "target_customer": cfg.target_customer,
            "stage": cfg.stage,
            "stage_goal": goal,
            "customer_type": cfg.customer_type,
            "duration_minutes": cfg.duration_minutes,
            "recommended_interviewees": recommended_count,
            "time_allocation": alloc,
            "total_questions": 25,
            "has_hypotheses": len(cfg.known_hypotheses) > 0,
            "hypotheses_count": len(cfg.known_hypotheses),
            "is_b2b": cfg.customer_type == "B2B",
            "b2b_roles": [r["role"] for r in B2B_ROLES] if cfg.customer_type == "B2B" else [],
        }

    def render_markdown(self) -> str:
        if self._config is None:
            raise ValueError("please call configure() first")
        cfg = self._config
        info = self.generate()
        alloc = self._time_allocation()

        lines = [
            f"# {cfg.business_scenario} - {cfg.target_customer} 访谈提纲",
            "",
            f"访谈目标：{info['stage_goal']}",
            f"预计时长：{cfg.duration_minutes}分钟",
            f"访谈人数建议：{info['recommended_interviewees']}人（建议至少10人以发现模式）",
            f"客户类型：{cfg.customer_type}",
            f"访谈阶段：{cfg.stage}",
            "",
            "---",
            "",
        ]

        lines.extend(self._build_warmup(alloc))
        lines.extend(["", "---", ""])
        lines.extend(self._build_job_exploration(alloc))
        lines.extend(["", "---", ""])
        lines.extend(self._build_pain_discovery(alloc))
        lines.extend(["", "---", ""])
        lines.extend(self._build_gain_discovery(alloc))
        lines.extend(["", "---", ""])
        lines.extend(self._build_closing(alloc))
        lines.extend(self._build_hypotheses_section())
        lines.extend(self._build_principles())

        if cfg.customer_type == "B2B":
            lines.append("- B2B场景需为每个角色（影响者/决策者/使用者/购买者）准备不同版本")
            lines.extend(self._build_b2b_versions())

        return "\n".join(lines)
