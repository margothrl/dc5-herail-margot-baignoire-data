# EXERCICE 3
#  Écrivez un script qui détermine si une campagne a été rentable en comparant le coût de la campagne au revenu généré.

cout_campagne = float(input("Entrez le coût de la campagne : "))
revenu_genere = float(input("Entrez le revenu généré : "))

if revenu_genere > cout_campagne:
    print("La campagne est rentable.")
elif revenu_genere < cout_campagne:
    print("La campagne n'est pas rentable.")
else:
    print("La campagne est parfaitement équilibrée (coût égal au revenu).")
