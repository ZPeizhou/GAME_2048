from tkinter import *

from create_grid import create_grid
from grid_2048 import init_game
from interface import interface
from grid_add_new_tile import grid_add_new_tile
from movement import movement
from whether_gameover import whether_the_game_is_over

window = Tk()
window.title('Game 2048')
window.geometry('400x490')
window.resizable(width=FALSE,height=FALSE)
canvas = Canvas(window,height=490,width=400)
canvas.pack()

score=0

def window_display(window):
    for line in range (0,500,100):
        canvas.create_line([(line,0),(line,400)],fill='black')
        canvas.create_line([(0,line),(400,line)],fill='black')
    for i in range (4):
        for j in range (4):
           canvas.create_text(100*j+50,100*i+50,text='%s'%(game_grid[i][j]))
    canvas.create_text(200,445,text='\n\n                      score: %s\n\n          Entrez votre commande:\n(g (gauche), d (droite), h (haut), b (bas))\n'%(score))

def failure1(window):
    canvas.create_rectangle(0,0,400,400,fill='grey')
    canvas.create_text(200,200,text='UNABLE TO MOVE THIS WAY\n\n     TRY ANOTHER MOVE')
    while 0:
        {}
    window_display(window)

def failure2(window):
    canvas.create_rectangle(0,0,400,400,fill='grey')
    canvas.create_text(200,200,text='    INVALIDE MOVE\n\nTRY ANOTHER MOVE')
    while 0:
        {}
    window_display(window)

game_continue=0
while game_continue==0:
    game_grid=init_game(4)
    window_display(window)
    game_continue=whether_the_game_is_over(game_grid)
    while game_continue==1:
        game_continue=whether_the_game_is_over(game_grid)
        if game_continue==0:
            break
        move = raw_input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
        while move!="g" and move!="d" and move!="h" and move!="b":
            failure2(window)
            move = raw_input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
        grid = create_grid(4)
        for i in range(0,4):
            for j in range(0,4):
                grid[i][j]=game_grid[i][j]
        movement(game_grid,move)
        game_grid=grid_add_new_tile(game_grid)
        while grid==game_grid:
            failure1(window)
            move = raw_input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
            while move!="g" and move!="d" and move!="h" and move!="b":
                failure2(window)
                move = raw_input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
            movement(game_grid,move)
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
        canvas.delete(ALL)
        window_display(window)
        if max(pool)==2048:
            canvas.create_rectangle(0,0,400,400,fill='pink')
            canvas.create_text(200,200,text='WIN')
            while 0:
                {}
    if game_continue==1:
        break
    else:
        canvas.create_rectangle(0,0,400,400,fill='grey')
        canvas.create_text(200,200,text='                 LOSE\n\nMAKE A MOVE TO RESTART')
        while 0:
            {}