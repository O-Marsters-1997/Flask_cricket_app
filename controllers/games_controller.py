import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from sqlalchemy import or_
from db.run_sql import run_sql
from services.database import db
from models.game import Game
from models.team import Team
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository


games_blueprint = Blueprint("games", __name__)

# List all games
# All Teams
@games_blueprint.route('/games')
def games():
    games = Game.query.order_by(Game.game_date).all()
    return render_template('games/index.html', games=games)

@games_blueprint.route('/games/<id>', methods = ['GET'])
def show(id):
    game = Game.query.filter(Game.id==id).one_or_none()
    team1 = game.team_1
    team2 = game.team_2
    return render_template('games/show.html', game=game, team_1=team1, team_2=team2)

#SHOW ONE GAME
@games_blueprint.route("/games/new", methods=['GET'])
def new_game():
    teams = Team.query.order_by(Team.name).all()
    games = Game.query.order_by(Game.game_date).all()
    return render_template('games/new.html', games=games, teams=teams)

#CREATE NEW GAME
#Post New Game
@games_blueprint.route("/games",  methods=['POST'])
def create_team():
    teams = Team.query.order_by(Team.name).all()
    if request.method == 'POST':
        team_1 = request.form['team_1']
        print(team_1)
        team_2 = request.form['team_2']
        print(team_2)
        team_1_runs = int(request.form['team_1_runs'])
        team_2_runs = int(request.form['team_2_runs'])
        game_date = request.form['game_date']
        # if team_1 or team_2 == '':
        #     print("hello")
        #     return render_template('games/new.html')
        data = Game(team_1, team_2, team_1_runs, team_2_runs, game_date)
        print(data)
        db.session.add(data)

        team_1_update = Team.query.filter(Team.name==team_1).one_or_none()
        team_2_update = Team.query.filter(Team.name==team_2).one_or_none()

        if team_1_runs > team_2_runs:
            team_1_update.points +=2
        elif team_2_runs > team_1_runs:
            team_2_update.points +=2
        else:
            team_1_update.points +=1
            team_2_update.points +=1
        db.session.commit()
        return redirect('/games')
    return render_template('games/new.html', teams=teams)



#Show games associated with team
@games_blueprint.route("/team-games/<id>", methods=['GET'])
def show_game_for_team(id):
    team = Team.query.filter(Team.id == id).one_or_none()
    games = Game.query.filter(or_(Game.team_1 == team.name, Game.team_2 == team.name))
    print(games)
    # games = games1 + games2
    return render_template('games/team.html', games = games)



# EDIT GET
@games_blueprint.route("/games/<id>/edit", methods=['GET'])
def edit_game(id):
    game = Game.query.filter(Game.id==id).one_or_none()
    teams = Team.query.order_by(Team.name).all()
    return render_template('games/edit.html', teams=teams, game=game)

# EDIT POST
# @games_blueprint.route("/games/<id>", methods=['POST'])
# def update_game(id):
#     team_1 = team_repository.select(request.form['team_1_id'])
#     team_2 = team_repository.select(request.form['team_2_id'])
#     team_1_runs = request.form['team_1_runs']
#     team_2_runs = request.form['team_2_runs']
#     game_date = request.form['game_date']

#     game = Game(team_1, team_2, team_1_runs, team_2_runs, game_date, id)
#     game_repository.update(game)
#     return redirect('/games')

# EDIT POST
@games_blueprint.route("/games/<id>", methods=['POST'])
def update_game(id):
    game_to_update = Game.query.filter(Game.id==id).one_or_none()
    if request.method == 'POST':
        game_to_update.team_1 = game_to_update.team_1
        game_to_update.team_2 = game_to_update.team_2
        game_to_update.team_1_runs = request.form['team_1_runs']
        game_to_update.team_2_runs = request.form['team_2_runs']
        game_to_update.game_date = request.form['game_date']
        try:
            db.session.commit()
            return redirect('/games')
        except:
            print("error")
            return redirect('/games')
          
    return render_template('games/edit.html')


#DELETE
@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_team(id):
    games = Game.query.all()
    game = Game.query.filter(Game.id==id).one_or_none()
    team_1_update = Team.query.filter(Team.name==game.team_1).one_or_none()
    team_2_update = Team.query.filter(Team.name==game.team_2).one_or_none()

    try:
        db.session.delete(game)
        db.session.commit()
        if game.team_1_runs > game.team_2_runs:
            team_1_update.points -=2
        elif game.team_2_runs > game.team_1_runs:
            team_2_update.points -=2
        else:
            team_1_update.points -= 1
            team_2_update.points -= 1
        db.session.commit()
        return redirect('/games')
    except:
        return redirect('/games')
    
    
