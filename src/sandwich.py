
class Sandwich:
    def __init__(self, prix, sandwich, taille, cal):
        self.prix = float(prix)
        self.name = str(sandwich)
        self.taille = int(taille)
        self.cal = int(cal)


    def __str__(self):
        return f"{self.prix}" \
               f"{self.name}" \
               f"{self.taille}" \
               f"{self.cal}"


    def get(self):
        return self.name

