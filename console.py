from models.team import Team

import repositories.group_1_team_repository as group_1_team_repository
import repositories.group_2_team_repository as group_2_team_repository

#Group1
team1_group1 = Team('Australia', 0)
group_1_team_repository.save(team1_group1)
team2_group1 = Team('Bangladesh', 0)
group_1_team_repository.save(team2_group1)
team3_group1 = Team('England', 0)
group_1_team_repository.save(team3_group1)
team4_group1 = Team('South Africa', 0)
group_1_team_repository.save(team4_group1)
team5_group1 = Team('Sri Lanka', 0)
group_1_team_repository.save(team5_group1)
team6_group1 = Team('West Indies', 0)
group_1_team_repository.save(team6_group1)

#Group2
team1_group2 = Team('Afghanistan', 0)
group_2_team_repository.save(team1_group2)
team2_group2 = Team('India', 0)
group_2_team_repository.save(team2_group2)
team3_group2 = Team('Namibia', 0)
group_2_team_repository.save(team3_group2)
team4_group2 = Team('New Zealand', 0)
group_2_team_repository.save(team4_group2)
team5_group2 = Team('Pakistan', 0)
group_2_team_repository.save(team5_group2)
team6_group2 = Team('Scotland', 0)
group_2_team_repository.save(team6_group2)
