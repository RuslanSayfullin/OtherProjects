# Дан массив целых чисел arr и три целых числа a, b и c. Необходимо найти количество подходящих троек.
# Тройка (arr[i], arr[j], arr[k]) считается хорошей, если выполняются следующие условия:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c

# Где |x| обозначает абсолютное значение x.
# Возвращает количество правильных троек.
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        pass



arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
example = Solution()
result1 = example.countGoodTriplets(arr, a, b, c)
assert result1 == 4
# Существует 4 подходящих тройки: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
print(result1)

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
example = Solution()
result2 = example.countGoodTriplets(arr, a, b, c)
assert result2 == 0
# Ни одна тройка не удовлетворяет всем условиям.
print(result2)
