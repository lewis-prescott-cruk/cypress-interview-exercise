import unittest

from exercise import sum

class Test(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers.
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
