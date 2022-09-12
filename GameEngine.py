from Quoridor import*

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
