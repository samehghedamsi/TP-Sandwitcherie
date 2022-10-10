
class Sandwich:

    def __init__(self, sandwich, size, kcal):
        self.name = str(sandwich)
        self.size = int(size)
        self.kcal = int(kcal)

    def __str__(self):
        return f"{self.name}" \
               f"{self.size}" \
               f"{self.kcal}"





