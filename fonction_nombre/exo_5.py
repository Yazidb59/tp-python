"""
convertissseur euros
"""

# fonction
def afficher_convertisseur(taux : float,debut : int) -> float:
    """
    donnes de la convertion
    :taux: (float) taux de change
    :debut: (float) première valeur
    :return: (float)
    """

    conversion = debut * taux

    return (conversion)

#programme principal

change = float(input("taux de change exprimé en décimal : "))
debut = int(input("première valeur en euros à convertir : "))
fin = int(input("valeur max à convertir : "))
pas = int(input("écart entre chauqe valeur en euros : "))

while debut <= fin :
    b = afficher_convertisseur(change,debut)
    print(f"{debut} € -> {b:.2f}$")
    debut += pas
