from move_row_left import move_row_left
from move_row_right import move_row_right

def transpose(game_grid):
    for i in range(0,3):
        for j in range(i+1,4):
            game_grid[i][j],game_grid[j][i]=game_grid[j][i],game_grid[i][j]
    return game_grid

def move_row_up(game_grid):
    transpose(game_grid)
    move_row_left(game_grid)
    transpose(game_grid)
    return game_grid

def move_row_down(game_grid):
    transpose(game_grid)
    move_row_right(game_grid)
    transpose(game_grid)
    return game_grid
