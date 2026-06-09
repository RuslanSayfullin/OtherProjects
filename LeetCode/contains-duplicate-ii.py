# Дан массив целых чисел nums и целое число k. 
# Верните true, если в массиве есть два различных индекса i и j таких, что nums[i] == nums[j] и abs(i - j) <= k.
from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        flag: bool = False
        result: dict = Counter(nums)
        indices: list = []

        for key, value in result.items():
            if value != 1:
                indices = [i for i, value in enumerate(nums) if value == key]   # получил индексы одинаковых щначений

        for i in range(len(indices)):
            for j in range((i+1), len(indices)):

                if (abs(indices[i] - indices[j]) <= k):
                    flag = True

        return flag


nums = [1,2,3,1]
k = 3
example = Solution()
result1 = example.containsNearbyDuplicate(nums, k)
#assert result1
print( "result1", result1)

nums = [1,0,1,1]
k = 1
example = Solution()
result2 = example.containsNearbyDuplicate(nums, k)
#assert result2
print( "result2", result2)

nums = [1,2,3,1,2,3]
k = 2
example = Solution()
result3 = example.containsNearbyDuplicate(nums, k)
#assert result3
print( "result3", result3)
