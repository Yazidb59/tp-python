"""
surface d'un disque
"""
r = float(input("Le rayon est de "))
from math import pi

def calculer_aire_disque(r):
    """calcul de la surface d'un disque"""
    surface = pi * r**2
    return surface

#programme prinipal
surface = calculer_aire_disque(r)
print(surface)
