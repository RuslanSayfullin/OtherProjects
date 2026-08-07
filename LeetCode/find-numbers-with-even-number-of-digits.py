# Дан массив целых чисел nums. Верните значение, указывающее, сколько из них содержат четное количество цифр.

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        result: int = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                result += 1


        return result

example = Solution()
    
nums = [12,345,2,6,7896]
result1 = example.findNumbers(nums)
# Explanation: 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
assert result1 == 2
print( "result1", result1)

nums = [555,901,482,1771]
result2 = example.findNumbers(nums)
# Explanation: Only 1771 contains an even number of digits.

assert result2 == 1
print( "result2", result2)