# EXERCICE 2 - b
# Listes : Créez une liste de 10 nombres, trouvez le maximum, le minimum, et calculez la moyenne.

liste_de_nombres = [15, 22, 17, 30, 62, 48, 20, 35, 51, 89]


maximum = liste_de_nombres[0]  
for nombre in liste_de_nombres:
    if nombre > maximum:
        maximum = nombre

minimum = liste_de_nombres[0] 
for nombre in liste_de_nombres:
    if nombre < minimum:
        minimum = nombre

somme = 0
for nombre in liste_de_nombres:
    somme += nombre
moyenne = somme / len(liste_de_nombres)


print(f"Le maximum est : {maximum}")
print(f"Le minimum est : {minimum}")
print(f"La moyenne est : {moyenne}")
