# Дан двумерный целочисленный массив nums, где nums[i] — непустой массив различных положительных целых чисел. 
# Верните список целых чисел, присутствующих в каждом массиве nums, отсортированный в порядке возрастания.
from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = nums[0]
        for i in (nums):
            result = set(result) & set(i)
        result = list(result)
        result.sort()

        return result

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
example = Solution()
result1 = example.intersection(nums)
# Единственными целыми числами, присутствующими в каждом из nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4] и nums[2] = [3,4,5,6], 
# являются 3 и 4, поэтому мы возвращаем [3,4].
assert result1 == [3,4]
print(result1)

nums = [[1,2,3],[4,5,6]]
result2 = example.intersection(nums)
assert result1 == []
print(result2)

nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
result3 = example.intersection(nums)
assert result3 == [10,12,13,27,45]
print(result3)