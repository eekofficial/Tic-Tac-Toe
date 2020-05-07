# write your code here
def exist_empty(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '_':
                return True
    return False

def check_win(grid, elem):
    in_row = True
    in_column = True
    in_diag_left = True
    in_diag_right = True
    for i in range(3):
        for j in range(3):
            if grid[i][j] != elem:
                in_row = False
            if grid[j][i] != elem:
                in_column = False
        if grid[i][i] != elem:
            in_diag_left = False
        if grid[i][2 - i] != elem:
            in_diag_right = False
        if in_row or in_column:
            return True
        in_row = True
        in_column = True
    if in_diag_left or in_diag_right:
        return True
    return False

def print_grid(grid):
    print('---------')
    print('| {} {} {} |'.format(grid[0][0], grid[0][1], grid[0][2]))
    print('| {} {} {} |'.format(grid[1][0], grid[1][1], grid[1][2]))
    print('| {} {} {} |'.format(grid[2][0], grid[2][1], grid[2][2]))
    print('---------')

def good_coordinate(grid, x, y):
    if not str(x).isdigit() or not str(y).isdigit():
        print('You should enter numbers!')
        return False
    if not 1 <= x <= 3 or not 1 <= y <= 3:
        print('Coordinates should be from 1 to 3!')
        return False
    x, y = perform_coordinates(x, y)
    if grid[x][y] != '_':
        print('This cell is occupied! Choose another one!')
        return False
    return True

def perform_coordinates(x, y):
    return 3 - y, x - 1
    
    

grid = [['_' for _ in range(3)] for _ in range(3)]
print_grid(grid)
x_move = True
count_x = 0
count_o = 0
while not check_win(grid, 'X') and not check_win(grid, 'Y'): 
    x, y = map(int, input('Enter the coordinates: ').split())
    while not good_coordinate(grid, x, y):
        x, y = map(int, input('Enter the coordinates: ').split())
    x, y = perform_coordinates(x, y)
    if x_move:
        grid[x][y] = 'X'
        count_x += 1
        x_move = False
    else:
        grid[x][y] == 'O'
        count_o += 1
        x_move = True  
    print_grid(grid)
x_win = check_win(grid, 'X')
o_win = check_win(grid, 'O')
if abs(count_x - count_o) > 1:
    print('Impossible')
elif exist_empty(grid) and not x_win and not o_win:
    print('Game not finished')
elif not x_win and not o_win:
    print('Draw')
elif x_win and o_win:
    print('Impossible')
elif x_win:
    print('X wins')
elif o_win:
    print('O wins')
else:
    print('Impossible')

    
    
