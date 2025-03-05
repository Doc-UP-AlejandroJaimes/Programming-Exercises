import unittest
from lucky_list import has_lucky_number  # Asegúrate de que el archivo se llame has_lucky_number.py

class TestHasLuckyNumber(unittest.TestCase):
    def test_contains_lucky_number(self):
        self.assertTrue(has_lucky_number([1, 2, 7, 10]))

    def test_no_lucky_number(self):
        self.assertFalse(has_lucky_number([1, 2, 3, 5, 6]))

    def test_multiple_lucky_numbers(self):
        self.assertTrue(has_lucky_number([14, 21, 28, 35]))

    def test_empty_list(self):
        self.assertFalse(has_lucky_number([]))

    def test_negative_lucky_number(self):
        self.assertTrue(has_lucky_number([-7, 1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
