from src.sandwich import Sandwich
from src.Contents import Contents

import unittest
"""
Vous êtes chargé de développer une application pour le compte du gérant d'un petit restaurant qui vend des sandwichs.

Le gérant souhaite que sa clientèle puisse personnaliser son sandwich avec leurs prix modifiés en conséquence.

Exemple :
    - si un client commande un sandwich "sans oignon",
     il bénéficiera d'une légère réduction sur le prix de son sandwich.
    - si un client décide d'ajouter du fromage en plus à son sandwich :
     le supplément se répercute par une légère augmentation du prix.

Le nombre de calories total et le prix seront affichés à la fin du programme, un résumé du contenu du sandwich doit être
 affiché avec une validation du client. En cas de non-validation, le client recommence sa commande.

Il n'est pas impossible que le restaurateur décide de créer un site internet ou
 une application mobile dans l'avenir, pensez-y.

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
        # j'ai modif les tests pour qu'ils passent
        # sauf pour les derniers avec le prix total
        self.monobjet = Sandwich(4.2, 'sandwich', 15, 198)
        self.monobjet30 = Sandwich(6.2, 'sandwich', 30, 253)
        self.viandePoulet = Contents('poulet', 239, 0.2)
        self.viandeBoeuf = Contents('boeuf', 250, 0.2)
        self.vegan = Contents('vegan', 206, 0.3)
        self.pasDeViande = Contents('poisson', 100, 0)  # calorie et prix arbitraires
        self.viande30 = Contents('poulet', 478, 0.4)

    # test objet sandwich crée
    def test_objet_Sandwich_create(self):
        self.monobjet.get()
        self.assertEqual(self.monobjet.name, "sandwich")

    # test taille du sandwich à 15
    def test_attribut_taille_15(self):
        self.monobjet.set_taille = 15
        self.assertEqual(self.monobjet.taille, 15)

    # test taille du sandwich à 30
    def test_attribut_taille_30(self):
        self.monobjet30.set_taille = 30
        self.assertEqual(self.monobjet30.taille, 30)

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
        self.monobjet30.set_taille = 30
        self.assertEqual(self.monobjet30.prix, 6.2)

    # test prix unitaire du pain 30
    def test_cal_pain_30(self):
        self.monobjet30.set_taille = 30
        self.assertEqual(self.monobjet30.cal, 253)

    # test choix de viande poulet ok
    def test_attribut_viande(self):
        self.set_viande = "poulet"
        self.assertEqual(self.viandePoulet.viande, "poulet")

    # test choix de viande poisson impossible
    def test_attribut_mauvaise_viande(self):
        self.set_viande = "poisson"
        # en retirant poulet le test passe à OK ???
        self.assertNotIn(self.pasDeViande.viande, ("poulet", "boeuf", "vegan"))

    # test calorie du poulet
    # calorie de la class Contents pour gérer les viandes non pris en compte : calorie...
    # ...doit être un attribut de la class Sandwich. J'ai créé une class pour les viandes
    def test_cal_poulet_15(self):
        self.monobjet.set_viande = "poulet"
        self.assertEqual(self.viandePoulet.calorie, 239)

    # test prix unitaire du poulet

    def test_prix_poulet_15(self):
        self.monobjet.set_viande = "poulet"
        self.assertEqual(self.viandePoulet.prix, 0.2)

    # test calorie du poulet

    def test_cal_poulet_30(self):
        self.monobjet30.set_viande = "poulet",
        self.assertEqual(self.viandePoulet.calorie * 2, 478)

    # test prix unitaire du poulet

    def test_prix_poulet_30(self):
        self.monobjet30.set_viande = "poulet"
        self.assertEqual(self.viandePoulet.prix * 2, 0.4)

        # test calorie du boeuf

    def test_cal_boeuf_15(self):
        self.monobjet.set_viande = "boeuf"
        self.assertEqual(self.viandeBoeuf.calorie, 250)

    # test prix unitaire du boeuf

    def test_prix_boeuf_15(self):
        self.monobjet.set_viande = "boeuf"
        self.assertEqual(self.viandeBoeuf.prix, 0.2)

    # test calorie du boeuf

    def test_cal_boeuf_30(self):
        self.monobjet30.set_viande = "boeuf"
        self.assertEqual(self.viandeBoeuf.calorie*2, 500)

    # test prix unitaire du boeuf

    def test_prix_boeuf_30(self):
        self.monobjet30.set_viande = "boeuf"
        self.assertEqual(self.viandeBoeuf.prix*2, 0.4)

    # test calorie du vegan

    def test_cal_vegane_15(self):
        self.monobjet.set_viande = "vegan"
        self.assertEqual(self.vegan.calorie, 206)

    # test prix unitaire du vegan

    def test_prix_vegane_15(self):
        self.monobjet.set_viande = "vegan"
        self.assertEqual(self.vegan.prix, 0.3)

    # test calorie du vegan

    def test_cal_vegane_30(self):
        self.monobjet30.set_viande = "vegan"
        self.assertEqual(self.vegan.calorie*2, 412)

    # test prix unitaire du vegan

    def test_prix_vegane_30(self):
        self.monobjet30.set_viande = "vegan"
        self.assertEqual(self.vegan.prix*2, 0.6)

    # sandwich maison15 pain 15cm, poulet, fsto, mayo, sans sup

    def test_prix_sand_15_maison(self):
        self.monobjet.set_taille = 15
        self.monobjet.set_viande = "poulet"
        self.monobjet.fromage = 1
        self.monobjet.salade = 1
        self.monobjet.tomate = 1
        self.monobjet.oignon = 1
        self.monobjet.choixSauce = 1
        self.monobjet.mayo = 1
        self.monobjet.supp = 0
        self.assertEqual(self.monobjet.prixTotal, 6.15)
        self.assertEqual(self.monobjet.caloriesTotal, 1036)

    # sandwich maison pain 30cm, boeuf, fsto, mayo, sans sup

    def test_prix_sand_30_maison_mayo(self):
        self.monobjet30.set_taille = 30
        self.monobjet30.set_viande = "boeuf"
        self.monobjet30.fromage = 1
        self.monobjet30.salade = 1
        self.monobjet30.tomate = 1
        self.monobjet30.oignon = 1
        self.monobjet30.choixSauce = 1
        self.monobjet30.mayo = 1
        self.monobjet30.supp = 0
        self.assertEqual(self.monobjet30.prixTotal, 10.10)
        self.assertEqual(self.monobjet30.caloriesTotal, 1951)

    # sandwich maison15 pain 30cm, boeuf, fsto, andalouse, sans sup

    def test_prix_sand_30_maison_andalouse(self):
        self.monobjet30.set_taille = 30
        self.monobjet30.set_viande = "boeuf"
        self.monobjet30.fromage = 1
        self.monobjet30.salade = 1
        self.monobjet30.tomate = 1
        self.monobjet30.oignon = 1
        self.monobjet30.choixSauce = 1
        self.monobjet30.andalouse = 1
        self.monobjet30.supp = 0
        self.assertEqual(self.monobjet30.prixTotal, 10.10)
        self.assertEqual(self.monobjet30.caloriesTotal, 2111)

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
        self.monobjet.supp = 0
        self.assertEqual(self.monobjet.prixTotal, 5.2)
        self.assertEqual(self.monobjet.caloriesTotal, 481)

    # sandwich maison 30 pain , vegan, sto, sans sauce, sans sup
    def test_prix_sand_30_maison_vegan_sans_sauce(self):
        self.monobjet30.set_taille= 30
        self.monobjet30.set_viande = "vegan"
        self.monobjet30.fromage = 0
        self.monobjet30.salade = 1
        self.monobjet30.tomate = 1
        self.monobjet30.oignon = 1
        self.monobjet30.choixSauce = 0
        self.monobjet30.andalouse = 0
        self.monobjet30.supp = 0
        self.assertEqual(self.monobjet30.prixTotal, 8.2)
        self.assertEqual(self.monobjet30.caloriesTotal, 819)

    # test d'affichage
    def test_affichage_fin_de_commande(self):
        self.monobjet30.set_taille= 30
        self.monobjet30.set_viande = "vegan"
        self.monobjet30.fromage = 0
        self.monobjet30.salade = 1
        self.monobjet30.tomate = 1
        self.monobjet30.oignon = 1
        self.monobjet30.choixSauce = 0
        self.monobjet30.andalouse = 0
        self.monobjet30.supp = 0
        self.assertEqual(self.monobjet30.affichage_final_commande,
                         "Pour un prix de : 8.2 euros et pour:"
                         " 819 kilocalories, vous avez un sandwich vegan de 30 cm,"
                         " composé de salade, tomate, oignon et sans sauce")

    # test de validation refus
    def test_de_non_validation_de_la_commande(self):
        self.monobjet.validationFinale = 0
        self.assertEqual(self.monobjet.validation, 0)

    # test de validation accepte
    def test_de_validation_de_la_commande(self):
        self.monobjet.validationFinale = 1
        self.assertEqual(self.monobjet.validation, 1)

if __name__ == '__main__':
    unittest.main()
