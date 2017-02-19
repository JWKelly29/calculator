import unittest
from app.calculator import Calculator

class TestCalculatorMultiply(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_multiply_method(self):
        result = self.calc.multiply(3,3)
        self.assertEqual(9, result)

    def test_calculator_returns_error_when_both_arguments_not_a_number(self):
        self.assertRaises(ValueError, self.calc.multiply, 'two', 'three')

    def test_calculator_returns_error_when_x_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.multiply, 'two', 3)

    def test_calculator_returns_error_when_y_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.multiply, 2, 'three')



if __name__ == '__main__':
    unittest.main()
