"""
Note sur 20
"""


def note_sur_20(note):
    calcul = note / 2
    return calcul


#programme principale
note = float(input("saisissez votre note : "))
total = float(input("le devoir était noté sur combien de point ? :"))

résultat = note_sur_20(note)

print(f"ta note est de {note}/40 {résultat}/20")
