# Целое число, деляющееся на сумму своих цифр, называется числом Харшада. 
# Вам дано целое число x. Верните сумму цифр числа x, если x является числом Харшада, в противном случае верните -1.

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        result: int = -1

        str_x = str(x)

        res: int = 0
        for element in str_x:
            res += int(element)

        if x % res == 0:
            result = res

        return result


example = Solution()
    
x = 18
result1 = example.sumOfTheDigitsOfHarshadNumber(x)
# Explanation: The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and the answer is 9.
assert result1 == 9
print( "result1", result1)