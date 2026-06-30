# Дан массив целых чисел nums. Найдите три числа, произведение которых максимально, и верните максимальное произведение.
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maximum_product: int = 0
        multipliers: list = []

        left: int = 0
        right: int = len(nums) - 1

        sorted_nums = sorted(nums)


        if sorted_nums[left] > 0:
            # если все числа положительные
            maximum_product = sorted_nums[right-2] * sorted_nums[right-1] * sorted_nums[right]
        elif sorted_nums[left] < 0 and sorted_nums[right] < 0:
            # если все числа отрицательные
            maximum_product = sorted_nums[right-2] * sorted_nums[right-1] * sorted_nums[right]

        else:
            if (sorted_nums[left] < 0) and (abs(sorted_nums[left]) > abs(sorted_nums[right])) and (sorted_nums[left+1] < 0) or (sorted_nums[left] * sorted_nums[left+1] * sorted_nums[right] > sorted_nums[right] * sorted_nums[right - 1] * sorted_nums[right - 2]):

                multipliers.append(sorted_nums[left])
                multipliers.append(sorted_nums[left+1])
                multipliers.append(sorted_nums[right])
            else:
                multipliers.append(sorted_nums[right])
                multipliers.append(sorted_nums[right-1])
                multipliers.append(sorted_nums[right-2])

            maximum_product = multipliers[0] * multipliers[1] * multipliers[2]

        return maximum_product
    
example = Solution()

nums = [1,2,3]
result1 = example.maximumProduct(nums)
assert result1 == 6
print( "result1", result1)

nums = [1,2,3,4]
result2 = example.maximumProduct(nums)
assert result2 == 24
print( "result2", result2)

nums = [-1,-2,-3]
result3 = example.maximumProduct(nums)
assert result3 == -6
print( "result3", result3)

nums = [-100,-98,-1,2,3,4]
result4 = example.maximumProduct(nums)
assert result4 == 39200
print( "result4", result4)

nums = [-100,-2,-3,1]
result5 = example.maximumProduct(nums)
assert result5 == 300
print( "result5", result5)

nums = [-4,-3,-2,-1,60]
result6 = example.maximumProduct(nums)
assert result6 == 720
print( "result6", result6)

nums = [-1,-2,-3,-4]
result7 = example.maximumProduct(nums)
assert result7 == -6
print( "result7", result7)

nums = [9,1,5,6,7,2]
result8 = example.maximumProduct(nums)
assert result8 == 378
print( "result8", result8)


