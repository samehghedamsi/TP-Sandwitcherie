class Sandwich():

    def __init__(self, prix, calorie, taille, viande, legume):
        self.prix = prix
        self.calorie = calorie
        self.taille = taille
        self.viande = list(self.viande('poulet', 'boeuf', 'vegan'))
        self.legume = list(self.legume('fromage', 'salade', 'tomate', 'oignon'))

    def create_set_taille(self):
        self.taille = input(int('choisissez la taille de votre sandwich 15cm ou 30cm:  '))
        if self.taille != 15 or 30:
            print('saisie invalide, veuillez saisir une taille de pain entre 15cm et 30cm')
        else:
            return self.taille

    def create_set_prix_pain(self):
        if self.taille == 15:
            self.prix == 4.2
            return self.prix
        else:
            self.prix = 6.2
            return self.prix

    def create_set_calorie_pain(self):
        if self.taille == 15:
            self.calorie == 198
            return self.calorie
        else:
            self.calorie = 253
            return self.calorie



