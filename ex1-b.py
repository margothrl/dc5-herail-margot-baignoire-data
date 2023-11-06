# EXERCICE 1 - b
# Manipulation de chaînes : Demandez à l'utilisateur de saisir une phrase, puis affichez la phrase en majuscules, en minuscules et le nombre de mots.

phrase = input("Veuillez écrire votre phrase : ")

phrase_majuscules = ""
for caractere in phrase:
    if 'a' <= caractere <= 'z':
        majuscule = chr(ord(caractere) - 32)
        phrase_majuscules += majuscule
    else:
        phrase_majuscules += caractere
print("Phrase en majuscule : " + phrase_majuscules)

phrase_minuscules = ""
for caractere in phrase:
    if 'A' <= caractere <= 'Z':
        minuscule = chr(ord(caractere) + 32)
        phrase_minuscules += minuscule
    else:
        phrase_minuscules += caractere
print("Phrase en minuscule : " + phrase_minuscules)

nombre_de_mots = 0
est_dans_un_mot = False
for caractere in phrase:
    if caractere.isalpha():
        if not est_dans_un_mot:
            est_dans_un_mot = True
            nombre_de_mots += 1
    else:
        est_dans_un_mot = False
print("Nombre de mots dans la phrase : " + str(nombre_de_mots))
