"""
Liste des nombres pairs compris entre deux limites min et max
"""
print("Entrez les limites de recherche :")

x = int(input("Limite min :"))

a = int(input("Limite max :"))

c = [x , a]
for i in range(len(c)):

    if c % 2 == 0 :
     print(f"Liste des nombres pairs compris entre {x} et {a}:" ,end="{b3}")
