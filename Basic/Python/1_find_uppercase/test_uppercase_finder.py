import unittest
from uppercase_finder import find_uppercase

class TestFindUppercase(unittest.TestCase):
    def test_only_uppercase(self):
        self.assertEqual(find_uppercase("HELLO"), "HELLO")

    def test_mixed_case(self):
        self.assertEqual(find_uppercase("HelloWorld"), "HW")

    def test_no_uppercase(self):
        self.assertEqual(find_uppercase("hello world"), "")

    def test_numbers_and_symbols(self):
        self.assertEqual(find_uppercase("123@!ABC#xyz"), "ABC")

    def test_empty_string(self):
        self.assertEqual(find_uppercase(""), "")

if __name__ == '__main__':
    unittest.main()
