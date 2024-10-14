"""
Volume d'une boîte
"""

def vol_boîte(l, L, H):
    calcul = l * L * H
    return calcul


l = float(input("Largeur (cm): "))
L = float(input("Longueur (cm): "))
H = float(input("Hauteur (cm): "))

resultat = vol_boîte(l, L, H)

print(f"Le volume de la boîte est de {resultat:.2f}cm3")
