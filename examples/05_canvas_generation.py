#!/usr/bin/env python3
"""VPD Example 01: Canvas Generation / 画布生成

Generates a Value Proposition Canvas with fit score analysis.
生成价值主张画布并分析契合度。

Run: python 01_canvas_generation.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vpd import VPDSkill

print("=" * 60)
print("VPD Example 01: Canvas Generation")
print("示例 01：画布生成")
print("=" * 60)

# Scenario: Fresh grocery delivery for young professionals
skill = VPDSkill("生鲜电商配送", "年轻职场人士")

# ── Generate canvas ──
print("\n📋 Scenario: Fresh grocery delivery for young professionals")
print("📋 场景：面向年轻职场人士的生鲜配送服务")
print("-" * 50)
canvas = skill.generate_canvas()
print(canvas[:600])
print("...\n")

# ── Analyze with populated canvas ──
print("\n📋 Populated Canvas Analysis / 填充画布分析")
print("-" * 50)
analysis = skill.analyze_canvas(
    product_name="FreshMart",
    jobs=[
        {"description": "购买新鲜食材", "category": "functional", "importance": 5},
        {"description": "节省购物时间", "category": "functional", "importance": 4},
    ],
    pains=[
        {"description": "超市排队时间长", "severity": "severe"},
        {"description": "食材不新鲜", "severity": "critical"},
    ],
    gains=[
        {"description": "30分钟内送达", "desire_level": "required"},
        {"description": "有机食品选择", "desire_level": "desired"},
    ],
    products=[
        {"description": "30分钟极速达", "category": "digital"},
        {"description": "源头直采新鲜保障", "category": "tangible"},
    ],
    pain_relievers=[
        {"description": "免排队送货上门", "target_pain": "超市排队时间长", "coverage": "full"},
        {"description": "冷链保鲜", "target_pain": "食材不新鲜", "coverage": "full"},
    ],
    gain_creators=[
        {"description": "30分钟达", "target_gain": "30分钟内送达", "coverage": "full"},
        {"description": "有机专区", "target_gain": "有机食品选择", "coverage": "partial"},
    ],
)
print(analysis[:600])
print("...\n")

print("✅ Tip: Higher fit scores mean better problem-solution alignment.")
print("✅ 提示：更高的契合度分数意味着更好的问题-方案匹配。")
