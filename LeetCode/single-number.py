# Дан непустой массив целых чисел nums, в котором каждый элемент встречается дважды, кроме одного. Найдите этот единственный элемент.
# Необходимо реализовать решение с линейной временной сложностью и использовать только постоянное дополнительное пространство.
from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0

        if len(nums) == 0:
            return single_number

        cnt = Counter(nums)
        single_number = next((key for key, value in cnt.items() if value == 1), 0)
        
        return single_number


nums = [2,2,1]
example = Solution()
result1 = example.singleNumber(nums)
print("result1", result1)

nums = [4,1,2,1,2]
result2 = example.singleNumber(nums)
print("result2", result2)

nums = [1]
result3 = example.singleNumber(nums)
print("result3", result3)