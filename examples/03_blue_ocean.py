#!/usr/bin/env python3
"""Example: Competitive Analysis with Blue Ocean ERRC Grid.

Scenario: Finding whitespace in the competitive project management market.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vpd import VPDSkill

vpd = VPDSkill("Project Management Tool", "Tech startups")

print("=" * 60)
print("Competitive Analysis: Project Management Market")
print("=" * 60)

analysis = vpd.analyze_competitor(
    my_name="Our PM Tool",
    factors=["Ease of use", "Customization", "Price", "Integrations",
             "AI automation", "Mobile experience", "Reporting"],
    players={
        "Asana":       [4, 3, 2, 4, 2, 4, 3],
        "Jira":        [2, 5, 3, 4, 2, 2, 4],
        "Trello":      [5, 2, 4, 2, 1, 3, 1],
        "Monday.com":  [4, 4, 2, 3, 3, 4, 3],
        "Our PM Tool": [4, 4, 4, 3, 5, 4, 3],
    }
)
print(analysis)

print("\n" + "=" * 60)
print("ERRC Grid (Eliminate-Reduce-Raise-Create)")
print("=" * 60)
print("""
  ELIMINATE: What factors can we remove entirely?
  → Complex onboarding wizards
  → Mandatory project templates

  REDUCE: What factors can we reduce below industry standard?
  → Setup time (from hours to minutes)
  → Number of clicks to create a task

  RAISE: What factors should we raise above industry standard?
  → AI-powered task prioritization
  → Cross-team visibility

  CREATE: What factors can we create that the industry has never offered?
  → Voice-first task management
  → Automatic meeting-to-action-item conversion
""")
