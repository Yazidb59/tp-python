"""
Valeur absolue d'un nombre
"""

nb = float(input("Entrez un nombre reel:"))
if nb >= 0:
    rep = nb
else:
    rep = -nb
print(f"La valeur absolue de {nb} est {rep}")
    