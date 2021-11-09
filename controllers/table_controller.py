from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository
import repositories.group_2_team_repository as group_2_team_repository

table_blueprint = Blueprint("table", __name__)

@table_blueprint.route('/table')
def table():
    teams_1 = team_repository.sort_teams_rank()
    teams_2 = group_2_team_repository.sort_teams_rank()
    return render_template('table/index.html', teams_1=teams_1, teams_2=teams_2)
