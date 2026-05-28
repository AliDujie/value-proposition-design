#!/usr/bin/env python3
"""Example: Experiment Design for PMF Validation.

Scenario: Testing whether users will pay for a new feature before building it.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vpd import VPDSkill

vpd = VPDSkill("SaaS Analytics Dashboard", "Data analysts at mid-size companies")

print("=" * 60)
print("Experiment Design: AI-Powered Insights Feature")
print("=" * 60)

# Design experiment with hypothesis and test cards
experiment = vpd.design_experiment(
    hypotheses=[{
        "description": "Users will pay an extra $15/month for AI-powered anomaly detection",
        "hypothesis_type": "value_proposition",
    }],
    test_cards=[{
        "hypothesis": "5%+ of existing users will click a paid upgrade CTA for AI insights",
        "test_method": "Landing page test",
        "metric": "CTA click-through rate",
        "threshold": ">= 5%",
        "falsification": "If < 3% click, the feature isn't valuable enough to build",
    }]
)
print(experiment)

print("\n" + "=" * 60)
print("Experiment Type Selection Guide")
print("=" * 60)
print("""
  LOW RISK (confidence > 70%): A/B test, feature flag
  MEDIUM RISK (40-70%): Concierge test, Wizard of Oz
  HIGH RISK (confidence < 40%): Landing page test, fake door test
  
  This experiment: HIGH RISK -> Recommendation: Landing page test
  -> Build a landing page describing the feature
  -> Drive traffic with ads to existing users
  -> Measure CTA clicks as purchase intent signal
  -> Success threshold: >5% CTA click rate
""")
