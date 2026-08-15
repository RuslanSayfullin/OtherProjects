# Вам даны два целочисленных массива одинаковой длины: target и arr. За один шаг вы можете выбрать любой непустой подмассив массива arr и перевернуть его. 
# Вы можете сделать любое количество шагов.
# Верните true, если вам удалось сделать массив arr равным массиву target, или false в противном случае.


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:

        return sorted(target) == sorted(arr)


    
example = Solution()
    
target = [1,2,3,4]
arr = [2,4,1,3]
result1 = example.canBeEqual(target, arr)
# Explanation: You can follow the next steps to convert arr to target:
# 1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
# 2- Reverse subarray [4,2], arr becomes [1,2,4,3]
# 3- Reverse subarray [4,3], arr becomes [1,2,3,4]
# There are multiple ways to convert arr to target, this is not the only way to do so.
assert result1
print( "result1", result1)

target = [7]
arr = [7]
result2 = example.canBeEqual(target, arr)
# Explanation: arr is equal to target without any reverses.
assert result2
print( "result2", result2)

target = [3,7,9]
arr = [3,7,11]
result3 = example.canBeEqual(target, arr)
# Explanation: arr does not have value 9 and it can never be converted to target.
assert not result3
print( "result3", result3)


        