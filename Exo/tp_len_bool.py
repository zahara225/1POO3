class Produit:
    def __init__(self, reference, nom, prix_ht):
        self._reference = reference
        self._nom       = nom
        self._prix_ht   = prix_ht
    def __str__(self):
        return f"{self._nom} ({self._reference}) - {self._prix_ht}€ HT"

class Inventaire:
    def __init__(self):
        self._produits = []
    def ajouter(self, produit):
        self._produits.append(produit)
    
    def __len__(self):
        return len(self._produits)
    
    def __bool__(self):       
        return len(self._produits) > 0   
     
    def __getitem__(self, index):  
        return self._produits[index]    

inv = Inventaire()
p1  = Produit("KB-001", "Clavier", 79.99)
p2  = Produit("MS-001", "Souris", 49.99)

print(len(inv))        
if inv: print("non vide")
inv.ajouter(p1)
print(bool(inv))    
if inv:
    print(f"{len(inv)} produit(s) en stock")
    
inv.ajouter(p2)
print(inv[0])     
print(inv[-1])    
for p in inv: 
    print(p)