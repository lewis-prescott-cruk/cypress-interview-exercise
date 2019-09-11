import unittest

from fractions import Fraction
from exercise import sum


class Test(unittest.TestCase):
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions.
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))
