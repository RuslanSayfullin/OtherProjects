# Дан целочисленный массив nums длины n (индексация начинается с 1).
# Элемент nums[i] массива nums называется «особенным», если i является делителем n, то есть n % i == 0.
# Верните сумму квадратов всех «особенных» элементов массива nums.

class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        result: int = 0

        nums_len = len(nums)

        for i in range(1, nums_len+1):
            if nums_len % i == 0:
                result += nums[i-1]*nums[i-1]

        return result


example = Solution()

nums = [1,2,3,4]
result1 = example.sumOfSquares(nums)
# Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
# Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.
assert result1 ==  21
print( "result1", result1)

nums = [2,7,1,19,18,3]
result2 = example.sumOfSquares(nums)
assert result2 ==  63
print( "result2", result2)