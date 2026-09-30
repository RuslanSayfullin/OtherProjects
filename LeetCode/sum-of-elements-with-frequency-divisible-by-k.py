# Дан целочисленный массив `nums` и целое число `k`.
# Верните целое число, представляющее собой сумму всех элементов массива `nums`,
# которые делятся на `k` (или 0, если таких элементов нет).
# Примечание: элемент включается в сумму столько раз, сколько он встречается в массиве, если его общая частота вхождения делится на `k`.
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: list[int], k: int) -> int:
        result: int = 0

        nums_count = Counter(nums)

        for key, value in nums_count.items():
            if value % k == 0:
                result += (key * value)

        return result

example = Solution()

nums = [1,2,2,3,3,3,3,4]
k = 2
result1 = example.sumDivisibleByK(nums, k)
# Explanation:
# The number 1 appears once (odd frequency).
# The number 2 appears twice (even frequency).
# The number 3 appears four times (even frequency).
# The number 4 appears once (odd frequency).
# So, the total sum is 2 + 2 + 3 + 3 + 3 + 3 = 16.
assert result1 == 16
print( "result1", result1)