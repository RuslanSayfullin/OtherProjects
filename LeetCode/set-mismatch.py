# У вас есть множество целых чисел s, которое изначально содержит все числа от 1 до n. 
# К сожалению, из-за какой-то ошибки одно из чисел в множестве дублировалось, превращаясь в другое число, что приводит к повторению одного числа и исчезновению другого.
# Вам предоставлен целочисленный массив nums, представляющий состояние данных этого набора после ошибки.
# Найдите число, которое встречается дважды, и число, которое отсутствует, и верните их в виде массива.
from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        error_nums = [0, 0]
        list_len = len(nums)

        cnt = Counter(nums)
        double_number = next((key for key, value in cnt.items() if value == 2), 0)

        error_nums[0] = double_number
        for h in range(1, (list_len+1)):

            if not h in nums:
                error_nums[1] = h

        return error_nums
    
nums = [1,2,2,4]
example = Solution()
result1 = example.findErrorNums(nums)
print("result1", result1)

nums = [1,1]
result2 = example.findErrorNums(nums)
print("result2", result2)

