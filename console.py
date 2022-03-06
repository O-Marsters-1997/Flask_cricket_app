import pdb
from models import game
from models.team import Team
from models.game import Game
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository


game_repository.delete_all()
team_repository.delete_all()

team1 = Team('Afghanistan',4, 2)
team_repository.save(team1)
team2 = Team('Astralia', 0, 1)
team_repository.save(team2)

team3 = Team('Bangladesh', 0, 1)
team_repository.save(team3)
team4 = Team('England', 0, 1)
team_repository.save(team4)
team5 = Team('India', 0, 2)
team_repository.save(team5)
team6 = Team('Namibia', 0, 2)
team_repository.save(team6)

team7 = Team('New Zealand', 0, 2)
team_repository.save(team7)
team8 = Team('Pakistan', 0, 2)
team_repository.save(team8)
team9 = Team('Ireland',0, 2)
team_repository.save(team9)
team10 = Team('South Africa', 0, 1)
team_repository.save(team10)
team11 = Team('Sri Lanka', 0, 1)
team_repository.save(team11)
team12 = Team('West Indies', 0, 1)
team_repository.save(team12)