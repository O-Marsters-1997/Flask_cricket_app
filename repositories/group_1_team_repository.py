import pdb
from db.run_sql import run_sql

from models.team import Team
# from models.game import Game

# import repositories.game_repository as game_repository


def save(team):
    sql = "INSERT INTO group_1_teams (name) VALUES (%s) RETURNING *"
    values = [team.name]
    results = run_sql(sql, values)
    # pdb.set_trace()
    id = results[0]['id']
    team.id = id
    return team

def select(id):
    sql = 'SELECT * FROM group_1_teams WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['points'], result['id'])
    return team


def select_all():
    teams = []
    sql = 'SELECT * FROM group_1_teams'
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'], row['id'])
        teams.append(team)
    return teams


def delete_all():
    sql = 'DELETE FROM group_1_teams'
    run_sql(sql)
