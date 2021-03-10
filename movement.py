from move_row_left import move_row_left
from move_row_right import move_row_right
from move_row_up_down import move_row_up
from move_row_up_down import move_row_down
from read_player_command import read_player_command

def movement(game_grid,move):
    movement=move
    if movement=="g":
        move_row_left(game_grid)
    elif movement=="d":
        move_row_right(game_grid)
    elif movement=="h":
        move_row_up(game_grid)
    elif movement=="b":
        move_row_down(game_grid)
    return game_grid
