
class Sandwich:
    def __init__(self, prix, sandwich, taille, cal, viande):
        self.prix = float(prix)
        self.name = str(sandwich)
        self.taille = int(taille)
        self.cal = int(cal)
        self.viande = str(viande)

    def __str__(self):
        return f"{self.prix}" \
               f"{self.name}" \
               f"{self.taille}" \
               f"{self.cal}" \
               f"{self.viande}"

    def get(self):
        return self.name

    def viande(self, calorie):
        self.viande = 'poulet', 'boeuf', 'vegan'
        self.calorie = 234
        return f"{self.viande} " \
               f"{self.calorie}"
