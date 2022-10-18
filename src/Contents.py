
class Contents:

    def __init__(self, viande, calorie, prix):
        self.viande = str(viande)
        self.calorie = int(calorie)
        self.prix = float(prix)

    def __str__(self):
        return f"{self.viande}" \
               f"{self.calorie}" \
               f"{self.prix}"

    def get(self):
        self.viande = "poulet", "boeuf", "vegan"
        #self.calorie = 239
       # return f"{self.viande} "
               #f"{self.calorie}"

    def viande30(self):
        self.prix = self.prix * 2
