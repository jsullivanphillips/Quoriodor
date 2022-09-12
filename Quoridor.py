
class GridSquare:
    def __init__(self):
        self.movement = [True, True, True, True]
        self.contains_player = False
    def set_movement(self, movement):
        self.movement = movement

class Map:
    def __init__(self, size):
        self.size = size
        self.grid = [[GridSquare() for _ in range(size)] for _ in range(size)]
        for r in range(size):
            for c in range(size):
                cur_grid_square = self.grid[r][c]
                if r == 0:
                    movement = cur_grid_square.movement
                    movement[0] = False
                    cur_grid_square.set_movement(movement)
                if c == 0:
                    movement = cur_grid_square.movement
                    movement[3] = False
                    cur_grid_square.set_movement(movement)
                if r == self.size - 1:
                    movement = cur_grid_square.movement
                    movement[2] = False
                    cur_grid_square.set_movement(movement)
                if c == self.size - 1:
                    movement = cur_grid_square.movement
                    movement[1] = False
                    cur_grid_square.set_movement(movement)



    def update_movement(self, r, c, movement):
        self.grid[r][c].movement = movement
        #update up
        if movement[0] == False:
            if r > 0:
                #grab gs above's movement array
                temp_movement = self.grid[r-1][c].movement
                #change its down movement to false
                temp_movement[2] = False
                #push update to above gs
                self.grid[r-1][c].set_movement(temp_movement)
        #update right
        if movement[1] == False:
            if c < self.size-1:
                #grab gs right movement array
                temp_movement = self.grid[r][c+1].movement
                #change its left movement to false
                temp_movement[3] = False
                #push update to right gs
                self.grid[r][c+1].set_movement(temp_movement)
        #update down
        if movement[2] == False:
            if r < self.size-1:
                #grab gs below's movement array
                temp_movement = self.grid[r+1][c].movement
                #change its up movement to false
                temp_movement[0] = False
                #push update to below gs
                self.grid[r+1][c].set_movement(temp_movement)
        #update left
        if movement[3] == False:
            if c > 0:
                #grab gs left movement array
                temp_movement = self.grid[r][c-1].movement
                #change its right movement to false
                temp_movement[1] = False
                #push update to left gs
                self.grid[r][c-1].set_movement(temp_movement)




#implement player
class Player:
    def __init__(self, location):
        self.location = location
