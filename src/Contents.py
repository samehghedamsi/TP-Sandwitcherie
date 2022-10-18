
class Contents:

    def __init__(self, viande, calorie):
        self.viande = str(viande)
        self.calorie = int(calorie)

    def __str__(self):
        return f"{self.viande}" \
               f"{self.calorie}"
