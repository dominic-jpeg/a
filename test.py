import unittest

# Function to test
def is_odd(n):
    return n % 2 != 0

class TestIsOdd(unittest.TestCase):

    def test_odd_num(self):
        self.assertTrue(is_odd(3))  # Testing an odd number

    def test_even_num(self):
        self.assertFalse(is_odd(4))  # Testing an even number

    def test_zero(self):
        self.assertFalse(is_odd(0))  # Testing zero as an edge case

if __name__ == '__main__':
    unittest.main()
