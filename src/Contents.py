
class Contents:

    def __init__(self, name, kcal):
        self.name = str(name)
        self.kcal = int(kcal)

    def __str__(self):
        return f"{self.name}" \
               f"{self.kcal}"
