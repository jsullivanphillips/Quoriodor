
def render(map):
    for r in range(map.size):
        #print upper border
        if r == 0:
            print(' ', end='')
            for c in range(map.size):
                print('- ', end='')
            print()
        if r >= 0:
            #vertical bars |
            #movement left and right
            for c in range(map.size):
                cg_movement = map.grid[r][c].movement
                if c == 0:
                    print('|', end='')
                if map.grid[r][c].contains_player == True:
                    print('O', end='')
                else:
                    print('*', end='')
                if cg_movement[1] == True: #movement to the right
                    print(' ', end='')
                elif cg_movement[1] == False:
                    print('|', end='')
            print()
            for c in range(map.size):
                #cross bars
                #vertical movement
                cg_movement = map.grid[r][c].movement
                if cg_movement[2] == False:
                    print(' -', end='')
                else:
                    print('  ', end='')
                if c == (map.size - 1):
                    print()
    print()
