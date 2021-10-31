import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_substract_correctly(self):
        assert self.calc.substraction(self,5,3) == 2

    def test_add_correctly(self):
        assert self.calc.adding(self,5,3) == 8

    def test_divide_correctly(self):
        assert self.calc.division(self,10,5) == 2
