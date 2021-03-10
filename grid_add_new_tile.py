import random

def grid_add_new_tile(game_grid):
    t=0
    for i in range(4):
        for j in range(4):
            if game_grid[i][j]==' ':
                t=t+1
    if t==0:
        return game_grid
    else:
        m=random.randint(0,3)
        n=random.randint(0,3)
        while game_grid[m][n]!=' ':
            m=random.randint(0,3)
            if game_grid[m][n]!=' ':
                n=random.randint(0,3)
        game_grid[m][n]=random.choice(['2','4'])
        return game_grid
