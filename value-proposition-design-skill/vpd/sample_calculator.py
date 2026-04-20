import math
from vpd.utils import load_config


class SampleCalculator:

    def __init__(self, config_path: str = ""):
        cfg = load_config(config_path)
        self._sample_cfg = cfg.get("sample", {})
        self._z_values = self._sample_cfg.get("confidence_z", {90: 1.645, 95: 1.960, 99: 2.576})

    def minimum_sample_size(self, confidence: int = 95, margin_of_error: float = 0.05, proportion: float = 0.5, population: int = 0) -> dict:
        z = self._z_values.get(confidence)
        if z is None:
            raise ValueError(f"confidence must be one of {list(self._z_values.keys())}, got {confidence}")
        if not 0 < margin_of_error < 1:
            raise ValueError(f"margin_of_error must be between 0 and 1, got {margin_of_error}")
        if not 0 < proportion < 1:
            raise ValueError(f"proportion must be between 0 and 1, got {proportion}")

        n0 = (z ** 2 * proportion * (1 - proportion)) / (margin_of_error ** 2)
        n0 = math.ceil(n0)

        if population > 0:
            n_adj = math.ceil(n0 / (1 + (n0 - 1) / population))
        else:
            n_adj = n0

        return {
            "sample_size": n_adj,
            "sample_size_infinite": n0,
            "confidence": confidence,
            "margin_of_error": margin_of_error,
            "proportion": proportion,
            "population": population if population > 0 else "infinite",
            "z_value": z,
        }

    def render_markdown(self, confidence: int = 95, margin_of_error: float = 0.05, proportion: float = 0.5, population: int = 0) -> str:
        r = self.minimum_sample_size(confidence, margin_of_error, proportion, population)
        lines = [
            "# 样本量计算结果",
            "",
            "| 参数 | 值 |",
            "|------|-----|",
            f"| 置信水平 | {r['confidence']}% |",
            f"| 误差范围 | ±{r['margin_of_error'] * 100}% |",
            f"| 预估比例 | {r['proportion'] * 100}% |",
            f"| 总体规模 | {r['population']} |",
            f"| Z值 | {r['z_value']} |",
            f"| **最小样本量** | **{r['sample_size']}** |",
        ]
        if population > 0:
            lines.append(f"| 无限总体样本量 | {r['sample_size_infinite']} |")
        return "\n".join(lines)
