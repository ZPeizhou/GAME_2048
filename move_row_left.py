def move_row_left(game_grid):
    for i in range(0,4):
        if game_grid[i][0]!=' 'and game_grid[i][1]==' 'and game_grid[i][2]==' 'and game_grid[i][3]==' ':
            continue
        if game_grid[i][0]==' 'and game_grid[i][1]!=' 'and game_grid[i][2]==' 'and game_grid[i][3]==' ':
            game_grid[i][0],game_grid[i][1]=game_grid[i][1],game_grid[i][0]
            continue
        if game_grid[i][0]==' 'and game_grid[i][1]==' 'and game_grid[i][2]!=' 'and game_grid[i][3]==' ':
            game_grid[i][0],game_grid[i][2]=game_grid[i][2],game_grid[i][0]
            continue
        if game_grid[i][0]==' 'and game_grid[i][1]==' 'and game_grid[i][2]==' 'and game_grid[i][3]!=' ':
            game_grid[i][0],game_grid[i][3]=game_grid[i][3],game_grid[i][0]
            continue
        if game_grid[i][0]!=' 'and game_grid[i][1]!=' 'and game_grid[i][2]==' 'and game_grid[i][3]==' ':
            if game_grid[i][0]==game_grid[i][1]:
                game_grid[i][0]=str(int(game_grid[i][0])+int(game_grid[i][1]))
                game_grid[i][1]=' '
                continue
            else:
                continue
        if game_grid[i][0]!=' 'and game_grid[i][1]==' 'and game_grid[i][2]!=' 'and game_grid[i][3]==' ':
            if game_grid[i][0]==game_grid[i][2]:
                game_grid[i][0]=str(int(game_grid[i][0])+int(game_grid[i][2]))
                game_grid[i][2]=' '
                continue
            else:
                game_grid[i][1],game_grid[i][2]=game_grid[i][2],game_grid[i][1]
                continue
        if game_grid[i][0]!=' 'and game_grid[i][1]==' 'and game_grid[i][2]==' 'and game_grid[i][3]!=' ':
            if game_grid[i][0]==game_grid[i][3]:
                game_grid[i][0]=str(int(game_grid[i][0])+int(game_grid[i][3]))
                game_grid[i][3]=' '
                continue
            else:
                game_grid[i][1],game_grid[i][3]=game_grid[i][3],game_grid[i][1]
                continue
        if game_grid[i][0]==' 'and game_grid[i][1]!=' 'and game_grid[i][2]!=' 'and game_grid[i][3]==' ':
            if game_grid[i][1]==game_grid[i][2]:
                game_grid[i][0]=str(int(game_grid[i][1])+int(game_grid[i][2]))
                game_grid[i][1]=' '
                game_grid[i][2]=' '
                continue
            else:
                game_grid[i][0]=game_grid[i][1]
                game_grid[i][1]=game_grid[i][2]
                game_grid[i][2]=' '
                continue
        if game_grid[i][0]==' 'and game_grid[i][1]!=' 'and game_grid[i][2]==' 'and game_grid[i][3]!=' ':
            if game_grid[i][1]==game_grid[i][3]:
                game_grid[i][0]=str(int(game_grid[i][1])+int(game_grid[i][3]))
                game_grid[i][1]=' '
                game_grid[i][3]=' '
                continue
            else:
                game_grid[i][0]=game_grid[i][1]
                game_grid[i][1]=game_grid[i][3]
                game_grid[i][3]=' '
                continue
        if game_grid[i][0]==' 'and game_grid[i][1]==' 'and game_grid[i][2]!=' 'and game_grid[i][3]!=' ':
            if game_grid[i][2]==game_grid[i][3]:
                game_grid[i][0]=str(int(game_grid[i][2])+int(game_grid[i][3]))
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
            else:
                game_grid[i][0]=game_grid[i][2]
                game_grid[i][1]=game_grid[i][3]
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
        if game_grid[i][0]!=' 'and game_grid[i][1]!=' 'and game_grid[i][2]!=' 'and game_grid[i][3]==' ':
            if game_grid[i][0]==game_grid[i][1]:
                game_grid[i][0]=str(int(game_grid[i][0])+int(game_grid[i][1]))
                game_grid[i][1]=game_grid[i][2]
                game_grid[i][2]=' '
                continue
            elif game_grid[i][1]==game_grid[i][2]:
                game_grid[i][1]=str(int(game_grid[i][1])+int(game_grid[i][2]))
                game_grid[i][2]=' '
                continue
            else:
                continue
        if game_grid[i][0]!=' 'and game_grid[i][1]!=' 'and game_grid[i][2]==' 'and game_grid[i][3]!=' ':
            if game_grid[i][0]==game_grid[i][1]:
                game_grid[i][0]=str(int(game_grid[i][0])+int(game_grid[i][1]))
                game_grid[i][1]=game_grid[i][3]
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
            elif game_grid[i][1]==game_grid[i][3]:
                game_grid[i][1]=str(int(game_grid[i][1])+int(game_grid[i][3]))
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
            else:
                game_grid[i][2]=game_grid[i][3]
                game_grid[i][3]=' '
                continue
        if game_grid[i][0]!=' 'and game_grid[i][1]==' 'and game_grid[i][2]!=' 'and game_grid[i][3]!=' ':
            if game_grid[i][0]==game_grid[i][2]:
                game_grid[i][0]=str(int(game_grid[i][0])+int(game_grid[i][2]))
                game_grid[i][1]=game_grid[i][3]
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
            elif game_grid[i][2]==game_grid[i][3]:
                game_grid[i][1]=str(int(game_grid[i][2])+int(game_grid[i][3]))
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
            else:
                game_grid[i][1]=game_grid[i][2]
                game_grid[i][2]=game_grid[i][3]
                game_grid[i][3]=' '
                continue
        if game_grid[i][0]==' 'and game_grid[i][1]!=' 'and game_grid[i][2]!=' 'and game_grid[i][3]!=' ':
            if game_grid[i][1]==game_grid[i][2]:
                game_grid[i][0]=str(int(game_grid[i][1])+int(game_grid[i][2]))
                game_grid[i][1]=game_grid[i][3]
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
            elif game_grid[i][2]==game_grid[i][3]:
                game_grid[i][0]=game_grid[i][1]
                game_grid[i][1]=str(int(game_grid[i][2])+int(game_grid[i][3]))
                game_grid[i][2]=' '
                game_grid[i][3]=' '
                continue
            else:
                game_grid[i][0]=game_grid[i][1]
                game_grid[i][1]=game_grid[i][2]
                game_grid[i][2]=game_grid[i][3]
                game_grid[i][3]=' '
                continue
        if game_grid[i][0]!=' 'and game_grid[i][1]!=' 'and game_grid[i][2]!=' 'and game_grid[i][3]!=' ':
            if game_grid[i][0]==game_grid[i][1]:
                game_grid[i][0]=str(int(game_grid[i][0])+int(game_grid[i][1]))
                if game_grid[i][2]==game_grid[i][3]:
                    game_grid[i][1]=str(int(game_grid[i][2])+int(game_grid[i][3]))
                    game_grid[i][2]=' '
                    game_grid[i][3]=' '
                    continue
                else:
                    game_grid[i][1]=game_grid[i][2]
                    game_grid[i][2]=game_grid[i][3]
                    game_grid[i][3]=' '
                    continue
            elif game_grid[i][1]==game_grid[i][2]:
                game_grid[i][1]=str(int(game_grid[i][1])+int(game_grid[i][2]))
                game_grid[i][2]=game_grid[i][3]
                game_grid[i][3]=' '
                continue
            elif game_grid[i][2]==game_grid[i][3]:
                game_grid[i][2]=str(int(game_grid[i][2])+int(game_grid[i][3]))
                game_grid[i][3]=' '
                continue
            else:
                continue
    return game_grid
