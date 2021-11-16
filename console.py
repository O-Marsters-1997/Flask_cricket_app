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


















#User has no control of which teams are in the league, they are pre-defined here instead!
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




# # print(team_repository.select_all())
# # print(group_2_team_repository.select_all())
# # print(team_repository.select(team5_group1.id).name)

# game_1 = Game(team1, team2, 196, 1900, '1970-01-01')
# game_repository.save(game_1)
# game_2 = Game(team1, team2, 186, 110, '1970-01-01')
# game_repository.save(game_2)


# team_repository.games(team1)

# game_repository.select(game_1.id)
# print(game_1.team_1.points)
# print(game_1.team_2.points)
# game_repository.lower_points_deleted_game(game_1, game_1.team_1, game_1.team_2)
# print(game_1.team_1.points)
# print(game_1.team_2.points)

# game_2_group_1 = Game(team3_group1, team4_group1, 160, 140, '1980-01-01 00:00:00.00')
# group_1_game_repository.save(game_2_group_1)
# game_3_group_1 = Game(team5_group1, team6_group1, 85, 86, '1945-01-01 00:00:00.00')
# group_1_game_repository.save(game_3_group_1)
# game_4_group_1 = Game(team1_group1, team3_group1, 220, 45, '1820-01-01 00:00:00.00')
# group_1_game_repository.save(game_4_group_1)
# game_5_group_1 = Game(team2_group1, team4_group1, 135, 136, '2019-01-08 00:00:00.00')
# group_1_game_repository.save(game_5_group_1)
# game_6_group_1 = Game(team1_group1, team6_group1, 135, 136, '2019-01-08 00:00:00.00')
# group_1_game_repository.save(game_6_group_1)
# game_7_group_1 = Game(team5_group1, team1_group1, 135, 136, '2019-01-08 00:00:00.00')
# group_1_game_repository.save(game_7_group_1)



# game_5_group_1 = Game(team2_group1, team1_group1, 135, 136, '2000-01-08 00:00:00.00')
# group_1_game_repository.update(game_5_group_1)


# games = team_repository.games(team1_group1)
# for game in games:
#     print(game.__dict__)

# group_1_game_repository.delete(game_5_group_1.id)


# sorted_games = group_1_game_repository.sort_games_date()
# for game in sorted_games:
#     print(game.team_1.name)
    # pdb.set_trace()




# sorted_games_1 = group_1_game_repository.sort_games_date()
# for game in sorted_games_1:
#     print(game.__dict__)

# sorted_teams_1 = team_repository.sort_teams_rank()
# for team in sorted_teams_1:
#     print(team.__dict__)

# sorted_teams_2 = group_2_team_repository.sort_teams_rank()
# for team in sorted_teams_2:
#     print(team.__dict__)
