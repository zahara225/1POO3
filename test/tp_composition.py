from datetime import date, timedelta


class GestionStock:

    def __init__(self, quantite=0, seuil_alerte=10):
        self._quantite    = quantite
        self.seuil_alerte = seuil_alerte

    def ajouter(self, qte):
        self._quantite += qte

    def retirer(self, qte):
        if qte > self._quantite:
            raise ValueError("Stock insuffisant")
        self._quantite -= qte

    @property
    def quantite(self): return self._quantite

    @property
    def alerte_stock_bas(self): return self._quantite < self.seuil_alerte
class GestionPeremption:
    def __init__(self, date_exp):
        self.date_expiration = date_exp

    def est_expire(self):
        return date.today() > self.date_expiration

    def jours_restants(self):
        return max(0, (self.date_expiration - date.today()).days)


# ── Assemblage par composition ───────────────────────────────────────
class ProduitAlimentaire:
    def __init__(self, ref, nom, prix, quantite, date_exp):
        self.reference  = ref
        self.nom        = nom
        self.prix       = prix
        self.stock      = GestionStock(quantite, seuil_alerte=20)
        self.peremption = GestionPeremption(date_exp)

    def calculer_valeur_stock(self):
        return self.prix * self.stock.quantite

    def __str__(self):
        statut = "EXPIRÉ" if self.peremption.est_expire() else f"{self.peremption.jours_restants()}j"
        return f"{self.nom} — stock : {self.stock.quantite} — péremption : {statut}"
    
class ProduitElectronique:
    def __init__(self, ref, nom, prix, quantite, garantie_ans):
        self.reference   = ref
        self.nom         = nom
        self.prix        = prix
        self.garantie    = garantie_ans
        self.stock       = GestionStock(quantite, seuil_alerte=5)
        

    def __str__(self):
        return f"{self.nom} — stock : {self.stock.quantite} — {self.garantie}an(s) garantie"

laptop = ProduitElectronique("PC-001", "MacBook Pro", 2499.99, 8, 2)
print(laptop)
print(f"Alerte stock bas ? {laptop.stock.alerte_stock_bas}")

yaourt = ProduitAlimentaire(
    "YGT-001", "Yaourt Bio", 0.99, 150,
    date.today() + timedelta(days=14)
)
print(yaourt)
print(f"Stock : {yaourt.stock.quantite}")
print(f"Jours restants : {yaourt.peremption.jours_restants()}")
print(f"Expiré ? {yaourt.peremption.est_expire()}")
yaourt.stock.retirer(140)
print(f"Stock après retrait : {yaourt.stock.quantite}")
print(f"Alerte stock bas ? {yaourt.stock.alerte_stock_bas}")

try:
    yaourt.stock.retirer(100)   
except ValueError as e:
    print(f"Erreur capturée : {e}")