from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.team import Team

import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

teams_blueprint = Blueprint("teams", __name__)


# All Teams

@teams_blueprint.route('/teams')
def teams():
    teams = team_repository.list_all()
    return render_template('teams/index.html', teams=teams)

@teams_blueprint.route('/teams/<id>', methods = ['GET'])
def show(id):
    team = team_repository.select(id)
    return render_template('teams/show.html', team=team)

# CREATE
#Create new Game
@teams_blueprint.route("/teams/new", methods=['GET'])
def new_team():
    teams = team_repository.list_all()
    return render_template("teams/new.html", teams=teams)


#Post New Game
@teams_blueprint.route("/teams",  methods=['POST'])
def create_team():
    name = request.form['team_name']
    points = int(request.form['team_points'])
    group_id = int(request.form['group_id'])
    team = Team(name, points, group_id)
    team_repository.save(team)
    return redirect('/teams')


#DELETE
@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')
