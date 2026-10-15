import unittest
from app import add_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 5), 10)

    if __name__ == '__main__':
        unittest.main()