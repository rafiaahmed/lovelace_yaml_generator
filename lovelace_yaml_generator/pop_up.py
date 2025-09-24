"""Generate YAML for Lovelace bubble-card pop-up stacks."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Dict, List

CATEGORY_CONFIG = (
    ("Weather", "mdi:weather-partly-cloudy", 0),
    ("Particulates", "mdi:chemical-weapon", 1),
    ("Gases", "mdi:molecule", 0),
)

HEADER_CARD = {
    "type": "custom:bubble-card",
    "card_type": "pop-up",
    "name": "Temperatures",
    "icon": "mdi:thermometer",
    "hash": "#air",
    "show_header": False,
}


def generate_pop_up_yaml(entities: Mapping[str, Sequence[str]]) -> str:
    """Return the YAML string describing the pop-up card stacks."""

    normalized = _normalize_entities(entities)
    overrides = _decimal_overrides(normalized.get("Gases", []))
    documents = []
    for override in overrides:
        document = _build_document(normalized, override)
        documents.append(_to_yaml(document))
    return "\n\n".join(documents)


def _normalize_entities(entities: Mapping[str, Sequence[str]]) -> Dict[str, List[str]]:
    normalized: Dict[str, List[str]] = {}
    for category, _, _ in CATEGORY_CONFIG:
        sensors = list(entities.get(category, ()))
        if not sensors:
            continue
        if category == "Weather":
            sensors = _with_temperature(sensors)
        elif category == "Particulates":
            sensors = sorted(sensors, key=_pm_value)
        normalized[category] = sensors
    return normalized


def _with_temperature(sensors: Sequence[str]) -> List[str]:
    deduped: List[str] = []
    seen: set[str] = set()
    for sensor in sensors:
        if sensor not in seen:
            deduped.append(sensor)
            seen.add(sensor)

    if not deduped:
        return deduped

    temperature = _derive_temperature_sensor(deduped)
    if not temperature:
        return deduped

    if temperature in deduped:
        deduped.remove(temperature)
    deduped.insert(1, temperature)
    return deduped


def _derive_temperature_sensor(sensors: Sequence[str]) -> str:
    prefix = _shared_prefix(sensors)
    if "_" in prefix:
        prefix = prefix[: prefix.rfind("_") + 1]
    return f"{prefix}temperature" if prefix else ""


def _shared_prefix(values: Sequence[str]) -> str:
    if not values:
        return ""
    prefix = values[0]
    for value in values[1:]:
        max_length = min(len(prefix), len(value))
        index = 0
        while index < max_length and prefix[index] == value[index]:
            index += 1
        prefix = prefix[:index]
        if not prefix:
            break
    return prefix


def _pm_value(sensor: str) -> float:
    tail = sensor.split("_pm")[-1]
    number = tail.replace("_", ".")
    try:
        return float(number)
    except ValueError:
        return float("inf")


def _decimal_overrides(gases: Sequence[str]) -> List[Mapping[str, int]]:
    overrides: List[Mapping[str, int]] = [{}]
    if len(gases) > 1:
        overrides.append({entity: 2 for entity in gases[1:]})
    return overrides


def _build_document(
    entities: Mapping[str, Sequence[str]],
    decimals_override: Mapping[str, int],
) -> Mapping[str, object]:
    sections = []
    for category, icon, default_decimals in CATEGORY_CONFIG:
        sensors = entities.get(category, [])
        if not sensors:
            continue
        cards = [_separator_card(category, icon)]
        for sensor in sensors:
            decimals = decimals_override.get(sensor, default_decimals)
            cards.append(_mini_graph_card(sensor, decimals))
        sections.append({"type": "custom:stack-in-card", "cards": cards})

    return {
        "type": "vertical-stack",
        "cards": [
            HEADER_CARD.copy(),
            {
                "type": "custom:stack-in-card",
                "cards": sections,
            },
        ],
        "grid_options": {"columns": "full"},
    }


def _separator_card(name: str, icon: str) -> Mapping[str, object]:
    return {
        "type": "custom:bubble-card",
        "card_type": "separator",
        "name": name,
        "icon": icon,
    }


def _mini_graph_card(entity_id: str, decimals: int) -> Mapping[str, object]:
    return {
        "type": "custom:mini-graph-card",
        "align_state": "right",
        "decimals": decimals,
        "points_per_hour": 1,
        "show": {
            "name": True,
            "icon": False,
        },
        "entities": [entity_id],
    }


def _to_yaml(document: Mapping[str, object]) -> str:
    return "\n".join(_render_mapping(document, indent=0))


def _render_mapping(
    mapping: Mapping[str, object],
    *,
    indent: int,
    first_prefix: str | None = None,
) -> List[str]:
    lines: List[str] = []
    items = list(mapping.items())
    spaces = "  " * indent
    for index, (key, value) in enumerate(items):
        prefix = first_prefix if index == 0 and first_prefix is not None else spaces
        if isinstance(value, dict):
            lines.append(f"{prefix}{key}:")
            lines.extend(_render_mapping(value, indent=indent + 1))
        elif isinstance(value, list):
            lines.append(f"{prefix}{key}:")
            lines.extend(_render_sequence(value, indent=indent + 1))
        else:
            lines.append(f"{prefix}{key}: {_format_scalar(value)}")
    return lines


def _render_sequence(values: Sequence[object], *, indent: int) -> List[str]:
    lines: List[str] = []
    spaces = "  " * indent
    for value in values:
        if isinstance(value, dict):
            lines.extend(
                _render_mapping(
                    value,
                    indent=indent + 1,
                    first_prefix=f"{spaces}- ",
                )
            )
        elif isinstance(value, list):
            lines.append(f"{spaces}-")
            lines.extend(_render_sequence(value, indent=indent + 1))
        else:
            lines.append(f"{spaces}- {_format_scalar(value)}")
    return lines


def _format_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return f"{value:g}"
    if value is None:
        return "null"
    return _format_string(str(value))


def _format_string(value: str) -> str:
    if not value:
        return "''"
    needs_quotes = (
        value.startswith("#")
        or value.strip() != value
        or value in {"true", "false", "null"}
    )
    return f'"{value}"' if needs_quotes else value
