import unittest
from app.calculator import Calculator

class TestCalculatorDivide(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_divide_method(self):
        result = self.calc.divide(10,3)
        self.assertEqual(3.3333333333333335, result)

    def test_calculator_returns_error_when_both_arguments_not_a_number(self):
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')

    def test_calculator_returns_error_when_x_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.divide, 'two', 3)

    def test_calculator_returns_error_when_y_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.divide, 2, 'three')



if __name__ == '__main__':
    unittest.main()
