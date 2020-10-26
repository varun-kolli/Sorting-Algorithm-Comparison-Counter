import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_sel(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_sel_01(self):
        nums = [0]*1000
        comps = selection_sort(nums)
        self.assertEqual(comps, 499500)
        self.assertEqual(nums, [0]*1000)

    def test_ins(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])


if __name__ == '__main__': 
    unittest.main()
