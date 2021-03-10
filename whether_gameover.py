from move_row_left import move_row_left
from move_row_right import move_row_right
from move_row_up_down import move_row_up
from move_row_up_down import move_row_down
from create_grid import create_grid

def whether_the_game_is_over(game_grid):
    game_continue=1
    grid = create_grid(4)
    for i in range(0,4):
        for j in range(0,4):
            grid[i][j]=game_grid[i][j]
    if game_grid==move_row_left(grid):
        if game_grid==move_row_right(grid):
            if game_grid==move_row_up(grid):
                if game_grid==move_row_down(grid):
                    game_continue=0
    return game_continue
