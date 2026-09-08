# Вам дан массив целых чисел nums с индексацией от 0 и целое число k. 
# Ваша задача — выполнить следующую операцию ровно k раз, чтобы максимизировать свой результат:
# 1.Выбрать элемент m из массива nums.
# 2.Удалить выбранный элемент m из массива.
# 3.Добавить в массив новый элемент со значением m + 1.
# Увеличить свой результат на m.
# Вернуть максимальный результат, которого вы можете достичь, выполнив операцию ровно k раз.

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        result: int = 0

        nums.sort(reverse=True)

        for i in range(k):
            result += nums[0]

            nums[0] = nums[0] + 1

        return result
 
example = Solution()
    
nums = [1,2,3,4,5]
k = 3
result1 = example.maximizeSum(nums, k)
# Explanation: We need to choose exactly 3 elements from nums to maximize the sum.
# For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
# For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
# For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
# So, we will return 18.
# It can be proven, that 18 is the maximum answer that we can achieve.
assert result1 == 18
print( "result1", result1) 

nums = [5,5,5]
k = 2
result2 = example.maximizeSum(nums, k)
# Explanation: We need to choose exactly 2 elements from nums to maximize the sum.
# For the first iteration, we choose 5. Then sum is 5 and nums = [5,5,6]
# For the second iteration, we choose 6. Then sum is 5 + 6 = 11 and nums = [5,5,7]
# So, we will return 11.
# It can be proven, that 11 is the maximum answer that we can achieve.
assert result2 == 11
print( "result2", result2) 