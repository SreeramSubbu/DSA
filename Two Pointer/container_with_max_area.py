"""
Container With Most Water
Given an array heights where each element represents the height of a vertical line, 
pick two lines to act as the walls of a container.
Return the maximum area (amount of water) the container can hold.

What is area? Width × height, where width is the distance between walls,
and height is the shorter wall (water overflows at the shorter wall).
"""
import unittest


class Solution:
    def max_area(heights):
        left, right = 0, len(heights)-1
        current_max = 0

        while (left < right):
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height

            current_max = max(current_max, current_area)
            if (heights[left] < heights[right]):
                left = left + 1
            else:
                right = right - 1
        return current_max


class TestSolution(unittest.TestCase):

    def test_sample_array(self):
        vals = [3, 4, 1, 2, 2, 4, 1, 3, 2]
        max = Solution.max_area(vals)
        self.assertEqual(max, 21)

    def test_short_array(self):
        vals = [1, 2, 1]
        max = Solution.max_area(vals)
        self.assertEqual(max, 2)

    def test_wide_array(self):
        vals = [2, 3, 4, 5, 1, 4, 6, 3, 2]
        max = Solution.max_area(vals)
        self.assertEqual(max, 18)


if __name__ == '__main__':
    unittest.main()
