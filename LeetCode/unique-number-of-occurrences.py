# Если задан массив целых чисел arr, верните true, если количество вхождений каждого значения в массиве уникально, или false в противном случае.
from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        flag: bool = True

        arr_list = Counter(arr)
        value_list = []

        for key, value in arr_list.items():
            if value not in value_list:
                value_list.append(value)
            else:
                flag = False
                break

        return flag


example = Solution()

arr = [1,2,2,1,1,3]
result1 = example.uniqueOccurrences(arr)
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
assert result1
print(result1)

arr = [1,2]
result2 = example.uniqueOccurrences(arr)
assert not result2
print(result2)

arr = [-3,0,1,-3,1,1,1,-3,10,0]
result3 = example.uniqueOccurrences(arr)
assert result3
print(result3)