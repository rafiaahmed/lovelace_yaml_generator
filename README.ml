# Lovelace YAML Generator

Generate Home Assistant bubble-card pop-up YAML from categorized entity lists.

## Command line

```bash
python -m lovelace_yaml_generator
```

The command prints the sample Seattle air quality configuration defined in
`lovelace_yaml_generator.examples.EXAMPLE_ENTITIES`.

## Interactive notebook UI

Open [`notebooks/bubble_card_ui.ipynb`](notebooks/bubble_card_ui.ipynb) in Jupyter
Lab or Jupyter Notebook. The notebook uses `ipywidgets` to provide text areas for
editing the Weather, Particulates, and Gases entity groups. Click **Generate
YAML** to refresh the rendered configuration and copy it into Home Assistant.
