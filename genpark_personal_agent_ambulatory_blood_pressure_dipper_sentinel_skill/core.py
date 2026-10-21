# -*- coding: utf-8 -*-
"""Ambulatory Blood Pressure Dipping Sentinel for GenPark Personal Agent."""
import json
from typing import Dict, Any

class AmbulatoryBloodPressureDippingSentinel:
    @staticmethod
    def calculate_nocturnal_dipping_ratio(daytime_mean_sbp: float, nighttime_mean_sbp: float, morning_surge_sbp: float = 0.0) -> Dict[str, Any]:
        dip_pct = round(((daytime_mean_sbp - nighttime_mean_sbp) / daytime_mean_sbp) * 100.0, 1)
        
        if dip_pct >= 20.0:
            category = "EXTREME_DIPPER"
            risk = "Elevated risk for anterior ischemic optic neuropathy and cerebral ischemic events."
        elif dip_pct >= 10.0:
            category = "NORMAL_DIPPER"
            risk = "Optimal physiological cardiovascular recovery profile."
        elif dip_pct >= 0.0:
            category = "NON_DIPPER"
            risk = "Elevated 24h cardiovascular burden and target organ damage risk."
        else:
            category = "REVERSE_DIPPER_RISER"
            risk = "Critical risk profile: severe nocturnal autonomic dysfunction and stroke risk."
            
        morning_surge_delta = round(max(0.0, morning_surge_sbp - nighttime_mean_sbp), 1) if morning_surge_sbp > 0 else 0.0
        return {
            "daytime_sbp": daytime_mean_sbp,
            "nighttime_sbp": nighttime_mean_sbp,
            "dipping_ratio_pct": dip_pct,
            "chronotype_classification": category,
            "morning_surge_mmhg": morning_surge_delta,
            "clinical_cardiovascular_assessment": risk
        }

    @staticmethod
    def generate_chrono_hypertensive_lifestyle_advisory(dipping_category: str) -> Dict[str, Any]:
        if "REVERSE" in dipping_category or "NON_DIPPER" in dipping_category:
            advisory = [
                "Screen urgently for Obstructive Sleep Apnea (OSA) via home sleep study",
                "Shift anti-hypertensive pharmacotherapy discussion with physician toward bedtime dosing (Chronotherapy)",
                "Eliminate evening sodium intake and avoid fluids 3 hours before bed"
            ]
        else:
            advisory = [
                "Maintain consistent 10-15 minute post-dinner zone 1 walk",
                "Keep magnesium threonate or bisglycinate intake 60 min before sleep",
                "Maintain circadian sleep hygiene"
            ]
        return {"category": dipping_category, "actionable_lifestyle_adjustments": advisory}
