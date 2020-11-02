from pydantic import BaseModel, PositiveInt

class PerGame(BaseModel):
    id: PositiveInt
    player_id: PositiveInt = None
    name: str = None
    season: str = None
    age: PositiveInt = None
    team: str = None
    league: str = None
    position: str = None
    games: PositiveInt = None
    games_started: PositiveInt = None
    minutes_played: PositiveInt = None
    field_goals: float = None
    field_goal_attempts: float = None
    field_goal_percentage: float = None
    three_pointers: float = None
    three_point_attempts: float = None
    three_point_percentage: float = None
    two_pointers: float = None
    two_point_attempts: float = None
    two_point_percentage: float = None
    effective_field_goal_percentage: float = None
    free_throws: float = None
    free_throw_attempts: float = None
    free_throw_percentage: float = None
    offensive_rebound_total: float = None
    defensive_rebound_total: float = None
    rebound_total: float = None
    assists: float = None
    steals: float = None
    blocks: float = None
    turnovers: float = None
    personal_fouls: float = None
    points: float = None