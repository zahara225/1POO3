from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass

class ObservateurStock(ABC):
    @abstractmethod
    def mise_a_jour(self, action, produit): pass

class AlerteStockBas(ObservateurStock):
    def __init__(self, seuil=10): self.seuil = seuil
    def mise_a_jour(self, action, produit):
        if hasattr(produit, "quantite") and produit.quantite < self.seuil:
            print(f"⚠ ALERTE : {produit.nom} — {produit.quantite} unités")

class LogMouvement(ObservateurStock):
    def mise_a_jour(self, action, produit):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"[{ts}] {action.upper()} — {produit.nom}")

@dataclass
class SimpleProduit:
    nom: str
    quantite: int

class Gestionnaire:
    def __init__(self):
        self._observateurs = []

    def abonner(self, obs):
        self._observateurs.append(obs)

    def ajouter(self, produit):
        for obs in self._observateurs:
            obs.mise_a_jour("ajout", produit)
class NotificationEmail(ObservateurStock):
    def mise_a_jour(self, action, produit):
        print(f"📧 Email envoyé : {action} sur {produit.nom}")


g = Gestionnaire()
g.abonner(LogMouvement())
g.abonner(AlerteStockBas(seuil=5))

clavier = SimpleProduit("Clavier", quantite=3)
g.ajouter(clavier)
ecran = SimpleProduit("Écran", quantite=50)
g.ajouter(ecran)
g.abonner(NotificationEmail())
g.ajouter(SimpleProduit("Souris", quantite=2))
            