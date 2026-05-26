#!/usr/bin/env python3
"""Example: Blue Ocean Strategy Analysis with ERRC Grid.

Scenario: Finding whitespace in the competitive project management market.
"""
from vpd import VPDSkill

vpd = VPDSkill("Project Management Tool")

print("=" * 60)
print("Blue Ocean Analysis: Project Management")
print("=" * 60)

analysis = vpd.competitive_strategy(
    industry="Project Management Software",
    competitors=["Asana", "Jira", "Trello", "Monday.com"],
    factors=["Ease of use", "Customization", "Price", "Integrations",
             "AI automation", "Mobile experience", "Reporting"]
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
