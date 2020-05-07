from flask import Flask, request
from db import db
import dao
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
def get_player_by_id(player_id):
    player = dao.get_player_by_id(player_id)
    return success_response(player)


@app.route('/api/players/', methods=['POST'])
def create_player():
    body = json.loads(request.data)
    new_player = dao.create_player(
        username=body.get('username')
    )
    return success_response(new_player, 201)


@app.route('/api/players/<int:player_id>/', methods=['POST'])
def change_player_name(player_id):
    body = json.loads(request.data)
    player = dao.change_player_name(player_id, body.get('new_name'))
    return success_response(player, 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
