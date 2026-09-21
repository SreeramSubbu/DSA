
import unittest


class Solution:
    def three_sum(nums: list):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


class TestSolution(unittest.TestCase):

    def test_array_1(self):
        vals = [-1, 0, 1, 2, -1, -1]
        result = Solution.three_sum(vals)
        self.assertEqual(result, [[-1, -1, 2], [-1, 0, 1]])

    def test_array_2(self):
        vals = [0, 0, 0, 0]
        result = Solution.three_sum(vals)
        self.assertEqual(result, [[0, 0, 0]])

    def test_array_2(self):
        vals = [1, 2, -2, -1]
        result = Solution.three_sum(vals)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
