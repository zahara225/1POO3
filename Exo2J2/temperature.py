class Temperature :
    def __init__(self, valeur_calsium):
        self._valeur_calsium = valeur_calsium
        
    @property
    def valeur_calsium(self):
        return self._valeur_calsium
    
    @valeur_calsium.setter
    def valeur_calsium(self, valeur) :
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour le prix")
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le prix doit être un nombre")
        if valeur < -273.15 or valeur > 1_000_000 :
            raise ValueError ("la valeur est hors limite")
        self._valeur_calsium = valeur
        
        
    @property
    def fahrenheit(self):
        return self._valeur_calsium *9/5 + 32
    
    @property
    def kelvin(self):
        return self._valeur_calsium + 273.15
    
    @property
    def etat(self):
        if self.valeur_calsium <= 0:
            return "solide"
        if self.valeur_calsium < 100:
            return "liquide"
        if self.valeur_calsium >= 100:
            return gazeux
        
    @classmethod 
    def depuis_fahrenheit(cls,valeur_f) :
         C = (valeur_f - 32) * 5/9.
         return cls(C)
     
    def est_compatible_avec(self, autre) :
        if not isinstance(autre, Temperature):
            raise TypeError ("les Temperatue doivent avoir le mm etat")
        return self.etat == autre.etat
        
        
    
     
     
     

    