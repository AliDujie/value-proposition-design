#!/usr/bin/env python3
"""Example: Value Proposition Canvas Analysis.

Scenario: Analyzing a meal delivery app's value proposition for busy professionals.
"""
from vpd import VPDSkill

vpd = VPDSkill("Meal Delivery App")

print("=" * 60)
print("Canvas Analysis: Meal Delivery App for Busy Professionals")
print("=" * 60)

analysis = vpd.analyze_canvas(
    jobs=["Get a healthy meal without cooking", "Save time during weeknights"],
    pains=["Food arrives cold", "Limited healthy options", "Too expensive"],
    gains=["30-minute delivery guarantee", "Nutritionist-designed menus", "Family-sized portions"]
)
print(analysis)

# Fit scoring
print("\n" + "=" * 60)
print("Fit Score Interpretation")
print("=" * 60)
print("""
  Problem-Solution Fit: How well our solution addresses the pains
  Product-Market Fit: Whether people would buy what we're building
  Business Model Fit: Whether the unit economics work long-term
""")
