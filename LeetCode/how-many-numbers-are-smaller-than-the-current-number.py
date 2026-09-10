# Для заданного массива nums определите для каждого элемента nums[i], сколько чисел в этом массиве меньше него. 
# Иными словами, для каждого nums[i] нужно подсчитать количество таких индексов j, при которых j != i и nums[j] < nums[i].
# Верните результат в виде массива.
import copy

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result: list = []

        nums_set = copy.deepcopy(nums)
        nums_set.sort()

        for element in nums:
            result.append(nums_set.index(element))    

        return result


example = Solution()
    
nums = [8,1,2,2,3]
result1 = example.smallerNumbersThanCurrent(nums)
assert result1 == [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
print( "result1", result1) 