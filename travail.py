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

def order(x):
    return x[1] 
A.sort()
print(A)


tup = tuple(A)
print(tup)

ma = max(tup,key=lambda a: a[1])
print(f"{ma} est le poduit le plus cher")
mi = min(tup,key=lambda b: b[1])
print(f"{mi} est le produit le moins cher")

# def bonus(prix):
#     return produits + LUXE
#     for x in prix:
#         if prix > 1000:
#             resultat = list(map(bonus,prix))
#         print(resultat)




