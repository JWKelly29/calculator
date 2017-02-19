import unittest
from app.calculator import Calculator

class TestCalculatorSubtract(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_subtract_method(self):
        result = self.calc.subtract(2,2)
        self.assertEqual(0, result)

    def test_calculator_returns_error_when_both_arguments_not_a_number(self):
        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')

    def test_calculator_returns_error_when_x_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.subtract, 'two', 3)

    def test_calculator_returns_error_when_y_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.subtract, 2, 'three')



if __name__ == '__main__':
    unittest.main()
