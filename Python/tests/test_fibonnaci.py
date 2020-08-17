from exercise import fibonacci
import unittest


class Test(unittest.TestCase):
    def test_returns_correct_fibonacci_number(self):
        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for index in range(len(correct_sequence)):
            response = fibonacci(index)
            assert response == correct_sequence[index]
