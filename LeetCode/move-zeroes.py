# Дана целочисленная матрица nums. 
# Необходимо переместить все нули в конец матрицы, сохраняя при этом относительный порядок ненулевых элементов.
# Обратите внимание, что это необходимо сделать непосредственно в матрице, не создавая её копию.
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            pass
        else:
            for i in range(len(nums)):

                if nums[i] == 0:
                    nums.append(nums.pop(nums.index(nums[i])))




nums = [0,1,0,3,12]
example = Solution()
example.moveZeroes(nums)
print(nums)
assert nums == [1,3,12,0,0]


nums = [0]
example = Solution()
example.moveZeroes(nums)
print(nums)
assert nums == [0]
