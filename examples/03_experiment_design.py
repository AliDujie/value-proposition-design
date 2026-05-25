#!/usr/bin/env python3
"""Example: Experiment Design for PMF Validation.

Scenario: Testing whether users will pay for a new feature before building it.
"""
from vpd import VPDSkill

vpd = VPDSkill("SaaS Analytics Dashboard")

print("=" * 60)
print("Experiment Design: AI-Powered Insights Feature")
print("=" * 60)

experiment = vpd.design_experiment(
    hypothesis="Users will pay an extra $15/month for AI-powered anomaly detection",
    risk_level="high",  # building without validation = high risk
    metric="conversion_to_paid"
)
print(experiment)

print("\n" + "=" * 60)
print("Experiment Type Selection Guide")
print("=" * 60)
print("""
  LOW RISK (confidence > 70%): A/B test, feature flag
  MEDIUM RISK (40-70%): Concierge test, Wizard of Oz
  HIGH RISK (confidence < 40%): Landing page test, fake door test
  
  This experiment: HIGH RISK → Recommendation: Landing page test
  → Build a landing page describing the feature
  → Drive traffic with ads to existing users
  → Measure CTA clicks as purchase intent signal
  → Success threshold: >5% CTA click rate
""")
