# Вам дан массив «гора» с индексами от 0. Ваша задача — найти все вершины в этом массиве.
# Верните массив, состоящий из индексов вершин в заданном массиве в любом порядке.
# Примечания: Вершина определяется как элемент, который строго больше своих соседних элементов.
# Первый и последний элементы массива не являются вершинами.
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks: list = []

        for i in range(1, len(mountain)-1):

            if mountain[i-1] < mountain[i] > mountain[i+1]:
                
                peaks.append(i)

        return peaks
    
example = Solution()

mountain = [2,4,4]
result1 = example.findPeaks(mountain)
# Explanation: mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
# mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
# So the answer is [].
assert result1 == []
print( "result1", result1)

mountain = [1,4,3,8,5]
result2 = example.findPeaks(mountain)
# Explanation: mountain[0] and mountain[4] can not be a peak because they are first and last elements of the array.
# mountain[2] also can not be a peak because it is not strictly greater than mountain[3] and mountain[1].
# But mountain [1] and mountain[3] are strictly greater than their neighboring elements.
# So the answer is [1,3].
assert result2 == [1,3]
print( "result2", result2)
