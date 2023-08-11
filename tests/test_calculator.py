from src.calculator import Calculator


class Test_Calculator:

    def test_add(self):
        result = Calculator.add(2, 3)
        assert result == 5
    
    def test_add2(self):
        result = Calculator.add(2, -3)
        assert result == -1