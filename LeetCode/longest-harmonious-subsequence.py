# Гармоничный массив определяется как массив, в котором разница между его максимальным и минимальным значениями равна 1.
# Дано целочисленное множество nums, верните длину его самой длинной гармоничной подпоследовательности среди всех возможных подпоследовательностей.
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        find_lhs: int = 0

        

        return find_lhs
    
example = Solution()

nums = [1,3,2,2,5,2,3,7]
result1 = example.findLHS(nums)
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
assert result1 == 5
print( "result1", result1)

nums = [1,2,3,4]
result2 = example.findLHS(nums)
# Explanation: The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.
assert result2 == 2
print( "result2", result2)

nums = [1,1,1,1]
result3 = example.findLHS(nums)
# Explanation: No harmonic subsequence exists.
assert result3 == 0
print( "result3", result3)