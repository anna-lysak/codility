from algorithms import minmax, sum_squares, pow_list, product_distinct_pairs, distinct_numbers, progression, \
    IndexOutOfBounds, replace_by_index, factors, unique, palindrome, palindrome_rec
import unittest


class AlgorithmsTest(unittest.TestCase):

    def almostEqual(self, list1, list2, n=7):
        l = len(list1)
        self.assertEqual(l, len(list2))

        for i in range(0, l):
            self.assertAlmostEqual(list1[i], list2[i], places=n)

    def test_minmax(self):
        self.assertEqual(minmax([2,3,4,5]), (2, 5))
        self.assertEqual(minmax([-5, -3, -6, 2, 5, 4]), (-6, 5))
        self.assertEqual(minmax({0.3, 0.4, 0.2}), (0.2, 0.4))
        # self.assertEqual(minmax(9), 2)
        # self.assertEqual(minmax(20), 1)

    def test_sum_squares(self):
        self.assertEqual(sum_squares(8), 84)  # 1+9+25+49
        self.assertEqual(sum_squares(4), 10)
        self.assertEqual(sum_squares(0), 0)
        self.assertEqual(sum_squares(-1), 0)

    def test_pow_list(self):
        self.assertEqual(pow_list(2, 8), [2, 4, 8, 16, 32, 64, 128, 256])
        self.assertEqual(pow_list(3, 2), [3, 9])
        self.assertEqual(pow_list(1, 2), [1, 1])
        self.almostEqual(pow_list(2, -3), [0.5, 0.25, 0.125], 3)

    def test_product_distinct_pairs(self):
        self.assertEqual(product_distinct_pairs([1, 3, 2, 4, 5, 8, 9]), [(1, 3), (5, 9)])
        self.assertEqual(product_distinct_pairs([1, 1, 1, 1, 1]), [(1, 1)])
        self.assertEqual(product_distinct_pairs([2, 2, 2, 2, 1]), [])


    def test_distinct_numbers(self):
        self.assertEqual(distinct_numbers([1, 2, 1, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(distinct_numbers([1, 1, 1]), [1])
        self.assertEqual(distinct_numbers([1, 4, 3]), [1, 4, 3])


    def test_progression(self):
        self.assertEqual(progression(), [0, 2, 6, 12, 20, 30, 42, 56, 72, 90])

    def test_replace_by_index(self):
        self.assertRaises(IndexOutOfBounds, replace_by_index, [1, 2, 3], 4, 5)
        self.assertEqual(replace_by_index([1, 2], 0, 3), [3, 2])

    def test_factors(self):
        self.assertEqual([i for i in factors(10)], [1, 10, 2, 5])

    def test_unique(self):
        self.assertTrue(unique([1, 2, 3, 4, 5]))
        self.assertFalse(unique([1, 2, 3, 2, 5]))

    def test_palindrome(self):
        self.assertTrue(palindrome("asdfdsa"))
        self.assertTrue(palindrome_rec("asdfdsa"))
        self.assertFalse(palindrome("asdfds"))
        self.assertFalse(palindrome_rec("asdfds"))
        self.assertTrue(palindrome("a"))
        self.assertTrue(palindrome_rec("a"))




if __name__ == '__main__':
    unittest.main()