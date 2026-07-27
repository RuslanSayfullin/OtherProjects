# Дан массив целых чисел nums, отсортированный в порядке возрастания, и целое число target. 
# Напишите функцию для поиска target в массиве nums. Если target существует, верните его индекс. В противном случае верните -1.
# Необходимо написать алгоритм со сложностью O(log n).
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid  = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

example = Solution()

nums = [-1,0,3,5,9,12]
target = 9
result1 = example.search(nums, target)
assert result1 == 4
print(result1)

nums = [-1,0,3,5,9,12]
target = 2
result2 = example.search(nums, target)
assert result2 == -1
print(result2)