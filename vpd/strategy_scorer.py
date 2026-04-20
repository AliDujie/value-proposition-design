from vpd.utils import load_config


class StrategyScorer:

    def __init__(self, config_path: str = ""):
        cfg = load_config(config_path)
        scfg = cfg.get("strategy", {})
        self._min = scfg.get("scoring", {}).get("min", 0)
        self._max = scfg.get("scoring", {}).get("max", 10)
        self._adv_thresh = scfg.get("advantage_threshold", 2)
        self._weak_thresh = scfg.get("weakness_threshold", -2)
        self._nomans_thresh = scfg.get("no_mans_land_threshold", 4)
        self.factors: list[str] = []
        self.players: dict[str, list[int]] = {}

    def set_factors(self, factors: list[str]) -> None:
        self.factors = list(factors)

    def add_player(self, name: str, scores: list[int]) -> None:
        if len(scores) != len(self.factors):
            raise ValueError(f"scores length {len(scores)} != factors length {len(self.factors)}")
        for s in scores:
            if not self._min <= s <= self._max:
                raise ValueError(f"score {s} out of range [{self._min}, {self._max}]")
        self.players[name] = list(scores)

    def _industry_avg(self) -> list[float]:
        n = len(self.players)
        if n == 0:
            return [0.0] * len(self.factors)
        avgs = []
        for i in range(len(self.factors)):
            avgs.append(sum(p[i] for p in self.players.values()) / n)
        return avgs

    def analyze(self, my_name: str) -> dict:
        if my_name not in self.players:
            raise ValueError(f"player '{my_name}' not found")
        my_scores = self.players[my_name]
        avgs = self._industry_avg()
        competitors = {k: v for k, v in self.players.items() if k != my_name}

        factor_analysis = []
        advantages, weaknesses, no_mans = [], [], []

        for i, factor in enumerate(self.factors):
            diff = my_scores[i] - avgs[i]
            entry = {
                "factor": factor,
                "my_score": my_scores[i],
                "industry_avg": round(avgs[i], 1),
                "diff": round(diff, 1),
            }
            for cname, cscores in competitors.items():
                entry[cname] = cscores[i]
            factor_analysis.append(entry)

            if diff >= self._adv_thresh:
                advantages.append(factor)
            elif diff <= self._weak_thresh:
                weaknesses.append(factor)

            all_low = all(p[i] <= self._nomans_thresh for p in self.players.values())
            if all_low:
                no_mans.append(factor)

        eliminate = [f for f in self.factors if all(
            self.players[p][self.factors.index(f)] <= 3 for p in self.players
        )]
        reduce = weaknesses
        raise_up = [f for f in advantages if my_scores[self.factors.index(f)] < 8]
        create = no_mans

        return {
            "my_name": my_name,
            "factor_analysis": factor_analysis,
            "advantages": advantages,
            "weaknesses": weaknesses,
            "no_mans_land": no_mans,
            "blue_ocean": {
                "eliminate": eliminate,
                "reduce": reduce,
                "raise": raise_up,
                "create": create,
            },
        }

    def render_markdown(self, my_name: str) -> str:
        r = self.analyze(my_name)
        comp_names = [k for k in self.players if k != my_name]
        lines = [
            f"# 竞争战略画布",
            "",
            f"分析对象：{my_name} vs {', '.join(comp_names)}",
            "",
            "## 竞争因素评分表",
            "",
        ]

        header = f"| 竞争因素 | {my_name} |"
        sep = f"|---------|:------:|"
        for cn in comp_names:
            header += f" {cn} |"
            sep += ":------:|"
        header += " 行业均值 |"
        sep += ":------:|"
        lines.extend([header, sep])

        for fa in r["factor_analysis"]:
            row = f"| {fa['factor']} | {fa['my_score']} |"
            for cn in comp_names:
                row += f" {fa.get(cn, '-')} |"
            row += f" {fa['industry_avg']} |"
            lines.append(row)

        lines.extend(["", "## 价值曲线（文本版）", ""])
        bar_chars = "▓░"
        for fa in r["factor_analysis"]:
            filled = "▓" * fa["my_score"] + "░" * (self._max - fa["my_score"])
            lines.append(f"{fa['factor']:　<8s}  {filled} {fa['my_score']}")

        lines.extend(["", "## 差异化机会识别", ""])
        if r["advantages"]:
            lines.append(f"### 我方优势领域（得分高于均值≥{self._adv_thresh}分）")
            for f in r["advantages"]:
                lines.append(f"- {f}")
        if r["weaknesses"]:
            lines.append(f"### 我方劣势领域（得分低于均值≥{abs(self._weak_thresh)}分）")
            for f in r["weaknesses"]:
                lines.append(f"- {f}")
        if r["no_mans_land"]:
            lines.append(f"### 无人区机会（所有玩家得分均≤{self._nomans_thresh}分）")
            for f in r["no_mans_land"]:
                lines.append(f"- {f}")

        bo = r["blue_ocean"]
        lines.extend(["", "## 蓝海四项行动框架", ""])
        lines.append("| 行动 | 说明 | 具体建议 |")
        lines.append("|------|------|---------|")
        lines.append(f"| **剔除** | 行业习以为常但可以去掉的因素 | {', '.join(bo['eliminate']) or '暂无'} |")
        lines.append(f"| **减少** | 可降低到行业标准以下的因素 | {', '.join(bo['reduce']) or '暂无'} |")
        lines.append(f"| **增加** | 应提升到行业标准以上的因素 | {', '.join(bo['raise']) or '暂无'} |")
        lines.append(f"| **创造** | 行业从未提供、应该创造的因素 | {', '.join(bo['create']) or '暂无'} |")

        return "\n".join(lines)
