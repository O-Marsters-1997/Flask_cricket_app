import pdb
from db.run_sql import run_sql

from models.team import Team

def list_all():
    teams = []
    sql = 'SELECT * FROM group_1_teams UNION SELECT * FROM group_2_teams  ORDER BY name ASC'
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'], row['id'])
        teams.append(team)
    return teams


def select(id):
    sql = 'SELECT * FROM group_1_teams UNION SELECT * FROM group_2_teams WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['points'], result['id'])

    return team