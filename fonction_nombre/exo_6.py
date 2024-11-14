"""
test de primalité
"""

#fonction
def est_premier(nb: int,)-> int:
    """
    :nb: (int) nombre a tester
    """
    for i in range(2,nb-1,1):
        if nb % i == 0:
            return False
    return True

#programme principale
nombre = int(input("Entrez le nombre à tester : "))
if est_premier(nombre):
    print(f"{nombre} est un nombre premier")
else:
    print(f"{nombre} n'est pas un nombre premier")
