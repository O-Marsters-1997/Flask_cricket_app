import pdb
from app import app
from models import game
from models.team import Team
from models.game import Game
from services.database import db


with app.app_context():

    db.session.query(Team).delete()
    db.session.query(Game).delete()

    team1 = Team('Afghanistan',0, 2)
    db.session.add(team1)
    db.session.commit()

    team2 = Team('Australia', 0, 1)
    db.session.add(team2)
    db.session.commit()

    team3 = Team('Bangladesh', 0, 1)
    db.session.add(team3)
    db.session.commit()

    team4 = Team('England', 0, 1)
    db.session.add(team4)
    db.session.commit()

    team5 = Team('India', 0, 2)
    db.session.add(team5)
    db.session.commit()

    team6 = Team('Namibia', 0, 2)
    db.session.add(team6)
    db.session.commit()

    team7 = Team('New Zealand', 0, 2)
    db.session.add(team7)
    db.session.commit()

    team8 = Team('Pakistan', 0, 2)
    db.session.add(team8)
    db.session.commit()

    team9 = Team('Ireland',0, 2)
    db.session.add(team9)
    db.session.commit()

    team10 = Team('South Africa', 0, 1)
    db.session.add(team10)
    db.session.commit()

    team11 = Team('Sri Lanka', 0, 1)
    db.session.add(team11)
    db.session.commit()

    team12 = Team('West Indies', 0, 1)
    db.session.add(team12)
    db.session.commit()