from services.database import db
from models.game import Game

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique = True, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, points, group_id, id=None):
        self.name = name
        self.points = points
        self.group_id = group_id
        self.id = id
      
        
    def victory(self, team):
        team.points +=2