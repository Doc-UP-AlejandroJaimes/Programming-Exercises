import unittest
from count_negatives import count_negatives 

class TestCountNegatives(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(count_negatives([1, -2, 3, -4, 5]), 2)

    def test_all_negatives(self):
        self.assertEqual(count_negatives([-1, -2, -3, -4]), 4)

    def test_all_positives(self):
        self.assertEqual(count_negatives([1, 2, 3, 4]), 0)

    def test_including_zero(self):
        self.assertEqual(count_negatives([0, -1, -2, 3, 4]), 2)

    def test_empty_list(self):
        self.assertEqual(count_negatives([]), 0)

if __name__ == '__main__':
    unittest.main()
