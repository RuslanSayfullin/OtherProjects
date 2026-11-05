# Дан целочисленный массив фиксированной длины `arr`. Необходимо продублировать каждое вхождение нуля, сдвинув остальные элементы вправо.
# Обратите внимание, что элементы, выходящие за пределы исходной длины массива, не записываются. 
# Выполните эти изменения непосредственно в исходном массиве; ничего возвращать не нужно.
from collections import deque

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dq = deque(arr)
        len_arr = len(arr)
        arr = []

        for element in range(len(dq)):
            if len(arr) != len_arr:
                arr.append(dq[element])
                if dq[element] == 0:
                    arr.append(0)
            else:
                break

        return arr

example = Solution()

arr = [1,0,2,3,0,4,5,0]
arr = example.duplicateZeros(arr)
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
print( "result1", arr, arr == [1,0,0,2,3,0,0,4])
assert arr == [1,0,0,2,3,0,0,4]
