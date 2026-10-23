# Дан массив целых чисел `nums` длины `n`.
# Стоимостью массива считается значение его первого элемента. Например, стоимость массива `[1, 2, 3]` равна 1, а стоимость массива `[3, 4, 1]` — 3.
# Необходимо разбить массив `nums` на 3 непересекающихся непрерывных подмассива.
# Верните минимально возможную сумму стоимостей этих подмассивов.

class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        result: int = 0


        nums2 = nums[1:]
        nums2 = sorted(nums2)
        print(nums2)
        result = nums[0] + nums2[0] + nums2[1]
        
        return result

example = Solution()

nums = [1,2,3,12]
result1 = example.minimumCost(nums)
# Explanation: The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
# The other possible ways to form 3 subarrays are:
# - [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
# - [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.
assert result1 == 6
print( "result1", result1)

nums = [5,4,3]
result2 = example.minimumCost(nums)
# Explanation: The best possible way to form 3 subarrays is: [5], [4], and [3] at a total cost of 5 + 4 + 3 = 12.
# It can be shown that 12 is the minimum cost achievable.
assert result2 == 12
print( "result2", result2)

nums = [10,3,1,1]
result3 = example.minimumCost(nums)
assert result3 == 12
print( "result3", result3)