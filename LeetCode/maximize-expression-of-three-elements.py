# Дан целочисленный массив `nums`.
# Выберите из массива `nums` три элемента `a`, `b` и `c`, находящиеся по различным индексам, так, чтобы значение выражения `a + b - c` было максимальным.
# Верните целое число, представляющее максимально возможное значение этого выражения.

class Solution:
    def maximizeExpressionOfThree(self, nums: list[int]) -> int:
        result: int = 0

        nums.sort(reverse=True)

        result = nums[0] + nums[1] - nums[-1]

        return result

example = Solution()

nums = [1,4,2,5]
result1 = example.maximizeExpressionOfThree(nums)
# Explanation: We can choose a = 4, b = 5, and c = 1. The expression value is 4 + 5 - 1 = 8, which is the maximum possible.
print( "result1", result1)
assert result1 == 8