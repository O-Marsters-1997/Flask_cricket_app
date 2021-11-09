class Team:
    def __init__(self, name, points, id=None):
        self.name = name
        self.points = points
        self.id =id
        
    def victory(self, team):
        team.points +=2
