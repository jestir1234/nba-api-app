from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint, Float, ForeignKey, VARCHAR
from app.database import Base


class PerGame(Base):
    __tablename__ = 'per_game'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=True)
    name = Column(VARCHAR(255), nullable=False)
    season = Column(String(255), nullable=True)
    age = Column(Integer, nullable=True)
    team = Column(String(255), nullable=True)
    league = Column(String(255), nullable=True)
    position = Column(String(255), nullable=True)
    games = Column(String(255), nullable=True)
    games_started = Column(String(255), nullable=True)
    minutes_played = Column(Integer, nullable=True)
    field_goals = Column(String(255), nullable=True)
    field_goal_attempts = Column(Float, nullable=True)
    field_goal_percentage = Column(Float, nullable=True)
    three_pointers = Column(Float, nullable=True)
    three_point_attempts = Column(Float, nullable=True)
    three_point_percentage = Column(Float, nullable=True)
    two_pointers = Column(Float, nullable=True)
    two_point_attempts = Column(Float, nullable=True)
    two_point_percentage = Column(Float, nullable=True)
    effective_field_goal_percentage = Column(Float, nullable=True)
    free_throws = Column(Float, nullable=True)
    free_throw_attempts = Column(Float, nullable=True)
    free_throw_percentage = Column(Float, nullable=True)
    offensive_rebound_total = Column(Float, nullable=True)
    defensive_rebound_total = Column(Float, nullable=True)
    rebound_total = Column(Float, nullable=True)
    assists = Column(Float, nullable=True)
    steals = Column(Float, nullable=True)
    blocks = Column(Float, nullable=True)
    turnovers = Column(Float, nullable=True)
    personal_fouls = Column(Float, nullable=True)
    points = Column(Float, nullable=True)

    __table_args__ = (UniqueConstraint(
        'player_id', 'season', name='unique_player_season'), )

    def __init__(
        self, 
        player_id, 
        name,
        season,
        age,
        team,
        league,
        position,
        games,
        games_started,
        minutes_played,
        field_goals,
        field_goal_attempts,
        field_goal_percentage,
        three_pointers,
        three_point_attempts,
        three_point_percentage,
        two_pointers,
        two_point_attempts,
        two_point_percentage,
        effective_field_goal_percentage,
        free_throws,
        free_throw_attempts,
        free_throw_percentage,
        offensive_rebound_total,
        defensive_rebound_total,
        rebound_total,
        assists,
        steals,
        blocks,
        turnovers,
        personal_fouls,
        points
    ):
        self.player_id = player_id if player_id else None
        self.name = name if name else None
        self.season = season if season else None
        self.age = age if age else None
        self.team = team if team else None
        self.league = league if league else None
        self.position = position if position else None
        self.games = games if games else None
        self.games_started = games_started if games_started else None
        self.minutes_played = minutes_played if minutes_played else None
        self.field_goals = field_goals if field_goals else None
        self.field_goal_attempts = field_goal_attempts if field_goal_attempts else None
        self.field_goal_percentage = field_goal_percentage if field_goal_percentage else None
        self.three_pointers = three_pointers if three_pointers else None
        self.three_point_attempts = three_point_attempts if three_point_attempts else None
        self.three_point_percentage = three_point_percentage if three_point_percentage else None
        self.two_pointers = two_pointers if two_pointers else None
        self.two_point_attempts = two_point_attempts if two_point_attempts else None
        self.two_point_percentage = two_point_percentage if two_point_percentage else None
        self.effective_field_goal_percentage = effective_field_goal_percentage if effective_field_goal_percentage else None
        self.free_throws = free_throws if free_throws else None
        self.free_throw_attempts = free_throw_attempts if free_throw_attempts else None
        self.free_throw_percentage = free_throw_percentage if free_throw_percentage else None
        self.offensive_rebound_total = offensive_rebound_total if offensive_rebound_total else None
        self.defensive_rebound_total = defensive_rebound_total if defensive_rebound_total else None
        self.rebound_total = rebound_total if rebound_total else None
        self.assists = assists if assists else None
        self.steals = steals if steals else None
        self.blocks = blocks if blocks else None
        self.turnovers = turnovers if turnovers else None
        self.personal_fouls = personal_fouls if personal_fouls else None
        self.points = points if points else None
        

    def __repr__(self):
        return 'Per game Stats: %s' % self.name
