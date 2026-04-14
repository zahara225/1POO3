class CompteBancaire :
    taux_interet = 0.02

    def __init__(self, titulaire, solde, decouverte_autorise=0):
        self.titulaire = titulaire
        self.solde = solde
        self.decouverte_autorise = decouverte_autorise
        self.historique = []
        

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            self.historique.append(f"Depot de {montant}")
            print(f"{montant} depose avec succes")

    def retirer(self, montant):
        if self.solde - montant >= - self.decouverte_autorise :
            self.solde -= montant 
            self.historique.append(f"Retrait de {montant}")       
            return True
        else:
            print("operation impossible") 
            self.historique.append(f"Echec de {montant}")      
            return False

    def virement(self, autre_compte, montant) :
        if self.retirer(montant) :
            autre_compte.deposer(montant)
            self.historique.append(f"Virement de {montant}")
            print("virement effectue")
        else:
            print("virement echoue")


    def afficher_historique(self) :
        print("historique des operation :")
        for operation in self.historique:
            print("-", operation)

    def appliquer_interet(self, solde, taux_interet) :
        if self.solde > 0 :
           interet = self.solde * CompteBancaire.taux_interet
           self.solde += interet
           self.historique.append(f"interet ajoute :{interet}")
        


#test

           c1 = CompteBancaire("Alice", 500, 200) 
           c2 = CompteBancaire("Bob", 200, 100)

           c1.retirer(650)      
           c1.virement(c2, 100)

           c2.virement(c1, 50)     
           print(c1.solde)         
           print(c2.solde)         

           c2.afficher_historique()            
        




