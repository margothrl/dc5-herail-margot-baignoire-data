# EXERCICE 7
# Écrire une fonction qui calcule le montant total dépensé par tous les clients.

def montant_total_depense(liste_clients):
    total = 0
    for client in liste_clients:
        montant = client.get("montant_depense", 0) 
        total += montant
    return total

liste_clients = [
    {"nom": "Client 1", "montant_depense": 132},
    {"nom": "Client 2", "montant_depense": 28},
    {"nom": "Client 3", "montant_depense": 150}
]

total_depense = montant_total_depense(liste_clients)

print(f"Le montant total dépensé par tous les clients est de {total_depense}€.")
