import unittest

from Calculator.calculator218 import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_return_multiplication(self):
        result = self.calculator.Multiplication(1, 2)
        self.assertEqual(2, result)

    def test_calculator_access_multiplication_result(self):
        self.calculator.Multiplication(1, 2)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_return_division(self):
        result = self.calculator.Division(4, 2)
        self.assertEqual(2, result)

    def test_calculator_access_division_result(self):
        self.calculator.Division(4, 2)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_return_exponent(self):
        result = self.calculator.Exponent(4, 2)
        self.assertEqual(16.0, result)

    def test_calculator_access_exponent_result(self):
        self.calculator.Exponent(4, 2)
        self.assertEqual(16.0, self.calculator.Result)

    def test_calculator_return_logarithm(self):
        result = self.calculator.Logarithm(1, 2)
        self.assertEqual(0.0, result)

    def test_calculator_access_logarithm_result(self):
        self.calculator.Logarithm(1, 2)
        self.assertEqual(0.0, self.calculator.Result)

    def test_calculator_return_squareRoot(self):
        result = self.calculator.SquareRoot(9)
        self.assertEqual(3, result)

    def test_calculator_access_squareRoot_result(self):
        self.calculator.SquareRoot(9)
        self.assertEqual(3, self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()