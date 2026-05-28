#!/usr/bin/env python3
"""Example: Value Proposition Canvas Analysis.

Scenario: Analyzing a meal delivery app's value proposition for busy professionals.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vpd import VPDSkill

vpd = VPDSkill("Meal Delivery App", "Busy professionals")

print("=" * 60)
print("Canvas Analysis: Meal Delivery App for Busy Professionals")
print("=" * 60)

# Full canvas analysis with all 7 components (correct Dict format)
analysis = vpd.analyze_canvas(
    product_name="Meal Delivery App",
    jobs=[
        {"description": "Get a healthy meal without cooking", "category": "functional", "importance": 5},
        {"description": "Save time during weeknights", "category": "functional", "importance": 4},
    ],
    pains=[
        {"description": "Food arrives cold", "category": "emotional", "importance": 3},
        {"description": "Limited healthy options", "category": "functional", "importance": 2},
        {"description": "Too expensive for daily use", "category": "financial", "importance": 4},
    ],
    gains=[
        {"description": "30-minute delivery guarantee", "category": "functional", "importance": 5},
        {"description": "Nutritionist-designed menus", "category": "functional", "importance": 3},
        {"description": "Family-sized portions", "category": "functional", "importance": 2},
    ],
    products=[
        {"description": "30-min hot delivery", "category": "feature"},
        {"description": "Weekly meal plans", "category": "feature"},
    ],
    pain_relievers=[
        {"description": "Insulated packaging keeps food hot", "target_pain": "Food arrives cold", "coverage": "full"},
        {"description": "Prep-ahead meal kits", "target_pain": "Too expensive for daily use", "coverage": "partial"},
    ],
    gain_creators=[
        {"description": "Rotating nutritionist menus", "target_gain": "Nutritionist-designed menus", "coverage": "full"},
        {"description": "Family bundle pricing", "target_gain": "Family-sized portions", "coverage": "full"},
    ]
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
