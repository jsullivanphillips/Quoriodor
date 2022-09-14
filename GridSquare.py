class GridSquare:
    def __init__(self):
        self.movement = [True, True, True, True]
        self.contains_player = False
        self.contains_player_value = 0
    def set_movement(self, movement):
        self.movement = movement
