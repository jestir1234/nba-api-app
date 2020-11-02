from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint, Float, ForeignKey, VARCHAR
from app.database import Base


class Advanced(Base):
    __tablename__ = 'advanced'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=True)
    name = Column(VARCHAR(255), nullable=False)
    season = Column(String(255), nullable=True)
    age = Column(Integer, nullable=True)
    team = Column(String(255), nullable=True)
    league = Column(String(255), nullable=True)
    position = Column(String(255), nullable=True)
    games = Column(String(255), nullable=True)
    minutes_played = Column(Integer, nullable=True)
    per = Column(Float, nullable=True)
    ts = Column(Float, nullable=True)
    three_point_attempt_rate = Column(Float, nullable=True)
    free_throw_attempt_rate = Column(Float, nullable=True)
    orb = Column(Float, nullable=True)
    drb = Column(Float, nullable=True)
    trb = Column(Float, nullable=True)
    ast = Column(Float, nullable=True)
    stl = Column(Float, nullable=True)
    blk = Column(Float, nullable=True)
    tov = Column(Float, nullable=True)
    usg = Column(Float, nullable=True)
    ows = Column(Float, nullable=True)
    dws = Column(Float, nullable=True)
    ws = Column(Float, nullable=True)
    ws_48 = Column(Float, nullable=True)
    obpm = Column(Float, nullable=True)
    dbpm = Column(Float, nullable=True)
    bpm = Column(Float, nullable=True)
    vorp = Column(Float, nullable=True)

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
        minutes_played,
        per,
        ts,
        three_point_attempt_rate,
        free_throw_attempt_rate,
        orb,
        drb,
        trb,
        ast,
        stl,
        blk,
        tov,
        usg,
        ows,
        dws,
        ws,
        ws_48,
        obpm,
        dbpm,
        bpm,
        vorp):
        self.player_id = player_id if player_id else None
        self.name = name if name else None
        self.season = season if season else None
        self.age = age if age else None
        self.team = team if team else None
        self.league = league if league else None
        self.position = position if position else None
        self.games = games if games else None
        self.minutes_played = minutes_played if minutes_played else None
        self.per = per if per else None
        self.ts = ts if ts else None
        self.three_point_attempt_rate = three_point_attempt_rate if three_point_attempt_rate else None
        self.free_throw_attempt_rate = free_throw_attempt_rate if free_throw_attempt_rate else None
        self.orb = orb if orb else None
        self.drb = drb if drb else None
        self.trb = trb if trb else None
        self.ast = ast if ast else None
        self.stl = stl if stl else None
        self.blk = blk if blk else None
        self.tov = tov if tov else None
        self.usg = usg if usg else None
        self.ows = ows if ows else None
        self.dws = dws if dws else None
        self.ws = ws if ws else None
        self.ws_48 = ws_48 if ws_48 else None
        self.obpm = obpm if obpm else None
        self.dbpm = dbpm if dbpm else None
        self.bpm = bpm if bpm else None
        self.vorp = vorp if vorp else None
        

    def __repr__(self):
        return 'Advanced Stats: %s' % self.name
