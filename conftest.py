from unittest.mock import Mock
from praktikum.bun import Bun
import pytest

from praktikum.ingredient import Ingredient


@pytest.fixture
def bun_mock():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = 'MockBun1'
    return bun_mock

@pytest.fixture
def filing_mock():
    ingredient_mock = Mock(spec=Ingredient)
    # ingredient_mock.get_name.return_value = 'MockIngredient1'
    return ingredient_mock

@pytest.fixture
def sauce_mock():
    ingredient_mock = Mock(spec=Ingredient)
    # ingredient_mock.get_name.return_value = 'MockIngredient1'
    return ingredient_mock








