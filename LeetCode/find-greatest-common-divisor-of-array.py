# Дана целочисленная матрица nums. Верните наибольший общий делитель наименьшего и наибольшего чисел из nums.
# Наибольший общий делитель двух чисел — это наибольшее положительное целое число, которое делит оба числа нацело.


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        gcd: int = 0

        nums.sort()
        print(nums)
        if nums[0] == nums[-1]:
            return nums[0]
        else:
            for i in range(nums[0], 0, -1):
                
                if nums[0] % i == 0 and nums[-1] % i == 0:
                    #print(i)
                    gcd = i
                    break

        return gcd


example = Solution()

nums = [2,5,6,9,10]
result1 = example.findGCD(nums)
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.
assert result1 == 2
print( "result1", result1)

nums = [7,5,6,8,3]
result2 = example.findGCD(nums)
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 8.
# The greatest common divisor of 3 and 8 is 1.
assert result2 == 1
print( "result2", result2)
