from GridSquare import GridSquare

class Map:
    def __init__(self, size):
        self.size = size
        self.grid = [[GridSquare() for _ in range(size)] for _ in range(size)]
        for r in range(size):
            for c in range(size):
                cur_grid_square = self.grid[r][c]
                if r == 0: #upwards movement
                    movement = cur_grid_square.movement
                    movement[0] = False
                    cur_grid_square.set_movement(movement)
                if c == 0: #movement left
                    movement = cur_grid_square.movement
                    movement[3] = False
                    cur_grid_square.set_movement(movement)
                if r == self.size - 1: #movement right
                    movement = cur_grid_square.movement
                    movement[2] = False
                    cur_grid_square.set_movement(movement)
                if c == self.size - 1: #movement down
                    movement = cur_grid_square.movement
                    movement[1] = False
                    cur_grid_square.set_movement(movement)

    # Only valid input should be passed to this method
    def add_wall(self, gs_1, gs_2, direction):
    # movement goes clockwise starting at up, direction reflects that
        if direction == 0:
            self.grid[gs_1[0]][gs_1[1]].movement[direction] = False
            self.grid[gs_2[0]][gs_2[1]].movement[2] = False
        elif direction == 1:
            self.grid[gs_1[0]][gs_1[1]].movement[direction] = False
            self.grid[gs_2[0]][gs_2[1]].movement[3] = False
        elif direction == 2:
            self.grid[gs_1[0]][gs_1[1]].movement[direction] = False
            self.grid[gs_2[0]][gs_2[1]].movement[0] = False
        elif direction == 3:
            self.grid[gs_1[0]][gs_1[1]].movement[direction] = False
            self.grid[gs_2[0]][gs_2[1]].movement[1] = False



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
