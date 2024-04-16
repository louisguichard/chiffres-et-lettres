import yaml


def load_config(profile="default"):
    """
    Load configuration settings from the YAML config file.

    Args:
        profile (str): Configuration profile name.

    Returns:
        dict: Dictionary containing profile-specific configurations.
    """
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config.get(profile)
