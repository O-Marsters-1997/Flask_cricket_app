import pdb
from db.run_sql import run_sql

from models.team import Team
from models.game import Game

import repositories.group_1_team_repository as group_1_team_repository
import repositories.group_2_team_repository as group_2_team_repository

import repositories.group_1_game_repository as group_1_game_repository
import repositories.group_2_team_repository as group_2_game_repository


def save(game):
    sql = 'INSERT INTO group_1_games (team_1_id, team_2_id, team_1_runs, team_2_runs) VALUES (%s, %s, %s, %s) RETURNING *'
    values = [game.team_1.id, game.team_2.id, game.team_1_runs, game.team_2_runs]

    results = run_sql(sql, values)
    id =results[0]['id']
    game.id = id
    return game


def delete_all():
    sql = 'DELETE FROM group_1_games'
    run_sql(sql)
