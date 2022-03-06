import pdb
from db.run_sql import run_sql

from models.team import Team
from models.game import Game

import repositories.team_repository as team_repository


# Create game
def save(game):
    sql = 'INSERT INTO games (team_1_id, team_2_id, team_1_runs, team_2_runs, game_date) VALUES (%s, %s, %s, %s, %s) RETURNING *'
    values = [game.team_1.id, game.team_2.id,
              game.team_1_runs, game.team_2_runs, game.game_date]

    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game


#Select game
def select(id):
    sql = 'SELECT * FROM games WHERE id = %s'
    # pdb.set_trace()
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team_1 = team_repository.select(result['team_1_id'])
        team_2 = team_repository.select(result['team_2_id'])
        game = Game(team_1, team_2,
                    result['team_1_runs'], result['team_2_runs'], result['game_date'], result['id'])
    return game


#Select all games
def select_all():
    games = []
    sql = 'SELECT * FROM games'

    results = run_sql(sql)
    for row in results:
        team_1 = team_repository.select(row['team_1_id'])
        team_2 = team_repository.select(row['team_2_id'])
        game = Game(team_1, team_2, row['team_1_runs'], row['team_2_runs'], row['game_date'], row['id'])
        games.append(game)
    return games

#Sort games
def sort_games_date():
    sorted_games = []
    sql = 'SELECT * FROM games ORDER BY game_date ASC'

    results = run_sql(sql)
    for row in results:
        team_1 = team_repository.select(row['team_1_id'])
        team_2 = team_repository.select(row['team_2_id'])
        sorted_game = Game(team_1, team_2, row['team_1_runs'], row['team_2_runs'], row['game_date'], row['id'])
        sorted_games.append(sorted_game)
    return sorted_games


#edit games
def update(game):
    sql = 'UPDATE games SET (team_1_id, team_2_id, team_1_runs, team_2_runs, game_date) = (%s, %s, %s, %s, %s) WHERE id = %s'
    values = [game.team_1.id, game.team_2.id, game.team_1_runs, game.team_2_runs, game.game_date, game.id]
    run_sql(sql, values)


#Delete game
def delete(id):
    sql = 'DELETE FROM games WHERE id = %s'
    values = [id]
    run_sql(sql, values)


def lower_points_deleted_game(game, team_1, team_2):
    sql_1 = 'SELECT team_1_runs FROM  games WHERE id = %s'
    values1 = [game.id]
    team_1_runs = run_sql(sql_1, values1)[0]
    sql_2 = 'SELECT team_2_runs FROM  games WHERE id = %s'
    values2 = [game.id]
    team_2_runs = run_sql(sql_2, values2)[0]
    if team_1_runs > team_2_runs:
        team_1.points -=2
    elif team_2_runs > team_1_runs:
        team_2.points -=2
    else:
        team_1.points -= 1
        team_2.points -= 1

    


# Delete all games
def delete_all():
    sql = 'DELETE FROM games'
    run_sql(sql)
