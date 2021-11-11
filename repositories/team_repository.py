import pdb
from db.run_sql import run_sql

from models.team import Team
from models.game import Game



def save(team):
    sql = "INSERT INTO teams (name, points, group_id) VALUES (%s, %s, %s) RETURNING *"
    values = [team.name, team.points, team.group_id]
    results = run_sql(sql, values)
    # pdb.set_trace()
    id = results[0]['id']
    team.id = id
    return team

def select(id):
    sql = 'SELECT * FROM teams WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['points'], result['group_id'], result['id'])
    return team


def select_all():
    teams = []
    sql = 'SELECT * FROM teams'
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'], row['group_id'], row['id'])
        teams.append(team)
    return teams


def list_all():
    teams = []
    sql = 'SELECT * FROM teams ORDER BY name ASC'
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'], row['group_id'], row['id'])
        teams.append(team)
    return teams


def sort_teams_rank(group):
    teams = []
    # pdb.set_trace()
    sql = 'SELECT * FROM teams WHERE group_id = %s ORDER BY points DESC'
    values = [group]
    results = run_sql(sql, values)

    for row in results:
        team = Team(row['name'], row['points'], row['group_id'], row['id'])
        teams.append(team)
    return teams


def delete(id):
    sql = "DELETE  FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#Delete all
def delete_all():
    sql = 'DELETE FROM teams'
    run_sql(sql)


def update(team):
    sql = "UPDATE teams SET (name, points, group_id) = (%s, %s, %s) where id = %s"
    values = [team.name, team.points, team.group_id, team.id]
    run_sql(sql, values)

def games(team):
    games = []
    sql = 'SELECT * FROM games WHERE %s in (team_1_id, team_2_id)'
    values = [team.id]

    results = run_sql(sql, values)
    for row in results:
        team_1 = select(row['team_1_id'])
        team_2 = select(row['team_2_id'])
        game = Game(team_1, team_2,  row['team_1_runs'],
                    row['team_2_runs'], row['game_date'], row['id'])
        games.append(game)

    return games

    
