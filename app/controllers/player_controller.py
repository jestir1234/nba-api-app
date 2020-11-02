from app.models.player import Player
import json

def get_player_by_id(request, session, player_id):
    # EP get player by player id #

    player = session.query(Player).filter(
        Player.id == player_id
    ).first()

    return player.toJSON()