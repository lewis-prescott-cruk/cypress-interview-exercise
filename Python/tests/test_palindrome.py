import unittest

from exercise import palindrome


class Test(unittest.TestCase):
    def test_palindrome(self):
        """
        Test that it can detect palindromicity.
        """
        string = "amanaplanacanalpanama"
        result = palindrome(string)
        self.assertEqual(result, True)
