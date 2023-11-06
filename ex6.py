# EXERCICE 6
# Parcourir la liste des clients et afficher ceux qui ont dépensé plus de 100€.

liste_clients = []

for i in range(1, 51):
    client = {
        "nom": f"Client {i}",
        "email": f"client{i}@exemple.com",
        "montant_depense": 10 + i * 5
    }
    liste_clients.append(client)

# Parcourir la liste de clients et afficher ceux qui ont dépensé plus de 100€
for client in liste_clients:
    if client["montant_depense"] > 100:
        print(f"Nom : {client['nom']}, Email : {client['email']}, Montant dépensé : {client['montant_depense']}€")

