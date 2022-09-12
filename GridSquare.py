class GridSquare:
    def __init__(self):
        self.movement = [True, True, True, True]
        self.contains_player = False
    def set_movement(self, movement):
        self.movement = movement
