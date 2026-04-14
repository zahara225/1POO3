from compte import CompteBancaire
if __name__=="__main__":
    compte1 = CompteBancaire("Alice", 500, 200) 
    compte2 = CompteBancaire("Bob", 200)

compte1.retirer(650)        
compte1.virement(compte2, 100)    

compte2.virement(compte1, 50)

print(compte1.solde)         
print(compte2.solde)         

compte2.afficher_historique()