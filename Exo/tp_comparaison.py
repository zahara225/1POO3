class Produit:
    def __init__(self, reference, nom, prix_ht):
        self._reference = reference
        self._nom       = nom
        self._prix_ht   = prix_ht
    def __str__(self):
        return f"{self._nom} ({self._reference}) - {self._prix_ht}€ HT"
    
    def __eq__(self, other):          
        if not isinstance(other, Produit): return False
        return self._reference == other._reference
    def __hash__(self):               
        return hash(self._reference)

    def __lt__(self, other):           
        return self._prix_ht < other._prix_ht

p1 = Produit("KB-001", "Clavier", 79.99)
p2 = Produit("MS-001", "Souris", 49.99)
p3 = Produit("KB-001", "Clavier v2", 89.99)
print(p1 == p3)   
print(p1 == p2)  
catalogue = {p1, p2, p3}  
print(len(catalogue)) 
for p in sorted([p1, p2]):
    print(p)
   