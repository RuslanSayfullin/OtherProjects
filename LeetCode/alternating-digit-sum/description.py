# Вам дано положительное целое число n. Каждая цифра числа n имеет знак в соответствии со следующими правилами:
# Старшей цифре присваивается положительный знак.
# Каждая другая цифра имеет знак, противоположный знаку соседних цифр.
# Верните сумму всех цифр с соответствующим им знаком.

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        summa: int = 0
        positive_sign: bool = True

        n_to_str = str(n)

        for symbol in n_to_str:
            if positive_sign:
                summa += int(symbol)
                positive_sign = False
            else:
                summa += -(int(symbol))
                positive_sign = True

        return summa
    
example = Solution()
    
n = 521
result1 = example.alternateDigitSum(n)
# Explanation: (+5) + (-2) + (+1) = 4.
assert result1 == 4
print( "result1", result1)

n = 111
result2 = example.alternateDigitSum(n)
# Explanation: (+1) + (-1) + (+1) = 1.
assert result2 == 1
print( "result2", result2)

n = 886996
result3 = example.alternateDigitSum(n)
# Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
assert result3 == 0
print( "result3", result3)