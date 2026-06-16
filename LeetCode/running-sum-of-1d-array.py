# Дан массив nums. Мы определяем текущую сумму массива как runningSum[i] = sum(nums[0]…nums[i]).
# Возвращаем текущую сумму nums.
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summa: list = []
        var: int = 0

        for i in nums:
            var += i
            summa.append(var)

        return summa

    
example = Solution()

nums = [1,2,3,4]
result1 = example.runningSum(nums)
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
assert result1 == [1,3,6,10]
print( "result1", result1)

nums = [1,1,1,1,1]
result2 = example.runningSum(nums)
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
assert result2 == [1,2,3,4,5]
print( "result2", result2)

nums = [3,1,2,10,1]
result3= example.runningSum(nums)
assert result3 == [3,4,6,16,17]
print( "result3", result3)