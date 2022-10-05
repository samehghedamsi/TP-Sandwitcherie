'''Vous êtes chargé de développer une application pour le compte du gérant d'un petit restaurant qui vend des sandwichs.

Le gérant souhaite que sa clientèle puisse personnaliser son sandwich avec leurs prix modifiés en conséquence.

Exemple :
    - si un client commande un sandwich "sans oignon", il bénéficiera d'une légère réduction sur le prix de son sandwich.
    - si un client décide d'ajouter du fromage en plus à son sandwich : le supplément se répercute par une légère augmentation du prix.

Le nombre de calories total et le prix seront affichés à la fin du programme, un résumé du contenu du sandwich doit être affiché avec une validation du client. En cas de non-validation, le client recommence sa commande.

Il n'est pas impossible que le restaurateur décide de créer un site internet ou une application mobile dans l'avenir, pensez-y.

Ecrivez un logiciel de gestion des commandes pour ce restaurateur exécutable dans le terminal.

Informations sur les prix des ingrédients et calories du pain au choix :
Pain Sandwich 15cm : 4.2 € /  198kcal
Pain Sandwich 30cm : 6.2 € /  253kcal (la quantité des ingrédients de base doit être doublé)
Ingrédient et calories de base pouvant être ajouté et retiré :
Poulet   : 0.2 €    /  239kcal
Boeuf    : 0.2 €    /  250kcal
Vegan     : 0.3 €    /  206kcal
Fromage  : 0.5 €    /  402kcal
Salade   : 0.2 €    /   16kcal
Tomate   : 0.2 €    /   21kcal
Oignons  : 0.3 €    /   40kcal
Sauce    : 0.55€    /   sans sauce : 0€
            Mayo       : 120kcal
            Ketchup    : 189kcal
            Blanche    : 110kcal
            Andalouse  : 200kcal
Bonus :
- Après validation, choix de la boisson (libre cours à votre  imagination) => prix : 1,50€
- Dessert ? (libre cours à votre imagination)'''

import unittest
class TestClass(unittest.TestCase):

    # création des sandwiches avec tous les ingrédients en 15 et 30 cm, avec sauce et sans sauce
    def setup(self):
        self.mon_sandwich_complet_15 = sandwich('Poulet', 'Boeuf', 'Vegan', 'Fromage', 'Salade', 'Tomate', 'Oignons', 'sauce')
        self.mon_sandwich_complet_30 = sandwich('Poulet', 'Boeuf', 'Vegan', 'Fromage', 'Salade', 'Tomate', 'Oignons', 'sauce')
        self.mon_sandwich_complet_15_nosauce = sandwich('Poulet', 'Boeuf', 'Vegan', 'Fromage', 'Salade', 'Tomate', 'Oignons')
        self.mon_sandwich_complet_30_nosauce = sandwich('Poulet', 'Boeuf', 'Vegan', 'Fromage', 'Salade', 'Tomate', 'Oignons')

    # Vérifier que les valeurs numériques ne renvoient pas des string
    def valeurs_numeriques_pas_en_string(self):
        self.mon_sandwich_complet_15.prix = 6.65
        self.assertIsNot(self.mon_sandwich_complet_15.prix, "6.65")

    # Vérifier que les valeurs numériques renvoient des float
    def valeurs_numeriques_sont_des_float(self):
        self.mon_sandwich_complet_15.prix = 6.65
        self.assertEqual(self.mon_sandwich_complet_15.prix), float(6.65)

    def test_prix_defaut(self):
        self.assertequal(self.mon_sandwich_complet_15.prix, 6.65)   #le prix par défaut 11,10 (pain + 2 X tous les ingrédients)
        self.assertequal(self.mon_sandwich_complet_30.prix, 11.10)  #le prix par défaut 6,65 (pain + tous les ingrédients)

    def test_calorie_defaut(self):
        self.assertequal(self.mon_sandwich_complet_15_nosauce.calorie, 1372,'kcal')     #test sandwich 15 et 30 calorie par défaut sans sauce
        self.assertequal(self.mon_sandwich_complet_30_nosauce.calorie, 2601,'kcal')

    def test_calorie_saucein(self):
        self.assertequal(self.mon_sandwich_complet_15_nosauce.calorie + self.ma_sauce.mayo.calorie, 1492,'kcal', )    #test sandwich 15 calorie avec sauce
        self.assertequal(self.mon_sandwich_complet_30_nosauce.calorie + self.ma_sauce.andalouse.calorie, 2801,'kcal')  #test sandwich 15 calorie avec sauce

    def test_prix_ingredient_out(self):
       self.assertNotEqual(self.mon_sandwich_complet_15_nosauce.prix, 6.65)    #test prix sandwich sans sauce, return error
       self.assertNotEqual(self.mon_sandwich_complet_30_nosauce.prix, 11.10)
       self.assertEqual(self.mon_sandwich_complet_15.prix - self.mon_ingredient.fromage.prix, 6.15)   #test  prix sandwich 15 ingredients fromage en moins
       self.assertEqual(self.mon_sandwich_complet_30.prix - self.mon_ingredient.fromage.prix, 10.60)  #test prix sandwich 30 ingredients fromage en moins