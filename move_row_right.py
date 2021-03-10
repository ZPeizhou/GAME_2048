from move_row_left import move_row_left

def invert(game_grid):
	for i in range(0,4):
		game_grid[i][0],game_grid[i][3]=game_grid[i][3],game_grid[i][0]
		game_grid[i][1],game_grid[i][2]=game_grid[i][2],game_grid[i][1]
	return game_grid

def move_row_right(game_grid):
	invert(game_grid)
	move_row_left(game_grid)
	invert(game_grid)
	return game_grid
