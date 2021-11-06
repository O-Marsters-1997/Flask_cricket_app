class Team:
    def __init__(self, name, rank, points, id=None):
        self.name = name
        self.rank = rank
        self.points=points
        self.id =id

    def victory(self, team):
        team.points +=2
