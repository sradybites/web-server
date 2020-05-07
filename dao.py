from db import *
from consts import *


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


def change_player_name(player_id, new_name):
    player = Player.query.filter_by(id=player_id).first()
    if player.name == new_name:
        return None
    player.name = new_name
    db.session.commit()
    return player.serialize()


def get_all_guilds():
    return[g.serialize() for g in Guild.query.all()]


def create_guild(name):
    new_guild = Guild(
        name=name
    )
    db.session.add(new_guild)
    db.session.commit()
    return new_guild.serialize()


def get_guild_by_id(guild_id):
    guild = Guild.query.filter_by(id=guild_id).first()
    if guild is None:
        return None
    return guild.serialize()


def add_player_to_guild(player_id, guild_id):
    guild = Guild.query.filter_by(id=guild_id).first()
    if guild is None:
        return None
    player = Player.query.filter_by(id=player_id).first()
    guild.members.append(player)
    player.guild = guild
    db.session.commit()
    return player.serialize()


def remove_player_from_guild(player_id, guild_id):
    guild = Guild.query.filter_by(id=guild_id).first()
    player = Player.query.filter_by(id=player_id, guild_id=guild_id).first()
    if player is None:
        return None
    guild.members.delete(player)
    player.guild = db.sql.null()
    db.session.commit()
    return player.serialize()


def rename_guild(new_name, guild_id):
    guild = Guild.query.filter_by(id=guild_id).first()
    if guild.name == new_name:
        return None
    guild.name = new_name
    return guild.serialize()


def delete_guild(guild_id):
    guild = Guild.query.filter_by(id=guild_id).first()
    if guild is None:
        return None
    db.session.delete(guild)
    db.session.commit()
    return guild.serialize()


def initialize_match(player_id):
    player1 = Player.query.filter_by(id=player_id).first()
    new_match = Match(status=MATCH_INIT)
    new_match.players.append(player1)
    db.session.add(new_match)
    db.session.commit()
    return new_match.serialize()


def add_player_to_match(player_id, match_id):
    player2 = Player.query.filter_by(id=player_id).first()
    match = Match.query.filter_by(id=match_id).first()
    if match is None:
        return None
    match.players.append(player2)
    db.session.commit()
    return match.serialize()


def start_match(match_id):
    match = Match.query.filter_by(id=match_id).first()
    if match is None:
        return None
    match.status = MATCH_ACTIVE
    db.session.commit()


def end_match(match_id, winner_id):
    match = Match.query.filter_by(id=match_id).first()
    if match is None:
        return None
    match.status = MATCH_DONE
    match.winner = winner_id
    db.session.commit()
    return match.serialize()


def get_match_by_id(match_id):
    match = Match.query.filter_by(id=match_id).first()
    if match is None:
        return None
    return match.serialize()


def delete_match_by_id(match_id):
    match = Match.query.filter_by(id=match_id.first())
    if match is None:
        return None
    db.session.delete(match)
    db.session.commit()
    return match.serialize()


def get_matches(filter_const=None):
    """
    Returns a serialized list of all matches unless filter_const is specified.
    :param filter_const: a global variable from consts beginning with 'MATCH'
    :return: list of JSON serialized Match objects
    """
    if filter_const is None:
        return [m.serialize() for m in Match.query.all()]
    return [m.serialize() for m in Match.query.filter_by(status=filter_const).all()]
