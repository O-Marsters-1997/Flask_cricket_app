from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository


# List all games
games_blueprint = Blueprint("games", __name__)

@games_blueprint.route('/games')
def games():
    games = game_repository.sort_games_date()
    return render_template('games/index.html', games=games)

#Create new Game
# NEW
# GET '/games/new'
@games_blueprint.route("/games/new", methods=['GET'])
def new_game():
    teams = team_repository.select_all()
    return render_template("games/new.html", teams=teams)


# CREATE
# POST '/games'
@games_blueprint.route("/games",  methods=['POST'])
def create_game():
    team_1 = team_repository.select(request.form['team_1_id'])
    team_2 = team_repository.select(request.form['team_2_id'])
    team_1_runs = request.form['team_1_runs']
    team_2_runs = request.form['team_2_runs']
    game_date = request.form['game_date']
    game = Game(team_1, team_2, team_1_runs, team_2_runs, game_date)

    game_repository.save(game)
    return redirect('/games')


# SHOW
# GET '/books/<id>'
@games_blueprint.route("/games/<id>", methods=['GET'])
def show_game(id):
    game = game_repository.select(id)
    return render_template('games/show.html', game=game)

# EDIT
# GET '/books/<id>/edit'
@games_blueprint.route("/games/<id>/edit", methods=['GET'])
def edit_game(id):
    game = game_repository.select(id)
    teams = team_repository.select_all()
    return render_template('games/edit.html', teams=teams, game=game)
