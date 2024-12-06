import unittest
from FibonacciGenerator import FibonacciGenerator

class TestFibonacciGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = FibonacciGenerator()

    def test_generate_sequence(self):
        self.assertEqual(self.generator.generate_sequence(0), [])
        self.assertEqual(self.generator.generate_sequence(1), [0])
        self.assertEqual(self.generator.generate_sequence(5), [0, 1, 1, 2, 3])

    def test_get_nth_number(self):
        self.assertIsNone(self.generator.get_nth_number(0))
        self.assertEqual(self.generator.get_nth_number(1), 0)
        self.assertEqual(self.generator.get_nth_number(7), 8)

if __name__ == '__main__':
    unittest.main()
