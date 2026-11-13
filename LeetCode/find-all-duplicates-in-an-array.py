# Дан целочисленный массив `nums` длины `n`, в котором все числа находятся в диапазоне от 1 до `n`, а каждое число встречается не более двух раз. 
# Верните массив, содержащий все числа, которые встречаются дважды.
# Необходимо разработать алгоритм, который работает за время O(n) и использует лишь константный объем дополнительной памяти (не считая памяти, необходимой для хранения результата).
from collections import Counter

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result: list[int] = []

        nums_cnt = Counter(nums)

        for k, value in nums_cnt.items():
            if value == 2:
                result.append(k)

        return result


example = Solution()

nums = [4,3,2,7,8,2,3,1]
result1 = example.findDuplicates(nums)
# Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
# Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.
print( "result1", result1)
assert result1 ==  [2,3]
