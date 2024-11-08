from joueurs import initialiser_joueurs
from grid import create_grid
from placement import verif_case
from winner import horizontal
from winner import verticale
from winner import diagonale
from winner import match_nul

symbol = input("veuillez rentrez le signe")

def main():
    initialiser_joueurs(symbol)
    create_grid()
    verif_case()
    horizontal()
    verticale()
    diagonale()
    match_nul()