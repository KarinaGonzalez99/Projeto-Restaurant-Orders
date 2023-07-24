# tests/ingredient/test_ingredient.py
from src.models.ingredient import Ingredient, restriction_map


# Req 1
def test_ingredient():
    # Teste do ingrediente "queijo"
    ingone = Ingredient("queijo")
    # Verificar se o nome do ingrediente está correto
    assert ingone.name == "queijo"
    # Verificar a igualdade entre dois ingredientes "queijo"
    assert ingone == Ingredient("queijo")
    # Verificar o hash do ingrediente "queijo"
    assert hash(ingone) == hash("queijo")
    # Verificar a representação do ingrediente em string
    assert repr(ingone) == "Ingredient('queijo')"
    # Verificar as restrições do ingrediente "queijo"
    expected_restrictions = restriction_map().get("queijo", set())
    assert ingone.restrictions == expected_restrictions
