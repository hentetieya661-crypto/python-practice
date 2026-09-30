import random
NS = random.randint(1, 100)
essais = 0
trouve = False
print("Devinez le nombre secret entre 1 et 100 !")
while not trouve:
    P = int(input("Proposez un nombre : "))
    essais += 1
        if P < NS:
        print("Trop petit")
    elif P > NS:
        print("Trop grand")
    else:
        print("Correct")
        trouve = True
print("Trouvé en", essais, "essais")

