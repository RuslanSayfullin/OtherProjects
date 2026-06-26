# Дан массив целых чисел nums. Переместите все четные числа в начало массива, а все нечетные числа в конец.
# Верните любой массив, удовлетворяющий этому условию.
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted_array: list = []
        even = []
        noteven = []


        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                noteven.append(i)
        noteven.sort(reverse=True)

        sorted_array = even + noteven

        return sorted_array
    
example = Solution()
    
nums = [3,1,2,4]
result1 = example.sortArrayByParity(nums)
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
assert result1 == [2,4,3,1]
print( "result1", result1)
        