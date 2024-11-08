table= [
        ["","",""],
        ["","",""],
        ["","",""]
        ]


"""

Cet fonction permet de rentrer dans la table le signe selectionner 
par le joueur et de verifier si son emplacement est vide.

elle reçoit en parametr


je fais rentrer au joueur les coordonnées de l'emplacement et je le stock 
dans une variables element


"""
def verif_case(table, symbol):
        row     = int(input("rentrez la ligne : "))
        column  = int(input("rentrez la colonne : "))
        element = table[row][column]

        if symbol == "X" or symbol == "x" or symbol == "O" or symbol == "o":
                if element == "":
                        table[row][column] = symbol
                        # table.insert(element, symbol)
                        print(table)
                        print("au joueur suivant de jouer")
                        return table
                else:
                        print("veuillez choisir une autre case")
                        return verif_case(table, symbol)
        else:
                print("veuillez choisir entre l")

                        

for x in table:
        for ele in x:
                symbol = input("veuillez rentrez le signe")
                verif_case(table, symbol)


#vérifier le merge
