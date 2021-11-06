from models.team import Team

import repositories.team_repository as team_repository

team1 = Team('Australia')
team_repository.save(team1)