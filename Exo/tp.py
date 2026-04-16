class Produit:
    def __init__(self, reference, nom, prix_ht):
        self._reference = reference
        self._nom       = nom
        self._prix_ht   = prix_ht
    
    def __str__(self):
        return f"{self._nom} ({self._reference}), {self._prix_ht}£ HT "
    
    def __repr__(self) :
        return f"produit('{self._reference}', '{self._nom}', '{self._prix_ht}')"
p1 = Produit("KB-001", "Clavier RGB", 79.99)
p2 = Produit("MS-001", "Souris", 49.99)

print(p1)
print(repr(p1))