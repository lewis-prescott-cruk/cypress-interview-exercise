import unittest
import re

from exercise import longestPalindrome


class Test(unittest.TestCase):
    @unittest.skip("skipping this test until we're ready to implement it")
    def test_long_palindrome(self):
        """
        Test that it can find the longest palindrome in a long-ish string.
        """
        with open('tests/long-ish.txt', 'r') as f:
            string = f.read()
        string = re.sub("[^a-z]", "", str.lower(string))
        result = longestPalindrome(string)
        self.assertEqual(result, 27)

    @unittest.skip("skipping this test until we're ready to implement it")
    def test_very_long_string(self):
        """
        Tests that the performance is adequate for a ~12 thousand character
        string.
        """
        with open('tests/long.txt', 'r') as f:
            string = f.read()
        string = re.sub("[^a-z]", "", str.lower(string))
        result = longestPalindrome(string)
        self.assertEqual(result, 1)
