import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a SimpleCalculator instance for all tests."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtraction(5, 3), 2)
        self.assertEqual(self.calc.subtraction(3, 5), -2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiplication(2, 3), 6)
        self.assertEqual(self.calc.multiplication(-1, 5), -5)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.division(6, 3), 2)
        self.assertEqual(self.calc.division(5, 2), 2.5)

    def test_division_by_zero(self):
        """Test division by zero."""
        self.assertIsNone(self.calc.division(5, 0))
        
if __name__ == '__main__':
    unittest.main()