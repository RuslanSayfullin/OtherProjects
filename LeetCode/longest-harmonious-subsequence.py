# Гармоничный массив определяется как массив, в котором разница между его максимальным и минимальным значениями равна 1.
# Дано целочисленное множество nums, верните длину его самой длинной гармоничной подпоследовательности среди всех возможных подпоследовательностей.
from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 0
        
        for x in count:
            if x + 1 in count:
                current_len = count[x] + count[x + 1]
                max_len = max(max_len, current_len)
        
        return max_len


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