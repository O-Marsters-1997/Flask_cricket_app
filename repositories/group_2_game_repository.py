import pdb
from db.run_sql import run_sql

from models.team import Team
from models.game import Game

import repositories.group_2_team_repository as group_2_team_repository


#Create game
def save(game):
    sql = 'INSERT INTO group_2_games (team_1_id, team_2_id, team_1_runs, team_2_runs, game_date) VALUES (%s, %s, %s, %s, %s) RETURNING *'
    values = [game.team_1.id, game.team_2.id,
              game.team_1_runs, game.team_2_runs, game.game_date]

    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game

#Select game
def select(id):
    sql = 'SELECT * FROM group_2_games WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        game = Game(result['team_1'], result['team_2'],
                    result['team_1_runs'], result['team_2_runs'])
    return game


#Select all games
def select_all():
    games = []
    sql = 'SELECT * FROM group_2_games'

    results = run_sql(sql)
    for row in results:
        team_1 = group_2_team_repository.select(row['team_1_id'])
        team_2 = group_2_team_repository.select(row['team_2_id'])
        game = Game(team_1, team_2, row['team_1_runs'],
                    row['team_2_runs'], row['game_date'], row['id'])
        games.append(game)
    return games

#Sort games
def sort_games_date():
    sorted_games = []
    sql = 'SELECT * FROM group_2_games ORDER BY game_date ASC'

    results = run_sql(sql)
    for row in results:
        team_1 = group_2_team_repository.select(row['team_1_id'])
        team_2 = group_2_team_repository.select(row['team_2_id'])
        sorted_game = Game(
            team_1, team_2, row['team_1_runs'], row['team_2_runs'], row['game_date'], row['id'])
        sorted_games.append(sorted_game)
    return sorted_games


#edit games
def update(game):
    sql = 'UPDATE group_2_games SET (team_1_id, team_2_id, team_1_runs, team_2_runs, game_date) = (%s, %s, %s, %s, %s) WHERE id = %s'
    values = [game.team_1.id, game.team_2.id, game.team_1_runs,
              game.team_2_runs, game.game_date, game.id]
    run_sql(sql, values)

#Delete game
def delete(id):
    sql = 'DELETE FROM group_2_games WHERE id = %s'
    values = [id]
    run_sql(sql, values)

# Delete all games
def delete_all():
    sql = 'DELETE FROM group_2_games'
    run_sql(sql)