# Дан массив положительных целых чисел nums. Верните массив, состоящий из цифр каждого целого числа из nums, разделенных в том же порядке, в котором они встречаются в nums.
# Разделение цифр целого числа означает получение всех его цифр в том же порядке.
# Например, для целого числа 10921 разделение цифр будет [1,0,9,2,1].
from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        separated: list[int] = []

        
        for element in nums:
            if -10 < element < 10:
                separated.append(element)
                continue
            else:
                inttostr = str(element)
                for symbol in inttostr:
                    separated.append(int(symbol))

        return separated
    
example = Solution()
    
nums = [13,25,83,77]
result1 = example.separateDigits(nums)
# Explanation: 
# - The separation of 13 is [1,3].
# - The separation of 25 is [2,5].
# - The separation of 83 is [8,3].
#- The separation of 77 is [7,7].
# answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
assert result1 == [1,3,2,5,8,3,7,7]
print( "result1", result1)

nums = [7,1,3,9]
result2 = example.separateDigits(nums)
# Explanation:  The separation of each integer in nums is itself. answer = [7,1,3,9].
assert result2 == [7,1,3,9]
print( "result2", result2)
