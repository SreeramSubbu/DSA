import array
class Solution:
    def twoSum(nums: array[int], target: int) -> bool:
        left = 0
        right =  len(nums) - 1

        while left < right :
            sum = nums[left]+ nums[right]
            if sum == target : 
                return True
            elif sum > target :
                right -= 1
            else:
                left += 1
        return False

import unittest

class TestSolution(unittest.TestCase):

    def test_sample_array(self):
       vals = [1,3,4,6,8,10,13]
       result = Solution.twoSum(vals,13)
       self.assertEqual(result,True)

    def sample_array2(self):
        vals = [2,7,11,15]
        result = Solution.twoSum(vals,18)
        self.assertEqual(result,True)

    def sample_array3(self):
      vals = [1,2,3,4,5]
      result = Solution.twoSum(vals,10)
      self.assertEqual(result,False) 

if __name__ == '__main__':
 unittest.main()