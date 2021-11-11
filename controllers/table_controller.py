from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository


table_blueprint = Blueprint("table", __name__)

@table_blueprint.route('/table')
def show_table():
    teams_1 = team_repository.sort_teams_rank(1)
    teams_2 = team_repository.sort_teams_rank(2)
    positions = [1,2,3,4,5,6]
    return render_template('table/index.html', teams_1=teams_1, teams_2=teams_2, positions=positions)
