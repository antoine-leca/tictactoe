table= [
        ["","",""],
        ["","",""],
        ["","",""]
        ]

def verif_case(table, symbol):
        print(symbol,'toto')
        row     = int(input("rentrez la ligne : "))
        column  = int(input("rentrez la colonne : "))
        element = table[row][column]

        if element == "":
                table[row][column] = symbol
                # table.insert(element, symbol)
                return print(table ,"au joueur suivant de jouer")
        else:
                print("veuillez choisir une autre case")
                return verif_case(table, symbol)
                        

for x in table:
        for ele in x:
                symbol  = input("veuillez rentrez le signe :  ")
                verif_case(table, symbol)


