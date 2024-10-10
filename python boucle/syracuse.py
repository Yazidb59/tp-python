"""
Conjecture de Syracuse
"""
No = int(input("Entrez un nombre entier supérieur à 1: "))

nx = No 

temps_vol = 0
alt_max = 0

print(f"Suite de Syracuse pour No = {No}")

print(No, end="")

while nx != 1 :
    if nx % 2 == 0 :    
       #si nx est pair
       nx = nx // 2
    else :
       nx = nx * 3 + 1    
       # si nx est impaire
    print(f"-{nx}", end="")
    temps_vol +=1
    # if nx > alt_max:
    #     alt_max = nx
    alt_max = max(nx, alt_max)

print(f"temps de vol = {temps_vol}")
print(f"Altitude maximale = {alt_max}")