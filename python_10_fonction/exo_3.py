"""
prix du trajet
"""
def prix_du_trajet(conso_v, Prix_l, kms, nb_pers):
    prix = conso_v * Prix_l * kms / nb_pers
    return prix

#programme principale
conso_v = float(input("concomation de la voiture (litre/100km): "))
Prix_l = float(input("prix d'un litre d'essence: "))
kms = float(input("nombre de kilomètrre parcourus : "))
nb_pers = float(input("nombre de personne dans la voiture : "))

resultat = prix_du_trajet(conso_v, Prix_l, kms, nb_pers)

print(f"Le trajet revient à {resultat} par personne")
