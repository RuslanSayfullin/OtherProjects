# Дан массив положительных целых чисел `arr`. Верните сумму всех возможных подмассивов массива `arr`, имеющих нечетную длину.
# Подмассив — это непрерывная подпоследовательность элементов массива.

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        result: int = 0

        massiv = []
        for e in arr:
            result += e
        step = 3
        while step <= len(arr):

            
            for i in range(len(arr)):
                if (len(arr[i:i+step]) % 2 != 0) and len(arr[i:i+step]) == step:

                    massiv.append(arr[i:i+step])
            step += 2


        for elem in massiv:
            result += sum(elem)
        return result


example = Solution()

arr = [1,4,2,5,3]
result1 = example.sumOddLengthSubarrays(arr)
print( "result1", result1)
assert result1 == 58

arr = [7,6,8,6]
result2 = example.sumOddLengthSubarrays(arr)
print( "result2", result2)
assert result2 == 68