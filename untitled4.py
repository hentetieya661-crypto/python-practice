
mpc = "ALGO2026"
k = 0
acc=false
while k < 3:
    mp = input("Entrez le mot de passe : ")
    if mp == mpc:
        print("Accès autorisé")
        acc=true
    else:
        k=k+1
        print("Mot de passe incorrect.")
        if k == 3:
            print("Compte bloqué")

