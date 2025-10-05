"""
You’re given a SimpleCalculator class within
simple_calculator.py with basic arithmetic operations.
Your task is to write unit tests to verify its correctness.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestAdd(unittest.TestCase):

  def setUp(self):
    """Set up the SimpleCalculator instance before each test."""
    self.calc = SimpleCalculator()

  def test_addition(self):
    result = self.calc.add(7,3)
    self.assertEqual(result, 10)

  def test_subtraction(self):
    result = self.calc.subtract(7, 3)
    self.assertEqual(result, 4)

  def test_multiplication(self):
    result = self.calc.multiply(7, 3)
    self.assertEqual(result, 21)

  def test_division(self):
    result = self.calc.divide(10, 5)
    self.assertEqual(result, 2)

  def test_division_by_zero(self):
    result = self.calc.divide(10, 0)
    self.assertIsNone(result)


if __name__ == "__main__":
  unittest.main()