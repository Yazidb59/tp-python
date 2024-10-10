"""
prix du trajet
"""

conso_v = float(input("concomation de la voiture (litre/100km): "))
prix_l = float(input("prix d-un litre d'essence: "))
kms = float(input("nombre de kilomètrre parcourus : "))
nb_pers = float(input("nombre de personne dans la voiture : "))

prix = conso_v * prix_l * kms / nb_pers

print(f"Le trajet revient à {prix} par personne")
