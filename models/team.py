class Team:
    def __init__(self, name, id=None):
        self.name = name
        self.id =id

    def victory(self, team):
        team.points +=2
