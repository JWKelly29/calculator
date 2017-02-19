import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method(self):
        result = calc.add(2,2)
        self.assertEqual(4, result)



if __name__ == '__main__':
    unittest.main()
