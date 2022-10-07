import unittest
"""
Vous êtes chargé de développer une application pour le compte du gérant d'un petit restaurant qui vend des sandwichs.

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
- Dessert ? (libre cours à votre imagination)
"""
class TestSandwich(unittest.TestCase):
# test création de la class
    def setUp(self):
        self.monobjet = Sandwich()
# test objet sandwich crée
    def test_objet_Sandwich_create(self):
        self.assertIsInstance(self.monobjet, Sandwich)
# test taille du sandwich à 15
    def test_attribut_taille_15(self):
        self.monobjet.set_taille = 15
        self.assertEqual(self.monobjet.taille, 15)
# test taille du sandwich à 30
    def test_attribut_taille_30(self):
        self.monobjet.set_taille= 30
        self.assertEqual(self.monobjet.taille, 30)
# test calorie du pain 15
    def test_prix_pain_15(self):
        self.monobjet.set_taille = 15
        self.assertEqual(self.monobjet.prix, 4.2)
# test prix unitaire du pain 15
    def test_cal_pain_15(self):
        self.monobjet.set_taille = 15
        self.assertEqual(self.monobjet.cal, 198)
# test calorie du pain 30
    def test_prix_pain_30(self):
        self.monobjet.set_taille = 30
        self.assertEqual(self.monobjet.prix, 6.2)
# test prix unitaire du pain 30
    def test_cal_pain_30(self):
        self.monobjet.set_taille = 30
        self.assertEqual(self.monobjet.cal, 253)

# test choix de viande poulet ok
    def test_attribut_viande(self):
        self.monobjet.set_viande = "poulet"
        self.assertEqual(self.monobjet.viande, "poulet")
# test choix de viande poisson impossible
    def test_attribut_mauvaise_viande(self):
        self.monobjet.set_viande = "poisson"
        self.assertNotIn(self.monobjet.viande, ("poulet","boeuf","vegan"))
# test calorie du poulet
    def test_cal_poulet_15(self):
        self.monobjet.set_viande = "poulet"
        self.assertEqual(self.monobjet.calorie, 239)
# test prix unitaire du poulet
    def test_prix_poulet_15(self):
        self.monobjet.set_viande = "poulet"
        self.assertEqual(self.monobjet.prix, 0.2)
# test calorie du poulet
    def test_cal_poulet_30(self):
        self.monobjet.set_viande = "poulet"
        self.assertEqual(self.monobjet.calorie, 478)
# test prix unitaire du poulet
    def test_prix_poulet_30(self):
        self.monobjet.set_viande = "poulet"
        self.assertEqual(self.monobjet.prix, 0.4)
# test calorie du boeuf
    def test_cal_boeuf_15(self):
        self.monobjet.set_viande = "boeuf"
        self.assertEqual(self.monobjet.calorie, 250)
# test prix unitaire du boeuf
    def test_prix_boeuf_15(self):
        self.monobjet.set_viande = "boeuf"
        self.assertEqual(self.monobjet.prix, 0.2)
# test calorie du boeuf
    def test_cal_boeuf_30(self):
        self.monobjet.set_viande = "boeuf"
        self.assertEqual(self.monobjet.calorie, 500)
# test prix unitaire du boeuf
    def test_prix_boeuf_30(self):
        self.monobjet.set_viande = "boeuf"
        self.assertEqual(self.monobjet.prix, 0.4)
# test calorie du vegan
    def test_cal_vegane_15(self):
        self.monobjet.set_viande = "vegan"
        self.assertEqual(self.monobjet.calorie, 206)
# test prix unitaire du vegan
    def test_prix_vegane_15(self):
        self.monobjet.set_viande = "vegan"
        self.assertEqual(self.monobjet.prix, 0.3)
# test calorie du vegan
    def test_cal_vegane_30(self):
        self.monobjet.set_viande = "vegan"
        self.assertEqual(self.monobjet.calorie, 412)
# test prix unitaire du vegan
    def test_prix_vegane_30(self):
        self.monobjet.set_viande = "vegan"
        self.assertEqual(self.monobjet.prix, 0.6)

# sandwich maison15 pain 15cm, poulet, fsto, mayo, sans sup
    def test_prix_sand_15_maison(self):
        self.monobjet.set_taille = 15
        self.monobjet.set_viande = "poulet"
        self.monobjet.fromage = 1
        self.monobjet.salade = 1
        self.monobjet.tomate = 1
        self.monobjet.oignon = 1
        self.monobjet.choixSauce= 1
        self.monobjet.mayo = 1
        self.monobjet.supp =0
        self.assertEqual(self.monobjet.prixTotal, 6.15)
        self.assertEqual(self.monobjet.caloriesTotal, 1036)

# sandwich maison pain 30cm, boeuf, fsto, mayo, sans sup
    def test_prix_sand_30_maison_mayo(self):
        self.monobjet.set_taille = 30
        self.monobjet.set_viande = "boeuf"
        self.monobjet.fromage = 1
        self.monobjet.salade = 1
        self.monobjet.tomate = 1
        self.monobjet.oignon = 1
        self.monobjet.choixSauce= 1
        self.monobjet.mayo = 1
        self.monobjet.supp =0
        self.assertEqual(self.monobjet.prixTotal, 10.10)
        self.assertEqual(self.monobjet.caloriesTotal, 1951)

# sandwich maison15 pain 30cm, boeuf, fsto, andalouse, sans sup
    def test_prix_sand_30_maison_andalouse(self):
        self.monobjet.set_taille = 30
        self.monobjet.set_viande = "boeuf"
        self.monobjet.fromage = 1
        self.monobjet.salade = 1
        self.monobjet.tomate = 1
        self.monobjet.oignon = 1
        self.monobjet.choixSauce= 1
        self.monobjet.andalouse = 1
        self.monobjet.supp =0
        self.assertEqual(self.monobjet.prixTotal, 10.10)
        self.assertEqual(self.monobjet.caloriesTotal, 2111)

# sandwich maison15 pain , vegan, sto, sans sauce, sans sup
    def test_prix_sand_15_maison_vegan_sans_sauce(self):
        self.monobjet.set_taille = 15
        self.monobjet.set_viande = "vegan"
        self.monobjet.fromage = 0
        self.monobjet.salade = 1
        self.monobjet.tomate = 1
        self.monobjet.oignon = 1
        self.monobjet.choixSauce = 0
        self.monobjet.andalouse = 0
        self.monobjet.supp =0
        self.assertEqual(self.monobjet.prixTotal, 5.2)
        self.assertEqual(self.monobjet.caloriesTotal, 481)
# sandwich maison 30 pain , vegan, sto, sans sauce, sans sup
    def test_prix_sand_30_maison_vegan_sans_sauce(self):
        self.monobjet.set_taille= 30
        self.monobjet.set_viande = "vegan"
        self.monobjet.fromage = 0
        self.monobjet.salade = 1
        self.monobjet.tomate = 1
        self.monobjet.oignon = 1
        self.monobjet.choixSauce = 0
        self.monobjet.andalouse = 0
        self.monobjet.supp = 0
        self.assertEqual(self.monobjet.prixTotal, 8.2)
        self.assertEqual(self.monobjet.caloriesTotal, 819)

# test d'affichage
    def test_affichage_fin_de_commande(self):
        self.monobjet.set_taille= 30
        self.monobjet.set_viande = "vegan"
        self.monobjet.fromage = 0
        self.monobjet.salade = 1
        self.monobjet.tomate = 1
        self.monobjet.oignon = 1
        self.monobjet.choixSauce = 0
        self.monobjet.andalouse = 0
        self.monobjet.supp = 0
        self.assertEqual(self.monobjet.affichage_final_commande, "Pour un prix de : 8.2 euros et pour: 819 kilocalories, vous avez un sandwich vegan de 30 cm, composé de salade, tomate, oignon et sans sauce")

#test de validation refus
    def test_de_non_validation_de_la_commande(self):
        self.monobjet.validationFinale = 0
        self.assertEqual(self.monobjet.validation, 0)

#test de validation accepte
    def test_de_validation_de_la_commande(self):
        self.monobjet.validationFinale = 1
        self.assertEqual(self.monobjet.validation, 1)

unittest.main()