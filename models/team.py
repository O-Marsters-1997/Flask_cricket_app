class Team:
    def __init__(self, name, points, group_id, id=None):
        self.name = name
        self.points = points
        self.group_id = group_id
        self.id =id
        
    def victory(self, team):
        team.points +=2
