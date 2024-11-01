import pandas as pd
from pathlib import Path


def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


if __name__ == "__main__":
    # TODO: fix this data path using the pathlib library
    data_path = "/Users/adrianochs/all_my_great_data/game.csv"
    df = load_csv(data_path)
    print(data_path)
