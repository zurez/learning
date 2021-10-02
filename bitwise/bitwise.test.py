
import unittest
from bitwise import multiply_by_power2


class BitwiseTestCase(unittest.TestCase):
    def test_multiply_by_power2(self):

        self.assertEqual(multiply_by_power2(5, 0), 5)
        self.assertEqual(multiply_by_power2(5, 1), 10)
        self.assertEqual(multiply_by_power2(5, 3), 40)


if __name__ == "__main__":
    unittest.main()
