import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test Addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)

    # Test Subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -2), 0)
        self.assertEqual(self.calc.subtract(3.5, 1.2), 2.3)

    # Test Multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 999), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # Test Division
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)  # Handles float results

    # Test Division by Zero
    def test_division_by_zero(self):
        self.assertEqual(self.calc.divide(10, 0), "Error: Cannot divide by zero.")

if __name__ == "__main__":
    unittest.main()
