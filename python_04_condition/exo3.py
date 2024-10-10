"""
Division par 2 et/ou 3
"""

nb = int(input("Entrez un nombre entier non signé :" ))
if nb % 2 == 0 and nb % 3 == 0:
    print(f"Le nombre {nb} est divisible par 3 et par 2")
elif nb % 2 == 0 and nb % 3 != 0:
   print(f"Le nombre {nb} est divisible par 2 mais pas par 3")
elif nb % 2 != 0 and nb % 3 == 0:
   print(f"Le nombre {nb} est divisible par 3 mais pas par 2")
else:
   print(f"Le nombre {nb} n'est ni divisible par 2 et ni par 3")
    