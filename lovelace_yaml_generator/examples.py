"""Example entity groups for the bubble-card pop-up generator."""

from __future__ import annotations

from typing import Dict, List

EXAMPLE_ENTITIES: Dict[str, List[str]] = {
    "Weather": [
        "sensor.beacon_hill_seattle_washington_usa_air_quality_index",
        "sensor.beacon_hill_seattle_washington_usa_humidity",
        "sensor.beacon_hill_seattle_washington_usa_pressure",
    ],
    "Particulates": [
        "sensor.beacon_hill_seattle_washington_usa_pm10",
        "sensor.beacon_hill_seattle_washington_usa_pm2_5",
    ],
    "Gases": [
        "sensor.beacon_hill_seattle_washington_usa_carbon_monoxide",
        "sensor.beacon_hill_seattle_washington_usa_nitrogen_dioxide",
        "sensor.beacon_hill_seattle_washington_usa_ozone",
        "sensor.beacon_hill_seattle_washington_usa_sulphur_dioxide",
    ],
}

__all__ = ["EXAMPLE_ENTITIES"]
