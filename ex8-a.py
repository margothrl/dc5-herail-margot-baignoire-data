# EXERCICE 8
# Utilisez la bibliothèque `pandas` pour lire un fichier CSV contenant des données de ventes et affichez les cinq premières lignes.

import pandas as pd

fichier_csv = "ex8-a.csv"
donnees_ventes = pd.read_csv(fichier_csv)

print(donnees_ventes.head())
