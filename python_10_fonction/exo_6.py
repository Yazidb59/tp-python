"""
Teste de primalité
"""
nb_entier = int(input("Entrez un nombre à tester : "))

def est_premier(N):
    if nb_entier % 2:
        calcul = nb_entier % N-1
        print(f"{nb_entier} est un nombre premier")
    else :
        calcul != nb_entier % N-1
        print(f"{nb_entier} n'est pas un nombre premier")
