N = int(input("Saisir N : "))
while not 10 <= N <= 100:
    N = int(input("Saisir N entre 10 et 100 : "))
i = N - 1
ligne = ""
while i >= 0:
    ligne = ligne + str(i) + " "
    i = i - 1
print(ligne)
