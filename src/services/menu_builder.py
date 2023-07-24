from typing import Dict, List
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from src.models.ingredient import restriction_map

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction: restriction_map = None) -> List[Dict]:
        result = []
        for dish in self.menu_data.dishes:
            # Verifica se não há restrição não está presente prato
            if (
                restriction is None
                or restriction not in dish.get_restrictions()
            ):
                dish_info = {
                    "dish_name": dish.name,
                    "ingredients": list(dish.recipe.keys()),
                    "price": dish.price,
                    "restrictions": dish.get_restrictions(),
                }
                result.append(dish_info)
        return result

        # Monta o dicionário e adiciona na lista de resultadoo
