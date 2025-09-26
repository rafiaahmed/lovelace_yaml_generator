"""Command line entry point for generating the sample YAML."""

from . import EXAMPLE_ENTITIES, generate_pop_up_yaml


def main() -> None:
    print(generate_pop_up_yaml(EXAMPLE_ENTITIES))


if __name__ == "__main__":
    main()
