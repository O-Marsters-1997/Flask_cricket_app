import pdb
from models.team import Team
from models.game import Game

import repositories.group_1_team_repository as group_1_team_repository
import repositories.group_2_team_repository as group_2_team_repository

import repositories.group_1_game_repository as group_1_game_repository
import repositories.group_2_game_repository as group_2_game_repository


group_1_game_repository.delete_all()
group_2_game_repository.delete_all()

group_1_team_repository.delete_all()
group_2_team_repository.delete_all()

#User has no control of which teams are in the league, they are pre-defined here instead!

# #Group1
team1_group1 = Team('Australia',12)
group_1_team_repository.save(team1_group1)
team2_group1 = Team('Bangladesh', 3)
group_1_team_repository.save(team2_group1)
team3_group1 = Team('England', 4)
group_1_team_repository.save(team3_group1)
team4_group1 = Team('South Africa', 4)
group_1_team_repository.save(team4_group1)
team5_group1 = Team('Sri Lanka', 8)
group_1_team_repository.save(team5_group1)
team6_group1 = Team('West Indies', 0)
group_1_team_repository.save(team6_group1)

#Group2
team1_group2 = Team('Afghanistan', 4)
group_2_team_repository.save(team1_group2)
team2_group2 = Team('India', 5)
group_2_team_repository.save(team2_group2)
team3_group2 = Team('Namibia',11)
group_2_team_repository.save(team3_group2)
team4_group2 = Team('New Zealand', 3)
group_2_team_repository.save(team4_group2)
team5_group2 = Team('Pakistan', 1)
group_2_team_repository.save(team5_group2)
team6_group2 = Team('Scotland', 14)
group_2_team_repository.save(team6_group2)


# print(group_1_team_repository.select_all())
# print(group_2_team_repository.select_all())
# print(group_1_team_repository.select(team5_group1.id).name)

# game_1_group_1 = Game(team1_group1, team2_group1, 196, 110, '1970-01-01 00:00:00.00')
# group_1_game_repository.save(game_1_group_1)
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


# games = group_1_team_repository.games(team1_group1)
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

# sorted_teams_1 = group_1_team_repository.sort_teams_rank()
# for team in sorted_teams_1:
#     print(team.__dict__)

# sorted_teams_2 = group_2_team_repository.sort_teams_rank()
# for team in sorted_teams_2:
#     print(team.__dict__)
