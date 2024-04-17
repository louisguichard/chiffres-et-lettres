import yaml


def load_config():
    """
    Load configuration settings from the YAML config file.

    Returns:
        dict: Dictionary containing onfigurations.
    """
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config
