# Дан массив целых чисел nums. Верните наибольший периметр треугольника с ненулевой площадью, образованного тремя из этих длин. 
# Если невозможно образовать треугольник с ненулевой площадью, верните 0.
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest: int = 0

        nums.sort() 

        for k in range(len(nums)-2):
        #print(nums[k])
            if (nums[k] + nums[k+1]) > nums[k+2]:
                largest = nums[k] + nums[k+1] + nums[k+2]



        return largest
    

example = Solution()

nums = [2,1,2]
result1 = example.largestPerimeter(nums)
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
assert result1 == 5
print( "result1", result1)

nums = [1,2,1,10]
result2 = example.largestPerimeter(nums)
# Explanation: You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
assert result2 == 0
print( "result2", result2)