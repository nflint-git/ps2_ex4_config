# data_load.py
import pandas as pd
from pathlib import Path
from datetime import datetime
from nba_dataclasses import Config, GameData, TeamStats
from config import load_config  # Import the function to load configuration
from pydantic import ValidationError


def load_csv(data_path: Path) -> pd.DataFrame:
    """Loads the CSV file from the given path and drops rows with NaN values."""
    df = pd.read_csv(data_path, parse_dates=["game_date"])
    df = df.dropna()  # Drop rows with any NaN values
    return df


def create_team_stats(row, prefix) -> TeamStats:
    """Creates and validates a TeamStats instance from a DataFrame row."""
    try:
        return TeamStats(
            team_id=row[f"team_id_{prefix}"],
            team_abbreviation=row[f"team_abbreviation_{prefix}"],
            team_name=row[f"team_name_{prefix}"],
            matchup=row[f"matchup_{prefix}"],
            wl=row.get(f"wl_{prefix}"),
            min=row.get("min"),
            fgm=row.get(f"fgm_{prefix}"),
            fga=row.get(f"fga_{prefix}"),
            fg_pct=row.get(f"fg_pct_{prefix}"),
            fg3m=row.get(f"fg3m_{prefix}"),
            fg3a=row.get(f"fg3a_{prefix}"),
            fg3_pct=row.get(f"fg3_pct_{prefix}"),
            ftm=row.get(f"ftm_{prefix}"),
            fta=row.get(f"fta_{prefix}"),
            ft_pct=row.get(f"ft_pct_{prefix}"),
            oreb=row.get(f"oreb_{prefix}"),
            dreb=row.get(f"dreb_{prefix}"),
            reb=row.get(f"reb_{prefix}"),
            ast=row.get(f"ast_{prefix}"),
            stl=row.get(f"stl_{prefix}"),
            blk=row.get(f"blk_{prefix}"),
            tov=row.get(f"tov_{prefix}"),
            pf=row.get(f"pf_{prefix}"),
            pts=row.get(f"pts_{prefix}"),
            plus_minus=row.get(f"plus_minus_{prefix}"),
            video_available=row.get(f"video_available_{prefix}")
        )
    except KeyError as e:
        print(f"Column {e} not found in the DataFrame for {prefix} team")
        return None  # Return None if validation fails


def load_and_validate_game_data(config: Config) -> list:
    """Loads and validates game data from the CSV based on configuration."""
    data_path = Path(__file__).parent.parent / config.data.data_path
    print(f"Trying to load file from: {data_path.resolve()}")

    # Load the CSV data
    df = load_csv(data_path)
    
    # Convert each row in the DataFrame to GameData instances, validating each row
    games = []
    for index, row in df.iterrows():
        try:
            # Validate home and away teams
            team_home = create_team_stats(row, "home")
            team_away = create_team_stats(row, "away")
            
            if team_home is None or team_away is None:
                print(f"Skipping row {index} due to validation errors in team data.")
                continue
            
            # Validate the overall game data
            game_data = GameData(
                season_id=row["season_id"],
                season_type=row["season_type"],
                team_home=team_home,
                team_away=team_away,
                game_id=row["game_id"],
                game_date=row["game_date"].date()
            )
            
            # Append validated game data to the list
            games.append(game_data)
        
        except ValidationError as e:
            print(f"Validation error for game at row {index}: {e}")
            continue  # Skip this row if validation fails

    return games


if __name__ == "__main__":
    # Load configuration and use it to load and validate game data
    config = load_config()
    games = load_and_validate_game_data(config)
    
    # Display the first GameData instance as an example
    if games:
        print("Example of validated GameData instance:\n", games[0])
    else:
        print("No valid game data found.")
