from Player import Player
from Map import Map
from RenderEngine import render
import sys
import re


class Game:
    def __init__(self, map_size):
        self.map = Map(map_size)
        self.p = re.compile("[0-" + str(map_size - 1) + "][,]{1}[0-" + str(map_size - 1) + "][ ]{1}[0-" + str(map_size - 1) + "][,]{1}[0-" + str(map_size - 1) + "]")
        self.p1 = Player(1)
        self.p2 = Player(2)


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
            self.map.grid[r - 1][c].contains_player_value = player.player_num
        if direction == 'd':
            #move player right
            location = player.location
            location[1] = location[1] + 1
            player.location = location
            #update grid square information
            self.map.grid[r][c].contains_player = False
            self.map.grid[r][c + 1].contains_player = True
            self.map.grid[r][c + 1].contains_player_value = player.player_num
        if direction == 's':
            #move player down
            location = player.location
            location[0] = location[0] + 1
            player.location = location
            #update grid square information
            self.map.grid[r][c].contains_player = False
            self.map.grid[r + 1][c].contains_player = True
            self.map.grid[r + 1][c].contains_player_value = player.player_num
        if direction == 'a':
            #move player left
            location = player.location
            location[1] = location[1] - 1
            player.location = location
            #update grid square information
            self.map.grid[r][c].contains_player = False
            self.map.grid[r][c - 1].contains_player = True
            self.map.grid[r][c - 1].contains_player_value = player.player_num



    def setup_game(self):
        print("Player 1, which collumn would you like to start in? 0 - %d" % (self.map.size - 1))
        valid_input = False
        while not valid_input:
            a = input()
            if a.isnumeric():
                if int(a) not in range(self.map.size):
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
                if int(a) not in range(self.map.size):
                    print("Please enter a number from 0 - %d" % (self.map.size - 1))
                    continue
                self.p2.set_location([self.map.size - 1, int(a)])
                valid_input = True
            else:
                print("Please enter a number from 0 - %d" % (self.map.size - 1))


        self.map.grid[self.p1.location[0]][self.p1.location[1]].contains_player = True
        self.map.grid[self.p1.location[0]][self.p1.location[1]].contains_player_value = self.p1.player_num
        self.map.grid[self.p2.location[0]][self.p2.location[1]].contains_player = True
        self.map.grid[self.p2.location[0]][self.p2.location[1]].contains_player_value = self.p2.player_num
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
                # Character movement
                if len(a) == 1:
                    if a not in 'wasd':
                        continue
                    r,c = curr_player.location
                    possible_moves = self.map.grid[r][c].movement

                    if a == 'w' and possible_moves[0] and not self.map.grid[r-1][c].contains_player:
                        self.move_player(curr_player, 'w')
                        action_taken_valid = True
                    if a == 'd' and possible_moves[1] and not self.map.grid[r][c+1].contains_player:
                        self.move_player(curr_player, 'd')
                        action_taken_valid = True
                    if a == 's' and possible_moves[2] and not self.map.grid[r+1][c].contains_player:
                        self.move_player(curr_player, 's')
                        action_taken_valid = True
                    if a == 'a' and possible_moves[3] and not self.map.grid[r][c-1].contains_player:
                        self.move_player(curr_player, 'a')
                        action_taken_valid = True
                    if(curr_player == self.p1 and curr_player.location[0] == self.map.size-1):
                        render(self.map)
                        print("PLAYER 1 HAS WON THE GAME")
                        sys.exit()
                    if(curr_player == self.p2 and curr_player.location[0] == 0):
                        render(self.map)
                        print("PLAYER 2 HAS WON THE GAME")
                        sys.exit()
                # Wall placement
                # verifies input is in format num,num num,num and within range of map
                if self.p.match(a) is not None:
                    gs_list = re.findall(r'\d{1}[,]\d{1}', a)
                    gs_1 = re.findall(r'\d{1}',gs_list[0])
                    gs_2 = re.findall(r'\d{1}',gs_list[1])
                    for i in range(len(gs_1)):
                        gs_1[i] = int(gs_1[i])
                        gs_2[i] = int(gs_2[i])
                    # Check if two blocks are different and next to each other
                    #ra and ca reflect clockwise movement starting at up
                    ra = [-1, 0, 1, 0]
                    ca = [0, 1, 0, -1]
                    for i in range(4):
                        if ((gs_1[0] + ra[i]) == gs_2[0]) and ((gs_1[1] + ca[i]) == gs_2[1]):
                            self.map.add_wall(gs_1, gs_2, i)
                            action_taken_valid = True
                    if not action_taken_valid:
                        print('Please enter two adjacent blocks with no existing wall between them. \nExample formatting: 0,0 0,1')
                if a =='exit':
                    sys.exit()


            render(self.map)

new_game = Game(5)
new_game.setup_game()
new_game.start_game()
