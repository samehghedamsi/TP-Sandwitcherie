
from src.Contents import Contents
from src.Sandwich import Sandwich
from src.Sauces import Sauces

# création des sandwiches
sandwich15 = Sandwich("Sandwich en 15 cm", 15, 198)
sandwich30 = Sandwich("Sandwich 30 cm", 30, 253)

# creation des sauces
mayonnaise = Sauces("Mayonnaise", 120)
ketchup = Sauces("Ketchup", 189)
blanche = Sauces("Blanche", 110)
andalouse = Sauces("Andalouse", 200)


# creation des viandes/vegan
poulet = Contents("Poulet", 239)
boeuf = Contents("Boeuf", 250)
vegan = Contents("Vegan", 206)
poisson = Contents("Poisson", 100)

print(55*"-")
print("-- Affichage du menu complet sous forme de listes de -- \n"
      "-- sandwiches, viandes/vegan et sauces sous formes   -- \n"
      "-- de nested dict                                    --")
print(55*"-")
sandwiches_list = {
        f"{sandwich15.name}": f"{sandwich15.kcal} kcal",
        f"{sandwich30.name}": f"{sandwich30.kcal} kcal",
    }
contents_list = {
        f"{poulet.name}": f"{poulet.kcal} kcal",
        f"{boeuf.name}": f"{boeuf.kcal} kcal",
        f"{vegan.name}": f"{vegan.kcal} kcal",
        f"{poisson.name}": f"{poisson.kcal} kcal"
    }
sauces_list = {
        f"{mayonnaise.name}": f"{mayonnaise.kcal} kcal",
        f"{ketchup.name}": f"{ketchup.kcal} kcal",
        f"{blanche.name}": f"{blanche.kcal} kcal",
        f"{andalouse.name}": f"{andalouse.kcal} kcal"
    }


def show_complete_menu():
    complete_menu = {
        "Les sandwiches": sandwiches_list,
        "L'accompagnement viande": contents_list,
        "Les sauces": sauces_list
    }
    return complete_menu


print(show_complete_menu())
print("")

print(43*"-")
print("-- Affichage des listes individuellement --")
print(43*"-")


def sandwiches_menu():
    sandwiches_list = {
        f"{sandwich15.name}": f"{sandwich15.kcal} kcal",
        f"{sandwich30.name}": f"{sandwich30.kcal} kcal",
    }
    for key, value in sandwiches_list.items():
        print(f"{key} : {value}")


def contents_menu():
    contents_list = {
        f"{poulet.name}": f"{poulet.kcal}",
        f"{boeuf.name}": f"{boeuf.kcal}",
        f"{vegan.name}": f"{vegan.kcal}",
        f"{poisson.name}": f"{poisson.kcal}"
    }
    for key, value in contents_list.items():
        print(f"{key} : {value} kcal")


def sauces_menu():
    sauces_list = {
        f"{mayonnaise.name}": f"{mayonnaise.kcal}",
        f"{ketchup.name}": f"{ketchup.kcal}",
        f"{blanche.name}": f"{blanche.kcal}",
        f"{andalouse.name}": f"{andalouse.kcal}"
    }
    for key, value in sauces_list.items():
        print(f"{key} : {value} kcal")


# ESSAYER GLOBAL DANS DEF
sandwiches_menu()
print(43*"-")
sauces_menu()
print(43*"-")
contents_menu()
