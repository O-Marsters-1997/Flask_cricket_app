import pdb
from db.run_sql import run_sql

from models.team import Team
from models.game import Game

import repositories.group_1_team_repository as group_1_team_repository
import repositories.group_2_team_repository as group_2_team_repository

import repositories.group_1_game_repository as group_1_game_repository
import repositories.group_2_team_repository as group_2_game_repository

#Select game
def select(id):
    sql = 'SELECT * FROM group_1_games WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        game = Game(result['team_1'], result['team_2'], result['team_1_runs'], result['team_2_runs'])
    return game

#Select all games
def sec_all():
    games = []
    sql = 'SELECT * FROM group_1_games'

# Create game
def save(game):
    sql = 'INSERT INTO group_1_games (team_1_id, team_2_id, team_1_runs, team_2_runs, game_date) VALUES (%s, %s, %s, %s, %s) RETURNING *'
    values = [game.team_1.id, game.team_2.id, game.team_1_runs, game.team_2_runs, game.game_date]

    results = run_sql(sql, values)
    id =results[0]['id']
    game.id = id
    return game

#Delete game

# Delete all games

def delete_all():
    sql = 'DELETE FROM group_1_games'
    run_sql(sql)
