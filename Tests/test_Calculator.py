import unittest
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Logarithm import logarithm
from Calculator.SquareRoot import squareRoot
from Calculator.Exponentiation import exponentiation
from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        self.assertEqual(6,addition(3,3))

    def test_subtraction(self):
        self.assertEqual(9,subtraction(18,9))

    def test_multiplication(self):
        self.assertEqual(6,multiplication(3,3))

    def test_division(self):
        self.assertEqual(3,division(9,3))

    def test_logarithm(self):
        self.assertEqual(6,logarithm(64,2))

    def test_exponentiation(self):
        self.assertEqual(9,exponentiation(3,2))

    def test_squareRoot(self):
        self.assertEqual(9,squareRoot(81))


if __name__ == '__main__':
    unittest.main()