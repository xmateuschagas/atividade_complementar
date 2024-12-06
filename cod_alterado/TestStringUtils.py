import unittest
from StringUtils import StringUtils

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    def test_reverse_string(self):
        self.assertEqual(self.utils.reverse_string("abc"), "cba")
        self.assertEqual(self.utils.reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(self.utils.is_palindrome("radar"))
        self.assertFalse(self.utils.is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
