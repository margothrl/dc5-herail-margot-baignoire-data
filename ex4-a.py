# EXERCICE 4 - a
# Définissez une fonction pour convertir le CTR (Click-Through Rate) en pourcentage. Testez la fonction avec plusieurs entrées.

def convertir_CTR(clics, impressions):
    if impressions == 0:
        return 0
    ctr = (clics / impressions) * 100
    return ctr

clics_1, impressions_1 = 300, 5000
ctr_1 = convertir_CTR(clics_1, impressions_1)
print(f"CTR 1 : {ctr_1:.2f}%")

clics_2, impressions_2 = 50, 1000
ctr_2 = convertir_CTR(clics_2, impressions_2)
print(f"CTR 2 : {ctr_2:.2f}%")

clics_3, impressions_3 = 100, 1200
ctr_3 = convertir_CTR(clics_3, impressions_3)
print(f"CTR 3 : {ctr_3:.2f}%")
