from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


match_association = db.Table('playermatch',
                             db.Column('player_id', db.Integer, db.ForeignKey('player_table.id')),
                             db.Column('match_id', db.Integer, db.ForeignKey('match_table.id')))


class Guild(db.Model):
    __tablename__ = "guild_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    members = db.relationship("Player", back_populates="guild")

    def serialize(self):  # TODO implement nested serialization
        return {
            'name': self.name
        }


class Player(db.Model):
    __tablename__ = "player_table"
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String)

    guild_id = db.Column(db.Integer, db.ForeignKey(Guild.id))

    guild = db.relationship("Guild", back_populates="members")
    matches = db.relationship("Match", secondary=match_association, back_populates="players")

    def serialize(self):  # TODO implement nested serialization
        return {
            'username': self.username,
            'name': self.name
        }


class Match(db.Model):
    __tablename__ = "match_table"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.Integer, db.ForeignKey('player_table.id'))

    players = db.relationship("Player", secondary=match_association, back_populates="matches")

    def serialize(self):  # TODO implement nested serialization
        return {
            'status': self.value
        }
