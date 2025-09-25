produits = ["clavier", "souris", "ecran", "chaise", "bureau", "lampe"]
prix = [45, 150, 1200, 855, 2000, 25]
A = list(zip(produits,prix))
print(A)

def prix_superieur(prix):
    return prix > 30
resultat = list(filter(prix_superieur,prix))
print(resultat)