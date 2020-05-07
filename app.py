from flask import Flask, request
from db import db
import dao
from consts import *
import json

app = Flask(__name__)
db_filename = "BFPDB.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


### base serialized responses ###
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


### ROUTES ###
@app.route('/api/players/')
def get_all_players():
    return success_response(dao.get_all_players())


@app.route('/api/players/<int:player_id>/')
def get_player(player_id):
    player = dao.get_player_by_id(player_id)
    if player is None:
        return failure_response("Player not found")
    return success_response(player)


@app.route('/api/players/', methods=['POST'])
def create_player():
    body = json.loads(request.data)

    # validate parameters for character creation
    username = body.get('username')
    if username is None or not isinstance(username, str) or len(username) > 10 or len(username) < 1:
        return failure_response("Invalid username", 400)

    # DAO handles duplicate username
    new_player = dao.create_player(
        username=username
    )
    if new_player is None:
        return failure_response("Username is taken", 422)
    return success_response(new_player, 201)


@app.route('/api/players/<int:player_id>/', methods=['PUT'])
def change_player_name(player_id):
    body = json.loads(request.data)

    # validate name param, duplicates allowed
    new_name = body.get('new_name')
    if new_name is None or not isinstance(new_name, str) or len(new_name) > 15 or len(new_name) < 1:
        return failure_response("Invalid name", 400)
    player = dao.change_player_name(player_id, new_name)
    if player is None:
        return failure_response("Choose a name different from your current one", 400)
    return success_response(player, 201)


@app.route('/api/players/<int:player_id>/', methods=['DELETE'])
def delete_player(player_id):
    player = dao.delete_player(player_id)
    if player is None:
        return failure_response("Player not found")
    return success_response(player, 204)


@app.route('/api/guilds/')
def get_all_guilds():
    return success_response(dao.get_all_guilds())


@app.route('/api/guilds/', methods=['POST'])
def create_guild():
    body = json.loads(request.data)

    # validate name param
    name = body.get('name')
    if name is None or not isinstance(name, str) or len(name) > 15 or len(name) < 1:
        return failure_response("Invalid name", 400)

    new_guild = dao.create_guild(name=name)
    if new_guild is None:
        return failure_response("Guild name taken", 422)
    return success_response(new_guild, 201)


@app.route('/api/guilds/<int:guild_id>/', methods=['GET', 'PUT', 'DELETE'])
def manage_guild(guild_id):
    if request.method == 'GET':
        guild = dao.get_guild_by_id(guild_id)
        if guild is None:
            return failure_response("Guild not found")
        return success_response(guild)
    elif request.method == 'PUT':
        body = json.loads(request.data)
        res = dao.rename_guild(guild_id, body.get('new_name'))
        if res is None:
            return failure_response("Guild name already in use", 422)
        return success_response(res, 201)
    elif request.method == 'DELETE':
        guild = dao.delete_guild(guild_id)
        if guild is None:
            failure_response("Guild not found")
        return success_response(guild, 204)


@app.route('/api/guilds/<int:guild_id>/members/', methods=['PUT', 'DELETE'])
def modify_guild_membership(guild_id):
    if request.method == 'PUT':
        body = json.loads(request.data)
        res = dao.add_player_to_guild(body.get('player_id'), guild_id)
        if res is None:
            return failure_response("Guild not found")
        return success_response(res, 201)
    elif request.method == 'DELETE':
        body = json.loads(request.data)
        res = dao.remove_player_from_guild(body.get('player_id'), guild_id)
        if res is None:
            return failure_response("Player either not found, or not a member", 422)
        return success_response(res, 204)


@app.route('/api/matches/', methods=['POST'])
def create_match():
    body = json.loads(request.data)
    return success_response(dao.initialize_match(body.get('player_id')))


@app.route('/api/matches/<int:match_id>/join', methods=['PUT'])
def join_match(match_id):
    body = json.loads(request.data)

    # TODO embed in a try-catch block
    res = dao.add_player_to_match(body.get('player_id'), match_id)
    if res is None:
        return failure_response("Something went wrong", 400)
    return success_response(res)


@app.route('/api/matches/<int:match_id>/start', methods=['PUT'])
def start_match(match_id):
    res = dao.start_match(match_id)
    if res is None:
        return failure_response("Match could not be started", 400)
    return success_response(res)


@app.route('/api/matches/<int:match_id>/winner', methods=['PUT'])
def end_match(match_id):
    body = json.loads(request.data)
    res = dao.end_match(match_id, body.get('winner_id'))
    if res is None:
        return failure_response("Match failed to complete", 400)
    return success_response(res)


@app.route('/api/matches/<int:match_id>/', methods=['GET', 'DELETE'])
def manage_match(match_id):
    if request.method == 'GET':
        match = dao.get_match_by_id(match_id)
        if match is None:
            return failure_response("Match not found")
        return success_response(match)
    elif request.method == 'DELETE':
        match = dao.delete_match_by_id(match_id)
        if match is None:
            return failure_response("Match not found")
        return success_response(match, 204)


@app.route('/api/matches/<int:filter_const>')
def get_all_matches(filter_const=None):
    if filter_const is not None and filter_const not in [MATCH_INIT, MATCH_ACTIVE, MATCH_DONE]:
        return failure_response("Invalid sort condition", 422)
    return success_response(dao.get_matches(filter_const=filter_const))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
