from praktikum.burger import Burger
from praktikum.burger import Ingredient
from conftest import bun_mock
from conftest import filing_mock
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
        assert burger.bun.get_name() == 'MockBun1'

    def test_add_ingredient(self, filing_mock):
        burger = Burger()
        burger.add_ingredient(filing_mock)
        assert len(burger.ingredients) == 1

    def test_remove_single_ingredient(self, filing_mock):
        burger = Burger()
        burger.add_ingredient(filing_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_from_list(self, filing_mock):
        burger = Burger()
        burger.add_ingredient(filing_mock)
        burger.add_ingredient(filing_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self, filing_mock, sauce_mock):
        burger = Burger()
        burger.add_ingredient(filing_mock)
        burger.add_ingredient(sauce_mock)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [sauce_mock, filing_mock]

    def test_get_price(self, bun_mock, filing_mock, sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(filing_mock)
        burger.add_ingredient(sauce_mock)

        bun_mock.get_price.return_value = 4
        filing_mock.get_price.return_value = 7
        sauce_mock.get_price.return_value = 5
        assert burger.get_price() == 20

    def test_get_receipt(self, bun_mock, filing_mock, sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(filing_mock)
        burger.add_ingredient(sauce_mock)

        bun_mock.get_price.return_value = 4
        filing_mock.get_price.return_value = 7
        sauce_mock.get_price.return_value = 5

        bun_mock.get_name.return_value = "testBun"
        filing_mock.get_name.return_value = 'testFiling'
        sauce_mock.get_name.return_value = 'testSauce'

        filing_mock.get_type.return_value = 'filling'
        sauce_mock.get_type.return_value = 'sauce'

        expected_receipt = (f'(==== {bun_mock.get_name()} ====)\n'
                            f'= {filing_mock.get_type()} {filing_mock.get_name()} =\n'
                            f'= {sauce_mock.get_type()} {sauce_mock.get_name()} =\n'
                            f'(==== {bun_mock.get_name()} ====)\n\n'
                            f'Price: {burger.get_price()}')
        print('\n' + expected_receipt)
        assert burger.get_receipt() == expected_receipt







