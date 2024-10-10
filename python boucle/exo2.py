"""
Division entières par 2
"""

x = int(input("Entrez un nombre entier positif au clavier :"))

cpt = 0

while x > 1:
    x = x // 2
    print(f"nb = {x}")
    cpt +=  1

print(f"nombre de boucle effectuer{cpt}")
