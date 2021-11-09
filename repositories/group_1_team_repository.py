import pdb
from db.run_sql import run_sql

from models.team import Team
from models.game import Game

# import repositories.game_repository as game_repository


def save(team):
    sql = "INSERT INTO group_1_teams (name, points) VALUES (%s, %s) RETURNING *"
    values = [team.name, team.points]
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


def sort_teams_rank(group):
    teams = []
    # pdb.set_trace()
    sql = 'SELECT * FROM group_1_teams  ORDER BY points DESC'
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'], row['id'])
        teams.append(team)
    return teams

#No delete (does not make sense)

#Delete all
def delete_all():
    sql = 'DELETE FROM group_1_teams'
    run_sql(sql)


def games(team):
    games = []
    sql_1 = 'SELECT * FROM group_1_games WHERE %s in (team_1_id, team_2_id)'
    values = [team.id]

    results_1 = run_sql(sql_1, values)
    for row in results_1:
        game = Game(row['team_1_id'], row['team_2_id'], row['team_1_runs'], row['team_2_runs'], row['game_date'], row['id'])
        games.append(game) 

    return games

