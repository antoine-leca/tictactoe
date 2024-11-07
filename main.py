from joueurs.py import initialiser_joueurs
from grid.py import create_grid
from placement.py import verif_case
from winner.py import horizontal
from winner.py import verticale
from winner.py import diagonale
from winner.py import match_nul

def main():
    initialiser_joueurs()
    create_grid()
    verif_case()
    horizontal()
    verticale()
    diagonale()
    match_nul()