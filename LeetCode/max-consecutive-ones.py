# Дана двоичная последовательность чисел nums. Верните максимальное количество последовательных единиц в этой последовательности.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result: int = 0

        if 1 not in nums:
            return result

        period: bool = False
        counter: int = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                period = True
            elif nums[i] == 0:
                period = False

            if period:
                counter += 1

            else:
                if counter > result:
                    result = counter
                else:
                    pass

                counter = 0
        if counter > result:
            result = counter
        return result

example = Solution()

nums = [1,1,0,1,1,1]
result1 = example.findMaxConsecutiveOnes(nums)
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

print( "result1", result1)
assert result1 == 3

nums = [1,0,1,1,0,1]
result2 = example.findMaxConsecutiveOnes(nums)

print( "result2", result2)

assert result2 == 2