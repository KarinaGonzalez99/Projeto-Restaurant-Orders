from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    # Teste de criação e propriedades do prato "Prato1"
    testdishs = Dish("Prato1", 10.0)
    assert testdishs.name == "Prato1"
    assert testdishs == Dish("Prato1", 10.0)
    # Teste de representação e hash do prato "Prato1"
    assert repr(testdishs) == "Dish('Prato1', R$10.00)"
    assert hash(testdishs) == hash("Dish('Prato1', R$10.00)")
    assert hash(testdishs) != hash("Dish('Prato1', R$20.00)")
    # Teste de TypeError ao criar um prato com preço inválido
    with pytest.raises(TypeError):Dish("Prato1", "10.0")
    # Teste de ValueError ao criar um prato com preço negativo
    with pytest.raises(ValueError):Dish("Prato1", -10.0)
    # Teste de adição de dependência de ingrediente ao prato "Prato1"
    ingredientPadrao = Ingredient("salmão")
    testdishs.add_ingredient_dependency(ingredientPadrao, 1)
    # Teste da receita do prato "Prato1" após adição da dependência
    assert testdishs.recipe == {ingredientPadrao: 1}
    # Teste para verificar os ingredientes do prato "Prato1"
    assert testdishs.get_ingredients() == {ingredientPadrao}
    # Teste para verificar as restrições do prato "Prato1"
    assert testdishs.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
    }
