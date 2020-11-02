from pydantic import BaseModel, PositiveInt
from datetime import datetime

class Player(BaseModel):
    id: PositiveInt
    name: str = None
    year_start = PositiveInt
    year_end = PositiveInt
    position: str = None
    height: str = None
    weight: str = None
    birth_date: datetime = None
    college: str = None