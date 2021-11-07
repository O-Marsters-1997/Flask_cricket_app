class Game:
    def __init__(self, team_1, team_2, team_1_runs, team_2_runs, game_date, id=None):
        self.team_1 = team_1
        self.team_2 = team_2
        self.team_1_runs = team_1_runs
        self.team_2_runs = team_2_runs
        self.game_date = game_date
        self.id = id

    def determine_winner(self, game):
        winner = None 
        if game.team_1_runs > game.team_2_runs:
            winner = game.team_1.name
        elif game.team_2_runs > game.team_1_runs:
            winner = game.team_2.name
        return f"The winner is {winner}"

