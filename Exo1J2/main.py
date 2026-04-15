from compte_securise import CompteBancaire

if __name__=="__main__" :
   
   
   compte1 = CompteBancaire("Alice", 500, 200)
   
   
   compte1.deposer(100)          
   compte1.retirer(800)          
   
   compte1.retirer(50)           

   print(compte1.solde)           
   print(compte1.est_a_decouverte)  
   print(compte1.nb_operation)   

   compte1.afficher_historique()

   compte1.titulaire = ""     
   compte1.deposer(True)      
