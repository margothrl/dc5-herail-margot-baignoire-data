# EXERCICE 5
# Créer une liste de dictionnaires, où chaque dictionnaire contient des informations sur un client (nom, email, montant dépensé). Minimum 50 entrées

liste_clients = []

for i in range(1, 51):
    client = {
        "nom": f"Client {i}",
        "email": f"client{i}@exemple.com",
        "montant_depense": 10 + i * 5
    }
    liste_clients.append(client)

for client in liste_clients:
    print(f"Nom : {client['nom']}, Email : {client['email']}, Montant dépensé : {client['montant_depense']}€")
