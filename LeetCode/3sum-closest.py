# Дан массив целых чисел nums длиной n и целочисленное значение target. 
# Необходимо найти три целых числа, расположенных на разных индексах в массиве nums, сумма которых наиболее близка к значению target.
# Верните сумму этих трех чисел.
# Можно предположить, что для каждого входного значения существует ровно одно решение.
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        three_sum: int = 0

        massiv: list = []
        minimum: int = 100000

        nums.sort()
        

        for i in range(len(nums) - 2):
            massiv.append((nums[i]+nums[i+1]+nums[i+2] - target))

        print(massiv)
        for e in massiv:
            if abs(e) < minimum:
                three_sum = e + target
                minimum = abs(e)

        return three_sum
    
example = Solution()

nums = [-1,2,1,-4]
target = 1
result1 = example.threeSumClosest(nums, target)
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
assert result1 == 2
print( "result1", result1)

nums = [0,0,0]
target = 1
result2 = example.threeSumClosest(nums, target)
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
assert result2 == 0
print( "result2", result2)

nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
result3 = example.threeSumClosest(nums, target)
assert result3 == -2
print( "result3", result3)