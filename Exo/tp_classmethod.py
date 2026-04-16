class Produit:
    tva       = 20
    _nb_total = 0

    def __init__(self, reference, nom, prix_ht):
        self._reference = reference
        self._nom       = nom
        self._prix_ht   = prix_ht
        Produit._nb_total += 1

    def __str__(self):
        return f"{self._nom} ({self._reference}) - {self._prix_ht}€ HT"
    
    @classmethod
    def get_nb_total(cls):
        return cls._nb_total
    
    @classmethod
    def set_tva(cls, nouvelle_tva):
        cls.tva = nouvelle_tva
    
    @classmethod             
    def from_string(cls, chaine):
        ref, nom, prix = chaine.split(";")
        return cls(ref, nom, float(prix))
    
class ProduitElectronique(Produit):
    pass
        
p1 = Produit("KB-001", "Clavier", 79.99)
p2 = Produit("MS-001", "Souris", 49.99)
p3 = Produit.from_string("SC-001;Écran;199.99")
p4 = ProduitElectronique.from_string("TV-001;Télé;499.99")
print(type(p4))   
print(p3)  
print(Produit.get_nb_total())   
Produit.set_tva(5.5)
print(Produit.tva)                       
        