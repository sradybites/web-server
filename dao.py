from db import *


def get_all_players():
    return [p.serialize() for p in Player.query.all()]


def create_player(username):
    new_player = Player(
        username=username
    )
    db.session.add(new_player)
    db.session.commit()
    return new_player.serialize()


def get_player_by_id(player_id):
    player = Player.query.filter_by(id=player_id).first()
    if player is None:
        return None
    return player.serialize()


def delete_player(player_id):
    player = Player.query.filter_by(id=player_id).first()
    if player is None:
        return None
    db.session.delete(player)
    db.session.commit()
    return player.serialize()
