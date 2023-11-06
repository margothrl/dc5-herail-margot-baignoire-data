# EXERCICE 8
# Fichiers : Écrivez un programme qui lit un fichier texte, compte le nombre de mots et écrit le résultat dans un autre fichier.

fichier_entree = "ex8-b.txt"
fichier_sortie = "ex8-b-resultat.txt"

def compter_mots(texte):
    compteur_mots = 0
    est_dans_un_mot = False

    for caractere in texte:
        if caractere != ' ' and not est_dans_un_mot:
            est_dans_un_mot = True
            compteur_mots += 1
        elif caractere == ' ':
            est_dans_un_mot = False

    return compteur_mots

with open(fichier_entree, "r") as file:
    texte = file.read()

nombre_de_mots = compter_mots(texte)

with open(fichier_sortie, "w") as file:
    file.write(f"Le nombre de mots dans le texte est : {nombre_de_mots}")
