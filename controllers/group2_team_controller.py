from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.team import Team
import repositories.group_2_team_repository as group_2_team_repository

import repositories.group_2_game_repository as group_2_game_repository

books_blueprint = Blueprint("books", __name__)
