from data import produits,prix
A = list(zip(produits,prix))
print(A)

def prix_superieur(prix):
    return prix > 30
resultat = list(filter(prix_superieur,prix))
print(resultat)

for produits,prix  in A:
    print(f"produit {produits} coute {prix}DH")


A.sort(key=lambda x: x[1])
print(A)

tup = tuple(A)
print(tup)


