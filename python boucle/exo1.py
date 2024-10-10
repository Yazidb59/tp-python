"""
Afficher les tables de multiplication
"""
x = int(input("Entrez un nombre entier :"))

for i in range(0,12):

    resultat= x * i

    print(f" {x} * {i} = {resultat}")
