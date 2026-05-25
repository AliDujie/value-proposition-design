#!/usr/bin/env python3
"""VPD Example 02: Competitor Analysis / 竞品分析

Competitive positioning analysis across key value proposition factors.
跨关键价值主张因素的竞争定位分析。

Run: python 02_competitor_analysis.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vpd import VPDSkill

print("=" * 60)
print("VPD Example 02: Competitor Analysis")
print("示例 02：竞品分析")
print("=" * 60)

skill = VPDSkill("生鲜电商配送", "年轻职场人士")

# ── Competitive positioning ──
print("\n📊 Scenario: Competitive analysis for grocery delivery")
print("📊 场景：生鲜配送竞品分析")
print("-" * 50)

result = skill.analyze_competitor(
    my_name="FreshMart",
    factors=["配送速度", "价格竞争力", "商品质量", "品类丰富度", "售后服务"],
    players={
        "FreshMart":    [5, 3, 5, 4, 4],
        "叮咚买菜":     [4, 4, 4, 5, 3],
        "盒马鲜生":     [3, 2, 5, 5, 5],
        "美团买菜":     [4, 5, 3, 4, 3],
    }
)
print(result[:800])
print("...\n")

print("✅ Tip: Use competitor analysis to identify differentiation opportunities.")
print("✅ 提示：使用竞品分析来识别差异化机会。")
