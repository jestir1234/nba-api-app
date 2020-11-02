from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from app.database import Base
import json

class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    year_start = Column(Integer, nullable=False)
    year_end = Column(Integer, nullable=True)
    position = Column(String(255), nullable=False)
    height = Column(String(255), nullable=False)
    weight = Column(String(255), nullable=False)
    birth_date = Column(DateTime, nullable=True)
    college = Column(String(255), nullable=True)
    __table_args__ = (UniqueConstraint('name', 'year_start',
                                       'position', name='unique_player_name_position'),)


    def __init__(self, name, year_start, year_end, position, height, weight, birth_date, college):
        self.name = name
        self.year_start = year_start
        self.year_end = year_end
        self.position = position
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.college = college

    def __repr__(self):
        return 'Player: %s' % self.name

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'year_start' : self.year_start,
            'year_end' : self.year_end,
            'position' : self.position,
            'height' : self.height,
            'weight' : self.weight,
            'birth_date' : self.birth_date,
            'college' : self.college
        }
