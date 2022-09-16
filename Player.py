class Player:
    def __init__(self, player_num, num_walls):
        self.location = []
        self.player_num = player_num
        self.num_walls = num_walls
    def set_location(self, location):
        self.location = location
