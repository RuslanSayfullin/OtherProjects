# Дан непустой массив неотрицательных целых чисел nums. Степень этого массива определяется как максимальная частота любого из его элементов.
# Ваша задача — найти наименьшую возможную длину (непрерывного) подмассива nums, имеющего ту же степень, что и nums.
from typing import List
from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first_seen = {}  # Здесь храним индекс первого появления числа
        last_seen = {}   # Здесь храним индекс последнего появления числа
        counts = {}      # Здесь храним количество повторений числа
        
        # 1. Собираем всю необходимую информацию за один проход
        for index, num in enumerate(nums):
            if num not in first_seen:
                first_seen[num] = index
            last_seen[num] = index
            counts[num] = counts.get(num, 0) + 1
            
        # 2. Находим максимальную частоту (степень массива)
        degree = max(counts.values())
        
        # 3. Ищем минимальную длину подмассива среди лидеров по частоте
        min_length = len(nums)
        
        for num in counts:
            if counts[num] == degree:
                # Длина отрезка от первого до последнего упоминания числа
                current_length = last_seen[num] - first_seen[num] + 1
                min_length = min(min_length, current_length)
                
        return min_length


example =Solution()

nums = [1,2,2,3,1]
result1 = example.findShortestSubArray(nums)
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
assert result1 == 2
print( "result1", result1)

nums = [1,2,2,3,1,4,2]
result2 = example.findShortestSubArray(nums)
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
assert result2 == 6
print( "result2", result2)

