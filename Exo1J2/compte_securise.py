class CompteBancaire:
    taux_interet = 0.02

    def __init__(self, titulaire, solde, decouverte_autorise=0):
        self.titulaire = titulaire
        self._solde = solde
        self._decouverte_autorise = decouverte_autorise
        self.historique = []

    @property
    def titulaire(self):
        return self._titulaire

    @titulaire.setter
    def titulaire(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("titulaire doit etre une chaine")
        if not valeur.strip():
            raise ValueError("titulaire doit pas etre vide")
        self._titulaire = valeur.strip()

    @property
    def decouverte_autorise(self):
        return self._decouverte_autorise

    @decouverte_autorise.setter
    def decouverte_autorise(self, montant):
        if not isinstance(montant, (int, float)):
            raise TypeError("decouverte_autorise est un nombre positif ou nul")
        if montant < 0:
            raise ValueError("decouverte_autorise doit etre >= 0")
        self._decouverte_autorise = round(montant, 2)

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, valeur):
        self._solde = valeur

    @property
    def est_a_decouverte(self):
        return self.solde < 0

    @property
    def nb_operation(self):
        return len(self.historique)

    def deposer(self, montant):
        if isinstance(montant, bool):
            raise TypeError("montant prend pas de bool")
        if not isinstance(montant, (int, float)):
            raise TypeError("Le montant doit être un nombre")
        if montant <= 0:
            raise ValueError("Le prix doit être positif")

        self.solde += montant
        self.historique.append(f"Depot de {montant}")
        print(f"{montant} depose avec succes")

    def retirer(self, montant):
        if self.solde - montant >= -self.decouverte_autorise:
            self.solde -= montant
            self.historique.append(f"Retrait de {montant}")
            return True
        else:
            print("operation impossible")
            self.historique.append(f"Echec de {montant}")
            return False

    def virement(self, autre_compte, montant):
        if self.retirer(montant):
            autre_compte.deposer(montant)
            self.historique.append(f"Virement de {montant}")
            print("virement effectue")
        else:
            print("virement echoue")

    def afficher_historique(self):
        print("historique des operation :")
        for operation in self.historique:
            print(f"[{self.titulaire}] {operation}")

    def appliquer_interet(self):
        if self.solde > 0:
            interet = self.solde * CompteBancaire.taux_interet
            self.solde += interet
            self.historique.append(f"interet ajoute : {interet}")