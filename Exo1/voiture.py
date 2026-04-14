class Voiture :

    nb_voiture = 0

    def __init__(self, marque, model, annee, kilometrage, prix_neuf) :
      self.marque = marque
      self.model = model
      self.annee = annee
      self.kiometrage = kilometrage
      self.prix_neuf = prix_neuf
      Voiture.nb_voiture += 1

    def afficher(self) :
      print(f"{self.marque}, {self.model}, {self.annee}, {self.kilometrage} | prix_neuf : {self.prix_neuf}")

    def est_recent(self):
      return self.annee >= 2000
      if annee.est_recent :
        print("true")

    def parcourir(self, distance) :
      self.kilometrage += distance

    def estime_valeur(self) :
      return round(self.kilometrage * 0,05 - self.prix_neuf)

#test
v1 = Voiture("Renault", "Clio", 2019, 45000, 15000)
v2 = Voiture("Peugeot", "208", 2022, 12000, 18000)

v1.parcourir(500)
print(v1.kilometrage)      
print(v1.estimer_valeur()) 

v2.afficher()

print(Voiture.nb_voitures) 

   


