# TODO: define your data classes here
from pydantic import BaseModel
from typing import Optional
from datetime import date
from typing import List, Dict, Optional

class TeamStats(BaseModel):
    team_id: int
    team_abbreviation: str
    team_name: str
    matchup: str
    wl: Optional[str] = None  # Allow None (or NaN) values
    min: Optional[int] = None
    fgm: Optional[int] = None
    fga: Optional[int] = None
    fg_pct: Optional[float] = None
    fg3m: Optional[int] = None
    fg3a: Optional[int] = None
    fg3_pct: Optional[float] = None
    ftm: Optional[int] = None
    fta: Optional[int] = None
    ft_pct: Optional[float] = None
    oreb: Optional[int] = None
    dreb: Optional[int] = None
    reb: Optional[int] = None
    ast: Optional[int] = None
    stl: Optional[int] = None
    blk: Optional[int] = None
    tov: Optional[int] = None
    pf: Optional[int] = None
    pts: Optional[int] = None
    plus_minus: Optional[int] = None
    video_available: Optional[bool] = None
    
class GameData(BaseModel):
    season_id: int
    season_type: str
    team_home: TeamStats
    team_away: TeamStats
    game_id: int
    game_date: date

class DataConfig(BaseModel):
    table: str
    data_path: str
    features_columns: List[str]

# Model configuration
class ModelConfig(BaseModel):
    name: str
    type: str
    params: Dict[str, Optional[int]]

class Config(BaseModel):
    data: DataConfig
    model: ModelConfig    