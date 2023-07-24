import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.source_path = source_path
        self._load_menu_data()

    def _load_menu_data(self):
        with open(self.source_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                dname, dprice, iname, iqnt = row
                dish = self._get_dish(dname, float(dprice))
                ingredient = self._get_ingredient(iname)
                dish.add_ingredient_dependency(ingredient, int(iqnt))

    def _get_dish(self, name, price):
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish
        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish

    def _get_ingredient(self, name):
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient
        new_ingredient = Ingredient(name)
        self.ingredients.add(new_ingredient)
        return new_ingredient

    # Req 3.4
    def test_menu_data_dish_recipe(self):
        expected_dishes = {
            "Lasanha": {"Molho Bolonhesa": 2, "Molho Branco": 1},
            "Feijoada": {"Feijão Preto": 3, "Linguiça": 2},
            "Strogonoff": {"Carne": 1, "Molho de Tomate": 1},
            "Pizza de Calabresa": {"Massa": 1, "Calabresa": 1},
            "Arroz com Camarão": {"Arroz": 1, "Camarão": 2},
            "Feijão Tropeiro": {"Feijão": 2, "Linguiça": 1},
        }

        for dish in self.dishes:
            if dish.name in expected_dishes:
                expected_recipe = expected_dishes[dish.name]
                assert len(dish.recipe) == len(expected_recipe)

        for ingredient, quantity in expected_recipe.items():
            assert ingredient in dish.recipe
            assert dish.recipe[ingredient] == quantity
