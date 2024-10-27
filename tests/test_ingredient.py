from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient('sauce', 'TestIngredient', 4)
        assert ingredient.get_name() == 'TestIngredient'

    def test_get_price(self):
        ingredient = Ingredient('sauce', 'TestIngredient', 8.6)
        assert ingredient.get_price() == 8.6

    def test_get_type(self):
        ingredient = Ingredient('filling', 'TestIngredient', 5.8)
        assert ingredient.get_type() == 'filling'
