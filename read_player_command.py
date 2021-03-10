def read_player_command():
    move = raw_input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move!="g" and move!="d" and move!="h" and move!="b":
        print("invalide movement!")
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move
