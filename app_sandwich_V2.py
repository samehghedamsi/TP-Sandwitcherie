
class Sandwich():

    def __init__(self, taille):
        self.taille = taille

    def definir_taille(self, mon_sandwich):
        while mon_sandwich.taille != 15 and mon_sandwich.taille != 30:
            mon_sandwich = Sandwich(int(input("veuillez saisir une taille correct, 15 ou 30:")))
        if mon_sandwich == 15 or mon_sandwich == 30:
            print( mon_sandwich.taille )

    def create_calorie_pain(self):
        if mon_sandwich.taille == 15:
            mon_sandwich.calorie = 198
        else:
            mon_sandwich.calorie = 253
        print(mon_sandwich.calorie)

    def create_prix_pain(self):
        if mon_sandwich.taille == 15:
            mon_sandwich.prix = 4.2
        else:
            mon_sandwich.prix = 6.2
        print(mon_sandwich.prix)

    def ajout_ingredient(self, mes_ingredients):
        list_ingredient_cal= {'Poulet':239,'Boeuf':250,'Vegan':206,'Fromage':402,'Salade':16,'Tomate':21,'Oignons':40 }
        list_ingredient_prix= {'Poulet':0.2,'Boeuf':0.2,'Vegan':0.3,'Fromage':0.5,'Salade':0.2,'Tomate':0.2,'Oignons':0.3, 'sauce':0.55 }
        list_sauce_cal = {'Mayo':120,'Ketchup':189,'Blanche':110,'Andalouse':200}
        nbr_ing = int(input("combien d'ingredients voulez vous ajouter: "))
        list_ing = ['pain']
        list_ing_prix = [mon_sandwich.prix]
        list_ing_calorie = [mon_sandwich.calorie]
        for i in range (nbr_ing):
            ajout_ing = input("veuillez saisir l'ingredient à ajouter, finissez votre ajout en tapant sur entree sans rien indiquer")
            if ajout_ing not in list_ingredient_prix:
                ajout_ing = input('saisissez des ingredients corrects:')
                i -= 1
            if ajout_ing in list_ingredient_prix:
                i = 0
                list_ing.append(ajout_ing)
                list_ing_prix.append(mes_ingredients.prix)
                list_ing_calorie.append(mes_ingredients.calorie)
                print(list_ing)
                mes_ingredients.prix = list_ingredient_prix.get(ajout_ing)
                mes_ingredients.calorie = list_ingredient_cal.get(ajout_ing)
                print(list_ing_prix, list_ing_calorie)
                i += 1
                mes_ingredients.prix = sum(list_ing_prix)
                mes_ingredients.calorie = sum(list_ing_calorie)
        print(mes_ingredients.prix, mes_ingredients.calorie)


mon_sandwich = Sandwich(int(input("veuillez saisir la longueur de votre pain 15 ou 30:")))
print(mon_sandwich.taille)
mon_sandwich.definir_taille(mon_sandwich)
mon_sandwich.create_calorie_pain()
mon_sandwich.create_prix_pain()
mon_sandwich.ajout_ingredient(mon_sandwich)