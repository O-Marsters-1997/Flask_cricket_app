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
