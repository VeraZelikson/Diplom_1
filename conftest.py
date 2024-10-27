from unittest.mock import Mock
from praktikum.bun import Bun
import pytest

from praktikum.ingredient import Ingredient


@pytest.fixture
def bun_mock():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_price.return_value = 4
    bun_mock.get_name.return_value = 'testBun'
    return bun_mock


@pytest.fixture
def filling_mock():
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_price.return_value = 7
    ingredient_mock.get_name.return_value = 'testFilling'
    ingredient_mock.get_type.return_value = 'filling'
    return ingredient_mock


@pytest.fixture
def sauce_mock():
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_price.return_value = 5
    ingredient_mock.get_name.return_value = 'testSauce'
    ingredient_mock.get_type.return_value = 'sauce'
    return ingredient_mock
