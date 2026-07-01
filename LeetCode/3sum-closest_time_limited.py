# Дан массив целых чисел nums длиной n и целочисленное значение target. 
# Необходимо найти три целых числа, расположенных на разных индексах в массиве nums, сумма которых наиболее близка к значению target.
# Верните сумму этих трех чисел.
# Можно предположить, что для каждого входного значения существует ровно одно решение.
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        three_sum: int = 0

        massiv: list = []

        raznitsa: int = 100000000000

        for i in range(len(nums)-2):

            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    summ = nums[i] + nums[j] + nums[k]
                    massiv.append(summ)


        for i in massiv:
            if abs(i - target) < raznitsa:
                three_sum = i
                raznitsa = abs(i - target)

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