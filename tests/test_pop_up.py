from lovelace_yaml_generator import generate_pop_up_yaml


ENTITIES = {
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


EXPECTED_YAML = """type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    name: Temperatures
    icon: mdi:thermometer
    hash: "#air"
    show_header: false
  - type: custom:stack-in-card
    cards:
      - type: custom:stack-in-card
        cards:
          - type: custom:bubble-card
            card_type: separator
            name: Weather
            icon: mdi:weather-partly-cloudy
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_air_quality_index
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_temperature
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_humidity
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_pressure
      - type: custom:stack-in-card
        cards:
          - type: custom:bubble-card
            card_type: separator
            name: Particulates
            icon: mdi:chemical-weapon
          - type: custom:mini-graph-card
            align_state: right
            decimals: 1
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_pm2_5
          - type: custom:mini-graph-card
            align_state: right
            decimals: 1
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_pm10
      - type: custom:stack-in-card
        cards:
          - type: custom:bubble-card
            card_type: separator
            name: Gases
            icon: mdi:molecule
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_carbon_monoxide
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_nitrogen_dioxide
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_ozone
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_sulphur_dioxide
grid_options:
  columns: full

type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    name: Temperatures
    icon: mdi:thermometer
    hash: "#air"
    show_header: false
  - type: custom:stack-in-card
    cards:
      - type: custom:stack-in-card
        cards:
          - type: custom:bubble-card
            card_type: separator
            name: Weather
            icon: mdi:weather-partly-cloudy
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_air_quality_index
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_temperature
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_humidity
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_pressure
      - type: custom:stack-in-card
        cards:
          - type: custom:bubble-card
            card_type: separator
            name: Particulates
            icon: mdi:chemical-weapon
          - type: custom:mini-graph-card
            align_state: right
            decimals: 1
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_pm2_5
          - type: custom:mini-graph-card
            align_state: right
            decimals: 1
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_pm10
      - type: custom:stack-in-card
        cards:
          - type: custom:bubble-card
            card_type: separator
            name: Gases
            icon: mdi:molecule
          - type: custom:mini-graph-card
            align_state: right
            decimals: 0
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_carbon_monoxide
          - type: custom:mini-graph-card
            align_state: right
            decimals: 2
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_nitrogen_dioxide
          - type: custom:mini-graph-card
            align_state: right
            decimals: 2
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_ozone
          - type: custom:mini-graph-card
            align_state: right
            decimals: 2
            points_per_hour: 1
            show:
              name: true
              icon: false
            entities:
              - sensor.beacon_hill_seattle_washington_usa_sulphur_dioxide
grid_options:
  columns: full"""


def test_generate_pop_up_yaml() -> None:
    assert generate_pop_up_yaml(ENTITIES) == EXPECTED_YAML
