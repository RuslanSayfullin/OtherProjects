# Дан массив целых чисел `nums`, не содержащий нулей. 
# Найдите наибольшее положительное целое число `k`, такое, что число `-k` также присутствует в массиве.
# Верните это положительное целое число `k`. Если такого числа нет, верните -1.

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        result: int = -1

        nums.sort()

        for i in nums:
            if -i in nums:
                result = i
      
        return result


example = Solution()

nums = [-1,2,-3,3]
result1 = example.findMaxK(nums)
# Explanation: 3 is the only valid k we can find in the array.
assert result1 == 3
print(result1)

nums = [-1,10,6,7,-7,1]
result2 = example.findMaxK(nums)
# Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
assert result2 == 7
print(result2)

nums = [-10,8,6,7,-2,-3]
result3 = example.findMaxK(nums)
# Explanation: There is no a single valid k, we return -1.
assert result3 == -1
print(result3)