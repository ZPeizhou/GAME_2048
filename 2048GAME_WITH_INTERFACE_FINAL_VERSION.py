from tkinter import *

from create_grid import create_grid
from grid_2048 import init_game
from grid_add_new_tile import grid_add_new_tile
from move_row_left import move_row_left
from move_row_right import move_row_right
from move_row_up_down import move_row_up
from move_row_up_down import move_row_down
from movement import movement
from whether_gameover import whether_the_game_is_over

window = Tk()
window.title('Game 2048')
window.geometry('400x490')
window.resizable(width=FALSE,height=FALSE)
canvas = Canvas(window,height=490,width=400)
canvas.pack()

game_grid=init_game(4)
score=0

def get_score(game_grid):
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
    return score

def window_display(window):
    for line in range (0,500,100):
        canvas.create_line([(line,0),(line,400)],fill='black')
        canvas.create_line([(0,line),(400,line)],fill='black')
    
    for i in range (4):
        for j in range (4):
           canvas.create_text(100*j+50,100*i+50,text='%s'%(game_grid[i][j]),font='32')
    canvas.create_text(200,445,text='\n\n                      score: %s\n\n          Entrez votre commande:\n(g (gauche), d (droite), h (haut), b (bas))\n'%(score))

def window_color(window):
    for i in range (4):
        for j in range (4):
            if game_grid[i][j]=='2':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#87CEFA')
            if game_grid[i][j]=='4':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#7AC5CD')
            if game_grid[i][j]=='8':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#76EEC6')
            if game_grid[i][j]=='16':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#66CDAA')
            if game_grid[i][j]=='32':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#71C671')
            if game_grid[i][j]=='64':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#9AFF9A')
            if game_grid[i][j]=='128':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#98F5FF')
            if game_grid[i][j]=='256':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#BCD2EE')
            if game_grid[i][j]=='512':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#CDC1C5')
            if game_grid[i][j]=='1024':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#CDAF95')
            if game_grid[i][j]=='2048':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#FF3030')
            if game_grid[i][j]=='4096':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#FF3030')
            if game_grid[i][j]=='8192':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#FF3030')
            if game_grid[i][j]=='16384':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#FF3030')
            if game_grid[i][j]=='32768':
                canvas.create_rectangle(100*j,100*i,100*j+100,100*i+100,fill='#FF3030')
    
def key_press(event):
    global score
    global flag
    dir=(event.keysym).lower()
    if dir in ['h','b','g','d']:
        grid = create_grid(4)
        for i in range(0,4):
            for j in range(0,4):
                grid[i][j]=game_grid[i][j]
        movement(game_grid,dir)
        grid_add_new_tile(game_grid)
        score = get_score(game_grid)
        canvas.delete(ALL)
        window_color(window)
        window_display(window)
        if grid==game_grid:
            canvas.create_rectangle(0,0,400,400,fill='grey')
            canvas.create_text(200,200,text='UNABLE TO MOVE THIS WAY\n\n     TRY ANOTHER MOVE')
            while 0:
                {}
            
            window_display(window)
        
        if whether_the_game_is_over(game_grid)==0:
            canvas.delete(ALL)
            canvas.create_rectangle(0,0,400,400,fill='grey')
            canvas.create_text(200,200,text='                 LOSE\n\nMAKE A MOVE TO RESTART')
            while 0:
                {}
            grid = init_game(4)
            for i in range(0,4):
                for j in range(0,4):
                    game_grid[i][j]=grid[i][j]
            window_display(window)
        
        pool=[]
        for i in range (0,4):
            for j in range (0,4):
                if game_grid[i][j]==' ':                    
                    pool.append(0)
                else:
                    pool.append(int(game_grid[i][j]))
        if max(pool)==2048 and flag==0:
            flag=flag+1
            canvas.create_rectangle(0,0,400,400,fill='pink')
            canvas.create_text(200,200,text='       WIN\n\nCARRYING ON')
            while 0:
                {}
            window_display(window)

    else:
        canvas.create_rectangle(0,0,400,400,fill='grey')
        canvas.create_text(200,200,text='    INVALIDE MOVE\n\nTRY ANOTHER MOVE')
        while 0:
            {}
        
        window_display(window)

score=get_score(game_grid)
flag=0
window_color(window)
window_display(window)


window.bind('<Key>',key_press)
window.mainloop()
