
def render(map):
    for r in range(map.size):
        #print upper border
        if r == 0:
            print('  ', end='')
            for c in range(map.size):
                print('%d '%c, end='')
            print()
            print('  ', end='')
            for c in range(map.size):
                print('- ', end='')
            print()
        if r >= 0 and r <= map.size - 1:
            # vertical bars | movement left and right
            for c in range(map.size):
                cg_movement = map.grid[r][c].movement
                if c == 0:
                    print('%d|'%r, end='')
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
                # vertical movement, cross bars
                # formatting spacer for last line
                if r == map.size - 1 and c == 0:
                    print(' ', end='')
                cg_movement = map.grid[r][c].movement
                if cg_movement[2] == False:
                    print(' -', end='')
                else:
                    print('  ', end='')
                if c == (map.size - 1):
                    print()


    print()
