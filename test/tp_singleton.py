class GestionnaireInventaire:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Création du gestionnaire unique")
            cls._instance               = super().__new__(cls)
            cls._instance._produits     = {}
            cls._instance._observateurs = []
        return cls._instance

    def ajouter_produit(self, nom):
        self._produits[nom] = nom   

    def __len__(self): return len(self._produits)
    
g1 = GestionnaireInventaire()
g2 = GestionnaireInventaire()
print(g1 is g2)   
g1.ajouter_produit("Clavier")
print(len(g2))  
assert GestionnaireInventaire() is GestionnaireInventaire()
print("✓ Singleton validé")    