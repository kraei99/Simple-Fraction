'''
    CS 5001, 
    Fall 2023
    HW7 - TestSimpleFraction
    Kayser Raei
'''

import unittest
from SimpleFraction import SimpleFraction

class TestSimpleFraction(unittest.TestCase):

    def test_init(self):
        # Test proper initialization
        fraction = SimpleFraction(3, 4)
        self.assertEqual(fraction.get_numerator(), 3)
        self.assertEqual(fraction.get_denominator(), 4)

        # Test default initialization
        default_fraction = SimpleFraction()
        self.assertEqual(default_fraction.get_numerator(), 1)
        self.assertEqual(default_fraction.get_denominator(), 1)

        # Test initialization with zero denominator
        with self.assertRaises(ValueError):
            SimpleFraction(3, 0)

        # Test initialization with non-integer numerator
        with self.assertRaises(ValueError):
            SimpleFraction(3.5, 2)

    def test_str(self):
        # Test string representation
        fraction = SimpleFraction(3, 4)
        self.assertEqual(str(fraction), "3/4")

    def test_eq(self):
        # Test equality comparison
        fraction1 = SimpleFraction(3, 4)
        fraction2 = SimpleFraction(6, 8)
        self.assertTrue(fraction1 == fraction2)

        # Test inequality
        fraction3 = SimpleFraction(2, 3)
        self.assertFalse(fraction1 == fraction3)

    def test_reciprocal(self):
        # Test reciprocal creation
        fraction = SimpleFraction(3, 4)
        reciprocal = fraction.make_reciprocal()
        self.assertEqual(reciprocal.get_numerator(), 4)
        self.assertEqual(reciprocal.get_denominator(), 3)

    def test_multiply(self):
        # Test multiplication with SimpleFraction
        fraction1 = SimpleFraction(3, 4)
        fraction2 = SimpleFraction(2, 3)
        product = fraction1.multiply(fraction2)
        self.assertEqual(product.get_numerator(), 3*2)
        self.assertEqual(product.get_denominator(), 4*3)

        # Test multiplication with an integer
        product_with_int = fraction1.multiply(2)
        self.assertEqual(product_with_int.get_numerator(), 3*2)
        self.assertEqual(product_with_int.get_denominator(), 4)

    def test_divide(self):
        # Test division with SimpleFraction
        fraction1 = SimpleFraction(3, 4)
        fraction2 = SimpleFraction(2, 3)
        quotient = fraction1.divide(fraction2)
        self.assertEqual(quotient.get_numerator(), 3*3)
        self.assertEqual(quotient.get_denominator(), 4*2)

        # Test division with an integer
        quotient_with_int = fraction1.divide(2)
        self.assertEqual(quotient_with_int.get_numerator(), 3)
        self.assertEqual(quotient_with_int.get_denominator(), 4*2)

if __name__ == '__main__':
    unittest.main()
