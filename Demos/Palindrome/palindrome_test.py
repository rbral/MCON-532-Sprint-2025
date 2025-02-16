import unittest
from palindrome import is_palindrome

class MyTestCase(unittest.TestCase):
    def test_sentence(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    def test_racecar(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_case(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_char(self):
        self.assertTrue(is_palindrome("race!car@"))

    def test_hello(self):
        self.assertFalse(is_palindrome("hello"))


if __name__ == '__main__':
    unittest.main()
