#plateau de jeu
"""
player = [
    ['X', 'O', 'X'],
    ['X', 'X', 'X'],
    ['O', 'X', 'O']
]
"""
#verification des cases horizontales
def horizontal(board):
    if player[0][0] == "X" and player[0][1] == "X" and player[0][2] == "X" or \
player[0][0] == "O" and player[0][1] == "O" and player[0][2] == "O":
        return print("victoire0")
    elif player[1][0] == "X" and player[1][1] == "X" and player[1][2] == "X" or \
player[1][0] == "O" and player[1][1] == "O" and player[1][2] == "O":
        return print("victoire1")

    elif player[2][0] == "X" and player[2][1] == "X" and player[2][2] == "X" or \
player[2][0] == "O" and player[2][1] == "O" and player[2][2] == "O":
        return print("victoire2")

horizontal(player)


#verification des cases verticales
def verticale(board):
    if player[0][0] == "X" and player[1][0] == "X" and player[2][0] == "X" or \
player[0][0] == "O" and player[1][0] == "O" and player[2][0] == "O":
        return print("victoire3")

    elif player[0][1] == "X" and player[1][1] == "X" and player[2][1] == "X" or \
player[0][1] == "O" and player[1][1] == "O" and player[2][1] == "O":
        return print("victoire4")

    elif player[0][2] == "X" and player[1][2] == "X" and player[2][2] == "X" or \
player[0][2] == "O" and player[1][2] == "O" and player[2][2] == "O":
        return print("victoire5")

verticale(player)


#verification des cases diagonales
def diagonale(board):
    if player[0][0] == "X" and player[1][1] == "X" and player[2][2] == "X" or \
player[0][0] == "O" and player[1][1] == "O" and player[2][2] == "O":
        return print("victoire6")

    elif player[0][2] == "X" and player[1][1] == "X" and player[2][0] == "X" or \
player[0][2] == "O" and player[1][1] == "O" and player[2][0] == "O":
        return print("victoire7")

diagonale(player)