
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

#implement game engine loop
class Game:
    def __init__(self):
        self.map = Map(8)
        self.p1 = Player([3,5])
        self.p2 = Player([2,2])
        self.map.grid[self.p1.location[0]][self.p1.location[1]].contains_player = True
        self.map.grid[self.p2.location[0]][self.p2.location[1]].contains_player = True

    def move_player(self, player, direction):
        r,c = player.location
        if direction == 'w':
            #move player up
            location = player.location
            location[0] = location[0] - 1
            player.location = location
            #update grid square information
            self.map.grid[r][c].contains_player = False
            self.map.grid[r - 1][c].contains_player = True
        if direction == 'd':
            #move player right
            location = player.location
            location[1] = location[1] + 1
            player.location = location
            #update grid square information
            self.map.grid[r][c].contains_player = False
            self.map.grid[r][c + 1].contains_player = True
        if direction == 's':
            #move player down
            location = player.location
            location[0] = location[0] + 1
            player.location = location
            #update grid square information
            self.map.grid[r][c].contains_player = False
            self.map.grid[r + 1][c].contains_player = True
        if direction == 'a':
            #move player left
            location = player.location
            location[1] = location[1] - 1
            player.location = location
            #update grid square information
            self.map.grid[r][c].contains_player = False
            self.map.grid[r][c - 1].contains_player = True

    def render(self):
        for r in range(self.map.size):
            #print upper border
            if r == 0:
                print(' ', end='')
                for c in range(self.map.size):
                    print('- ', end='')
                print()
            if r >= 0:
                #vertical bars |
                #movement left and right
                for c in range(self.map.size):
                    cg_movement = self.map.grid[r][c].movement
                    if c == 0:
                        print('|', end='')
                    if self.map.grid[r][c].contains_player == True:
                        print('O', end='')
                    else:
                        print('*', end='')
                    if cg_movement[1] == True: #movement to the right
                        print(' ', end='')
                    elif cg_movement[1] == False:
                        print('|', end='')
                print()
                for c in range(self.map.size):
                    #cross bars
                    #vertical movement
                    cg_movement = self.map.grid[r][c].movement
                    if cg_movement[2] == False:
                        print(' -', end='')
                    else:
                        print('  ', end='')
                    if c == (self.map.size - 1):
                        print()
        print()

    def start_game(self):
        self.render()
        turn = 0
        while(1):
            if(turn == 0):
                curr_player = self.p1
                print('player 1 turn')
            else:
                curr_player = self.p2
                print('player 2 turn')

            action_taken_valid = False
            while not action_taken_valid:
                a = input()
                if len(a) == 1:
                    if a not in 'wasd':
                        continue
                    r,c = curr_player.location
                    possible_moves = self.map.grid[r][c].movement
                    if a == 'w' and possible_moves[0]:
                        self.move_player(curr_player, 'w')
                        action_taken_valid = True
                    if a == 'd' and possible_moves[1]:
                        self.move_player(curr_player, 'd')
                        action_taken_valid = True
                    if a == 's' and possible_moves[2]:
                        self.move_player(curr_player, 's')
                        action_taken_valid = True
                    if a == 'a' and possible_moves[3]:
                        self.move_player(curr_player, 'a')
                        action_taken_valid = True


            self.render()

new_game = Game()
new_game.start_game()
