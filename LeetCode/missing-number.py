# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0 
        
        for i in range(1, (len(nums)+1)):
            if i not in nums:
                missing = i
                break
        return missing
            

nums = [3,0,1]
example = Solution()
result1 = example.missingNumber(nums)
print("result1", result1)

nums = [0,1]
result2 = example.missingNumber(nums)
print("result2", result2)

nums = [9,6,4,2,3,5,7,0,1]
result3 = example.missingNumber(nums)
print("result2", result3)