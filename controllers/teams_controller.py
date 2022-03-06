import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from services.database import db

from models.team import Team

import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

teams_blueprint = Blueprint("teams", __name__)


# All Teams
@teams_blueprint.route('/teams')
def teams():
    teams = Team.query.order_by(Team.name).all()
  
    return render_template('teams/index.html', teams=teams)

@teams_blueprint.route('/teams/<id>', methods = ['GET'])
def show(id):
    team = Team.query.filter(Team.id==id).one_or_none()
    return render_template('teams/show.html', team=team)

# CREATE
#Create new Game
# dfjkasdbfkj
@teams_blueprint.route("/teams/new", methods=['GET'])
def new_team():
    teams = Team.query.all()

    return render_template("teams/new.html", teams=teams)


#Post New Game
@teams_blueprint.route("/teams",  methods=['POST'])
def create_team():
    if request.method == 'POST':
        team_name = request.form['team_name']
        team_points = int(request.form['team_points'])
        team_group_id = int(request.form['group_id'])
        if team_name == '':
            return render_template('teams/new.html')
        if db.session.query(Team).filter(Team.name == team_name).count() == 0:
            data = Team(team_name, team_points, team_group_id)
            db.session.add(data)
            db.session.commit()
            return redirect('/teams')
        return render_template('teams/new.html')


# EDIT GET
@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_game(id):
    team = Team.query.filter(Team.id==id).one_or_none()
    return render_template('teams/edit.html', team=team)

# EDIT POST
@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_game(id):
    team_to_update = Team.query.filter(Team.id==id).one_or_none()
    if request.method == 'POST':
        team_to_update.name = team_to_update.name
        team_to_update.points = request.form['team_points']
        team_to_update.group_id = request.form['group_id']
        try:
            db.session.commit()
            return redirect('/teams')
        except:
            print("error")
            return redirect('/teams')
          
    return render_template('teams/edit.html')

#DELETE
@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    teams = Team.query.order_by(Team.name).all()
    team = Team.query.filter(Team.id==id).one_or_none()
    try:
        db.session.delete(team)
        db.session.commit()
        return redirect('/teams')
    except:
        return redirect('/teams')


    





