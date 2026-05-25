# Дан целочисленный массив nums. Верните третье различное максимальное число в этом массиве. 
# Если третьего максимального числа не существует, верните максимальное число.
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        setnums = set(nums)
        nums = list(setnums)
        nums.sort()

        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
        
example =Solution()

nums = [3,2,1]
result1 = example.thirdMax(nums)
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
assert result1 == 1
print( "result1", result1)

nums = [1,2]
result2 = example.thirdMax(nums)
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
assert result2 == 2
print( "result2", result2)

nums = [2,2,3,1]
result3 = example.thirdMax(nums)
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
assert result3 == 1
print( "result3", result3)

nums = [-1,2,3]
result4 = example.thirdMax(nums)
assert result4 == -1
print( "result3", result3)