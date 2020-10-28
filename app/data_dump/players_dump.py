import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.environment import get_sqlalchemy_db_uri
from sqlalchemy import exc
from app.models.player import Player
import datetime
from fastapi import FastAPI

app = FastAPI()

Engine = create_engine(
    get_sqlalchemy_db_uri(),
    pool_pre_ping=True
)

session = sessionmaker(autocommit=False, bind=Engine)

db = session()

with open('player_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            try: 
                line_count += 1
                date = datetime.datetime.strptime('{0} {1}'.format(
                    row[6].replace(',', ''), '7:40'), '%B %d %Y %H:%M') if row[6] else None
                player = db.query(Player).filter(Player.name == row[0]).first()
                if player:
                    print('Player already exists: ', player.name)
                    continue

                new_player = Player(
                    row[0],
                    int(row[1]),
                    int(row[2]),
                    row[3],
                    row[4],
                    row[5],
                    date,
                    row[7]
                )
                db.add(new_player)
                db.commit()
                db.refresh(new_player)
            except exc.SQLAlchemyError as e:
                print(e)
    
    print('Completed data dump for players')
