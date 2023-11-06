# EXERCICE 9
# Écrivez un script qui analyse les titres des e-mails marketing pour trouver le nombre d'occurrences d'un mot clé spécifique.

titres_emails = [
    "Promotion spéciale pour le Black Friday",
    "Offre exclusive pour les abonnés",
    "Vente flash de la rentrée",
    "Découvrez nos nouveautés",
    "Réduction de 20% sur tous les produits",
    "Super promotion CyberMonday",
    "Réductions spéciale pour nos membres gold, promotion sur tout le site !"
]

mot_cle = "promotion"

def compter_occurrences(titres, mot_cle):
    count = 0
    for titre in titres:
        titre_minuscules = titre.lower()
        mots = titre_minuscules.split()
        if mot_cle in mots:
            count += 1
    return count

nombre_occurrences = compter_occurrences(titres_emails, mot_cle)

print(f"Le mot clé '{mot_cle}' apparaît {nombre_occurrences} fois dans les titres des e-mails marketing sélectionnés.")
