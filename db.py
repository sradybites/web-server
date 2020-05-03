from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PlayerMatch(db.Model):
    __tablename__ = "match_association"
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player_table.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('match_table.id'))
    team = db.Column(db.Boolean)

    player = db.relationship('Player', back_populates="matches")
    match = db.relationship('Match', back_populates="team1")


class Player(db.Model):
    __tablename__ = "player_table"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    bio = db.Column(db.String)
    joindate = db.Column(db.DateTime, nullable=False)
    matches = db.relationship("PlayerMatch", back_populates="player")

    def serialize(self):
        return {
            'username': self.username
        }


class Match(db.Model):
    __tablename__ = "match_table"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean)
    team1 = db.relationship("PlayerMatch", back_populates="match")
    team2 = db.relationship("PlayerMatch", back_populates="match")
    team1_score = db.Column(db.Integer, nullable=False)
    team2_score = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'status': self.value
        }


class Guild(db.Model):
    # might not actually implement guilds, we'll see
    # for now, functions as a voluntary grouping of Players
    __tablename__ = "guilds"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
