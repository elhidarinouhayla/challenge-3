from data import produits,prix
A = list(zip(produits,prix))
print(A)

def prix_superieur(prix):
    return prix > 30
resultat = list(filter(prix_superieur,prix))
print(resultat)