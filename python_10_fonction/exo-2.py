"""
Note sur 20
"""
note = float(input("saisissez votre note : "))
total = float(input("le devoir était noté sur combien de ponint ? :"))

def note_sur_20(note):
    calcul = note / 2
    return note

résultat = note_sur_20(note)

print(f"ta note est de {note}/40 {résultat}/20 ")
