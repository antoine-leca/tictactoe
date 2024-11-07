L = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

create_grid()
"""
def isFull():
        if L == " ":
            print("Le tableau est vide, vous pouvez jouer.")
        else:
            print("i")

isFull()
"""
var = 0
car = 0
while car < len(L):
    while var < len(L[var][car]):
        if L == " ":
            print("Le tableau est vide, vous pouvez jouer.")
        else:
            print("i")
        var +=1
    car += 1