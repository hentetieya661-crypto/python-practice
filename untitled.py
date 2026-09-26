NP = int(input("Saisir NP : "))
NB = int(input("Saisir NB : "))
N = int(input("Saisir N : "))
while N <= 0:
    N = int(input("N doit être > 0, saisir N : "))
valeur = NP * 2 + NB * 145
part = valeur / N
print("part =", part)
