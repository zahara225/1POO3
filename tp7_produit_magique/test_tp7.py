from produit import Produit

if __name__=="__main__" :
    p1 = Produit("KB-001", "Clavier", 79.99)
    p2 = Produit.from_dict({"ref": "MS-001", "nom": "Souris", "prix": 49.99})
    p3 = Produit("KB-001", "Clavier v2", 89.99)

    print(p1)                    
    print(repr(p1))              
    print(p1 == p3)              
    print(p1 < p2)              

    tries = sorted([p1, p2])
    print([str(p) for p in tries])

    catalogue = {p1, p2, p3}
    print(len(catalogue))       

    print(Produit.validation_prix(49.99))  
    print(Produit.validation_prix(-10))   