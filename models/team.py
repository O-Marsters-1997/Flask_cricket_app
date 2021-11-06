class Team:
    def __init__(self, name, points, id=None):
        self.name = name
        self.id =id
        self.points = points

    def victory(self, team):
        team.points +=2
