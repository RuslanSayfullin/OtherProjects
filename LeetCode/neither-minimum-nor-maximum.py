# Дан массив целых чисел nums, содержащий различные положительные целые числа. 
# Найдите и верните любое число из массива, которое не является ни минимальным, ни максимальным значением в массиве, или -1, если такого числа нет.
# Верните выбранное целое число.

class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        result: int = -1

        if len(nums) > 2:

            maximum = sorted(nums)
            if (maximum[0] != maximum[1]):
                result = maximum[1]

        return result

example = Solution()
    
nums = [3,2,1,4]
result1 = example.findNonMinOrMax(nums)
assert result1 == 2
# Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.
print( "result1", result1)

nums = [1,2]
result2 = example.findNonMinOrMax(nums)
assert result2 == -1
# Explanation: Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, there is no answer.
print( "result2", result2)

nums = [2,1,3]
result3 = example.findNonMinOrMax(nums)
assert result3 == 2
# Explanation: Since 2 is neither the maximum nor the minimum value in nums, it is the only valid answer.
print( "result3", result3)

nums = [1]
result4 = example.findNonMinOrMax(nums)
assert result4 == -1
print( "result4", result4)
