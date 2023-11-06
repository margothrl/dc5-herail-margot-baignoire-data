# EXERCICE 4
# Fonctions : Écrivez une fonction qui calcule le factoriel d'un nombre.

def factoriel(n):
    if n < 0:
        return "Le factoriel n'est défini que pour les entiers positifs."
    elif n == 0:
        return 1
    else:
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        return resultat

nombre = 5
fact = factoriel(nombre)
print(f"Le factoriel de {nombre} est {fact}")
