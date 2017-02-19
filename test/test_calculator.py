import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_when_both_arguments_not_a_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_calculator_returns_error_when_x_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_calculator_returns_error_when_y_arg_not_a_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')



if __name__ == '__main__':
    unittest.main()
