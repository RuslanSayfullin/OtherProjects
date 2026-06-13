# Вам дан целочисленный массив nums. Уникальными элементами массива являются элементы, которые встречаются в нем ровно один раз.
# Верните сумму всех уникальных элементов массива nums.
from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summa: int = 0

        var_counter = Counter(nums)

        for key, value in var_counter.items():
            if value == 1:
                summa += key

        return summa

        

example = Solution()

nums = [1,2,3,2]
result1 = example.sumOfUnique(nums)
# Explanation: The unique elements are [1,3], and the sum is 4.
assert result1 == 4
print( "result1", result1)

nums = [1,1,1,1,1]
result2 = example.sumOfUnique(nums)
# Explanation: There are no unique elements, and the sum is 0.
assert result2 == 0
print( "result2", result2)

nums = [1,2,3,4,5]
result3 = example.sumOfUnique(nums)
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
assert result3 == 15
print( "result3", result3)