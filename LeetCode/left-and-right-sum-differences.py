# Вам дан массив целых чисел nums размером n, индексированный с нуля.
# Определите два массива leftSum и rightSum, где:
# leftSum[i] — сумма элементов слева от индекса i в массиве nums. Если такого элемента нет, leftSum[i] = 0.
# rightSum[i] — сумма элементов справа от индекса i в массиве nums. Если такого элемента нет, rightSum[i] = 0.
# Верните массив целых чисел answer размером n, где answer[i] = |leftSum[i] - rightSum[i]|.
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        difference: list = []

        if len(nums) == 1:
            difference.append(0)
            return difference
        
        leftSum = [0,]
        for i in range(len(nums)-1):
            res = nums[i] + leftSum[i]
            leftSum.append(res)

        rightSum = [0,]
        rev_num = nums[::-1]
        for i in range(len(rev_num)-1):
            res = rev_num[i] + rightSum[i]
            rightSum.append(res)

        
        rightSum = rightSum[::-1]

        #print(leftSum, rightSum)

        for i in range(len(leftSum)):
            difference.append(abs(leftSum[i] - rightSum[i]))

        return difference

example = Solution()

nums = [10,4,8,3]
result1 = example.leftRightDifference(nums)
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
assert result1 == [15,1,11,22]
print( "result1", result1)

nums = [1]
result2 = example.leftRightDifference(nums)
# The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].
assert result2 == [0]
print( "result2", result2)
