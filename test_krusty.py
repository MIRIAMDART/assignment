import unittest
from krusty import get_gst

class TestRate(unittest.TestCase):

    def test_rate(self):
        self.assertRaises(ValueError, get_gst, -2)

if __name__ == '__main__':
    unittest.main()


