# Дан массив целых чисел nums. Найдите три числа, произведение которых максимально, и верните максимальное произведение.
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maximum_product: int = 0
        multipliers: list = []

        left: int = 0
        right: int = len(nums) - 1

        sorted_nums = sorted(nums)


        for i in range(3):
            

            if abs(sorted_nums[left]) >= abs(sorted_nums[right]):
                multipliers.append(sorted_nums[left])
                left += 1
            else:
                multipliers.append(sorted_nums[right])
                right -= 1



        maximum_product = multipliers[0] * multipliers[1] * multipliers[2]

        return maximum_product
    
example = Solution()

nums = [1,2,3]
result1 = example.maximumProduct(nums)
assert result1 == 6
print( "result1", result1)

nums = [1,2,3,4]
result2= example.maximumProduct(nums)
assert result2 == 24
print( "result2", result2)

nums = [-1,-2,-3]
result3= example.maximumProduct(nums)
assert result3 == -6
print( "result3", result3)

nums = [-100,-98,-1,2,3,4]
result4= example.maximumProduct(nums)
assert result4 == 39200
print( "result4", result4)

