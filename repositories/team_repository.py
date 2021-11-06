import pdb
from db.run_sql import run_sql

from models.team import Team
# from models.game import Game

# import repositories.game_repository as game_repository


def save(team):
    sql = "INSERT INTO teams (name) VALUES (%s) RETURNING *"
    values = [team.name]
    results = run_sql(sql, values)
    # pdb.set_trace()
    id = results[0]['id']
    team.id = id
    return team
