import unittest
import array

# Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle.

# For three sides to form a valid triangle,
# all three of these conditions must hold: (a + b > c), (a + c > b), and (b + c > a),
# where (a), (b), and (c) are the side lengths. In other words,
# the sum of every possible pair must exceed the third side.


# Time complexity O(n^2) + sort O(n log n)
# Space complexity O(1)


class Solution:
    def triangle_numbers(nums: array):
        nums.sort()
        count = 0
        for i in range(len(nums)-1, 1, -1):
            left = 0
            right = i-1
            while left < right:
                if (nums[left]+nums[right] > nums[i]):
                    # Every number between left and right forms a valid triangle with numbers at right and i
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count


class TestSolution(unittest.TestCase):

    def test_array_1(self):
        vals = [11, 4, 9, 6, 15, 18]
        count = Solution.triangle_numbers(vals)
        self.assertEqual(count, 10)

    def test_array_2(self):
        vals = [1, 1, 2]
        count = Solution.triangle_numbers(vals)
        self.assertEqual(count, 0)

    def test_array_3(self):
        vals = [2, 3, 4]
        count = Solution.triangle_numbers(vals)
        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
