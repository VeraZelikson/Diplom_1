from praktikum.burger import Burger
from conftest import bun_mock
from conftest import filling_mock
from conftest import sauce_mock


class TestBurger:

    def test_empty_buns(self):
        burger = Burger()
        assert burger.bun is None

    def test_empty_ingredients(self):
        burger = Burger()
        assert len(burger.ingredients) == 0

    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.get_name() == 'testBun'

    def test_add_ingredient(self, filling_mock):
        burger = Burger()
        burger.add_ingredient(filling_mock)
        assert len(burger.ingredients) == 1

    def test_remove_single_ingredient(self, filling_mock):
        burger = Burger()
        burger.add_ingredient(filling_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_from_list(self, filling_mock):
        burger = Burger()
        burger.add_ingredient(filling_mock)
        burger.add_ingredient(filling_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self, filling_mock, sauce_mock):
        burger = Burger()
        burger.add_ingredient(filling_mock)
        burger.add_ingredient(sauce_mock)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [sauce_mock, filling_mock]

    def test_get_price(self, bun_mock, filling_mock, sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(filling_mock)
        burger.add_ingredient(sauce_mock)
        assert burger.get_price() == 20

    def test_get_receipt(self, bun_mock, filling_mock, sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(filling_mock)
        burger.add_ingredient(sauce_mock)

        expected_receipt = (f'(==== {bun_mock.get_name()} ====)\n'
                            f'= {filling_mock.get_type()} {filling_mock.get_name()} =\n'
                            f'= {sauce_mock.get_type()} {sauce_mock.get_name()} =\n'
                            f'(==== {bun_mock.get_name()} ====)\n\n'
                            f'Price: {burger.get_price()}')
        assert burger.get_receipt() == expected_receipt







