# TODO: read in your yaml file and parse it using the data classes defined in dataclasses.py
import yaml
from pathlib import Path
from nba_dataclasses import Config

def load_config() -> Config:
    """Load configuration from config.yaml and return it as a Config instance."""
    config_path = Path(__file__).parent.parent / "config.yaml"
    config_dict = yaml.safe_load(config_path.read_text())
    return Config(**config_dict)

# For testing purposes only
if __name__ == "__main__":
    config = load_config()
    data_config = config.data
    model_config = config.model

    # Print the configurations with spaces in between for readability
    print("\nData Configuration:", data_config, "\n")
    print("\nModel Configuration:", model_config, "\n")