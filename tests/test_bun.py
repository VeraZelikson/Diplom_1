from praktikum.bun import Bun


class TestBun:
    def test_get_name(self):
        bun = Bun('TestBun', 1)
        assert bun.get_name() == 'TestBun'

    def test_get_price(self):
        bun = Bun('TestBun', 2.7)
        assert bun.get_price() == 2.7
