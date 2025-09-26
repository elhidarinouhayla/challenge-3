from data import produits,prix
A = list(zip(produits,prix))
print(A)

def prix_superieur(prix):
    return prix > 30
resultat = list(filter(prix_superieur,prix))
print(resultat)

for prod,pr  in A:
    print(f"produit {prod} coute {pr}DH")

print(prix)
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

def bonus(price):
    for x in price:
        if x > 1000:
            print(f"produit coute {x}DH (LUXE)")  
bonus(prix)

# etape 2:
# def le_de_produit():
#     produit1 = input("entrer un produit: ")
#     for produit2 in produits:
#         if produit1 in produits:
#             print(f"{produits}:{prix}")

# def new_produit_prix():
    # new_produit = input("enter un nauveau produit: ")
    # new_prix = input(int("entrer un nauveau prix: "))
    # new_produit.append(produits)
    # new_prix.append(prix)

message = ("""1. Chercher un produit dans la list
2. Ajouter un produit 
3. Quitter""" )
print(message)

while True:
    
    choix = int(input("Entrer un choix: "))
    if choix == 1: 
        print(choix)
        produit1 = input("entrer un produit: ") 
        produits2 = [] 
        for index,contenu in enumerate(A):
            
            """ print(pro)
            print(pri[0]) """
            if produit1 == contenu[0]:
                produits2.append(contenu[0])
                indexprix = index
        if produit1 in produits2: 
            all = A[indexprix]
            print(f"l9itha sawya {all[1]}")
              
        else:
                print("le produit n'appartient pas a`la liste !")
    elif choix == 2:
        print(choix)
        """ new_produit = input("Enter un nauveau produit: ") 
        new_prix = int(input("Entrer un nauveau prix: ")) 
        produits.append(new_produit) 
        prix.append(new_prix) """ 
    elif choix == 3:
        print("Quitter") 
        break 
    else:
        print("le numero n'existe pas !")
    
