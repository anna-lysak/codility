from BinaryGap import binary_gap
import unittest


class BinaryGapTest(unittest.TestCase):
    def test_BinaryGap(self):
        self.assertEqual(binary_gap(0), 0)
        self.assertEqual(binary_gap(529), 4)
        self.assertEqual(binary_gap(9), 2)
        self.assertEqual(binary_gap(20), 1)


if __name__ == '__main__':
    unittest.main()