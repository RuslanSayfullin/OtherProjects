# Дано целое число n. Верните разницу между произведением его цифр и суммой его цифр.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        result: int = 0


        subtract: int = 1
        summa: int = 0

        list_str_n = list(str(n))

        for element in list_str_n:
            subtract = subtract * (int(element))
            summa = summa + (int(element))

        # print(subtract, summa)
        result = subtract - summa
        return result
    
example = Solution()

n = 234
result1 = example.subtractProductAndSum(n)
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
assert result1 == 15
print( "result1", result1)

n = 4421
result1 = example.subtractProductAndSum(n)
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
assert result1 == 21
print( "result1", result1)