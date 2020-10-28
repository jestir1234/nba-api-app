import csv
from fastapi import FastAPI
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from app.environment import get_sqlalchemy_db_uri
from app.models.per_game import PerGame
from app.models.player import Player
import datetime

app = FastAPI()

Engine = create_engine(
    get_sqlalchemy_db_uri(),
    pool_pre_ping=True
)

session = sessionmaker(autocommit=False, bind=Engine)

db = session()

row_preview = None

int_columns = {
    '2',
    '8'
}

def get_headers():
    headers = []
    with open('per_game_stats.csv') as csv_file:
        for idx, line in enumerate(csv_file):
            if idx == 0:
                column_headers = line.split(',')
                for col in column_headers:
                    headers.append(col)
        return headers

with open('per_game_stats.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    headers = get_headers()
    print('headers', headers)
    for row in csv_reader:
        print('row', row)
        if line_count == 0:
            line_count += 1
            continue
        else:
            line_count += 1
            if row[1] == '':  # row is empty
                continue
            player = db.query(Player).filter(Player.name == row[0]).first()
            season_stat = db.query(PerGame).filter(
                and_(
                    PerGame.name == row[0],
                    PerGame.season == row[1]
                )
            ).first()

            if season_stat:
                print('Season already exists: ',
                      season_stat.name, season_stat.season)
                continue

            print('line_count', line_count)
            args = [player.id if player else None]

            for idx, col in enumerate(headers):
                if idx > len(row) - 1:
                    args.append(None)
                    continue
                print('row[{0}]: {1}'.format(idx, row[idx]))
                if idx in int_columns:  # converts ints for
                    args.append(int(row[idx]) if row[idx] else None)
                else:
                    args.append(row[idx])

            new_per_game = PerGame(*args)
            db.add(new_per_game)
            db.commit()
            db.refresh(new_per_game)

    print('completed data dump of per_game')
