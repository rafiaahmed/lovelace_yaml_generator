"""Command line entry point for generating the sample YAML."""

from . import generate_pop_up_yaml

EXAMPLE_ENTITIES = {
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


def main() -> None:
    print(generate_pop_up_yaml(EXAMPLE_ENTITIES))


if __name__ == "__main__":
    main()
