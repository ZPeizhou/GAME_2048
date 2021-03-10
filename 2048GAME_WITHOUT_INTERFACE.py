from create_grid import create_grid
from grid_2048 import init_game
from interface import interface
from grid_add_new_tile import grid_add_new_tile
from read_player_command import read_player_command
from movement import movement
from whether_gameover import whether_the_game_is_over

import time

game_continue=0
while game_continue==0:
    game_grid=init_game(4)
    interface(game_grid)
    game_continue=whether_the_game_is_over(game_grid)
    while game_continue==1:
        game_continue=whether_the_game_is_over(game_grid)
        if game_continue==0:
            break
        move= read_player_command()
        grid = create_grid(4)
        for i in range(0,4):
            for j in range(0,4):
                grid[i][j]=game_grid[i][j]
        movement(game_grid,move)
        game_grid=grid_add_new_tile(game_grid)
        while grid==game_grid:
            print("UNABLE TO MOVE THIS WAY")
            move= read_player_command()
            movement(game_grid,move)
        interface(game_grid)
        pool=[]
        for i in range (0,4):
            for j in range (0,4):
                if game_grid[i][j]==' ':
                    pool.append(0)
                else:
                    pool.append(int(game_grid[i][j]))
        score=0
        for score_count in range (16):
            score=score+pool[score_count]
        print("score:%s"%(score))
        if max(pool)==2048:
            print("WIN")
            break
    if game_continue==1:
        break
    else:
        print("LOSE")
        print("RESTART AFTER FIVE SECONDS")
        time.sleep(5)
