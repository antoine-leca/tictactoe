from main import symbol

def initialiser_joueurs() :

    player1 =  input("Entrez le nom de player1 : ")
    player2 = input("Entrez le nom de player2 : ")
    print(f"player1 est {player1}.")
    print(f"player2 est {player2}.")
    return player1, player2
player1, player2 =  initialiser_joueurs()


def initialiser_joueurs() :
    while True:
        player1 = input("Player1, choisissez votre symbole (X ou O) : ").upper()
        if player1 == "X" or player1 == "O":
            break
        else:
            print("Valeur incorrecte. Veuillez entrez X ou O.")
    player2 = "O" if player1 == "X" else "X"
    print(f"player1 est {player1}.")
    print(f"player2 est {player2}.")
    return player1, player2
player1, player2 = initialiser_joueurs()