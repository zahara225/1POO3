class Produit:
    tva = 20

    def __init__(self, reference, nom, prix_ht):
        if not Produit.valider_reference(reference):
            raise ValueError(f"Référence invalide : {reference}")
        self._reference = reference
        self._nom       = nom
        self._prix_ht   = prix_ht

    def __str__(self):
        return f"{self._nom} ({self._reference}) - {self._prix_ht}€ HT"
    
    @staticmethod
    def valider_reference(reference):
        if len(reference) != 6 : return False
        if reference[2] != "-" : return False
        return reference[:2].isalpha() and reference[3:].isdigit()
    @staticmethod
    def calculer_prix_ttc(prix_ht, tva=20):
        return round(prix_ht * (1 + tva / 100), 2)

        
           
print(Produit.valider_reference("KB-001"))   
print(Produit.valider_reference("CLAVIER"))   
print(Produit.valider_reference("K-001"))
print(Produit.calculer_prix_ttc(100))       
print(Produit.calculer_prix_ttc(100, 5.5)) 
p1 = Produit("KB-001", "Clavier", 79.99)   
p2 = Produit("MAUVAIS", "Test", 10.0)        
