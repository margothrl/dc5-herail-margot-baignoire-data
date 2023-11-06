# EXERCICE 2 - a
# Créez une liste des dépenses marketing mensuelles et calculez les dépenses totales de l'année.

depenses_mensuelles = [500, 1200, 800, 1500, 1300, 1100, 90, 1000, 950, 1200, 1400, 1100]

depenses_annuelles = 0
for depense in depenses_mensuelles:
    depenses_annuelles += depense

print(f"Les dépenses marketing totales de l'entreprise sur l'année sont de {depenses_annuelles}€.")
