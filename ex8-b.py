# EXERCICE 8
# Fichiers : Écrivez un programme qui lit un fichier texte, compte le nombre de mots et écrit le résultat dans un autre fichier.

fichier_entree = "ex8-b.txt"
fichier_sortie = "ex8-b-resultat.txt"

def compter_mots(texte):
    mots = texte.split()
    return len(mots)

with open(fichier_entree, "r") as file:
    texte = file.read()

nombre_de_mots = compter_mots(texte)

with open(fichier_sortie, "w") as file:
    file.write(f"Le nombre de mots dans le texte est : {nombre_de_mots}")
