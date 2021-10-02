import unittest
from test_demo import test


class TestDemoTest(unittest.TestCase):
    def test_atest_demo(self):
        self.assertEqual(test(), "test")


if __name__ == "__main__":
    unittest.main()
