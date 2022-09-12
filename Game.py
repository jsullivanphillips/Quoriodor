from Player import Player
from Map import Map
import sys
from RenderEngine import render
class Game:
    def __init__(self):
        self.map = Map(8)
        self.p1 = Player()
        self.p2 = Player()


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



    def setup_game(self):
        print("Player 1, which collumn would you like to start in? 0 - %d" % (self.map.size - 1))
        valid_input = False
        while not valid_input:
            a = input()
            if a.isnumeric():
                if int(a) not in range(self.map.size - 1):
                    print("Please enter a number from 0 - %d" % (self.map.size - 1))
                    continue
                self.p1.set_location([0, int(a)])
                valid_input = True
            else:
                print("Please enter a number from 0 - %d" % (self.map.size - 1))

        print("Player 2, which collumn would you like to start in? 0 - %d" % (self.map.size - 1))
        valid_input = False
        while not valid_input:
            a = input()
            if a.isnumeric():
                if int(a) not in range(self.map.size - 1):
                    print("Please enter a number from 0 - %d" % (self.map.size - 1))
                    continue
                self.p2.set_location([self.map.size - 1, int(a)])
                valid_input = True
            else:
                print("Please enter a number from 0 - %d" % (self.map.size - 1))


        self.map.grid[self.p1.location[0]][self.p1.location[1]].contains_player = True
        self.map.grid[self.p2.location[0]][self.p2.location[1]].contains_player = True
    def start_game(self):
        render(self.map)
        turn = 0
        while(1):
            if(turn%2 == 0):
                curr_player = self.p1
                print('player 1 turn')
                turn += 1
            else:
                curr_player = self.p2
                print('player 2 turn')
                turn += 1

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
                if a =='exit':
                    sys.exit()


            render(self.map)

new_game = Game()
new_game.setup_game()
new_game.start_game()
