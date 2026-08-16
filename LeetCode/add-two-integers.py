# Даны два целых числа num1 и num2; верните сумму этих чисел.

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

    
example = Solution()
    
num1 = 12
num2 = 5
result1 = example.sum(num1, num2)
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
assert result1 == 17
print( "result1", result1)

num1 = -10
num2 = 4
result2 = example.sum(num1, num2)
# Explanation: num1 + num2 = -6, so -6 is returned.
assert result2 == -6
print( "result2", result2)