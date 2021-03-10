from grid_add_new_tile import grid_add_new_tile
from create_grid import create_grid

def init_game(n=4):
    game_grid=create_grid(n)
    game_grid=grid_add_new_tile(game_grid)
    game_grid=grid_add_new_tile(game_grid)
    return game_grid
