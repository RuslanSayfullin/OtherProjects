# Последовательность Трибоначчи Tn определяется следующим образом:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Если задано значение n, верните значение Tn.
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def tribonacci(self, n: int) -> int:
        number: int = 0

        if n == 0:
            number = 0
        elif n == 1:
            number = 1
        elif n == 2:
            number = 1
        else:
            return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        
        return number

example =Solution()

n = 4
result1 = example.tribonacci(n)
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
assert result1 == 4
print( "result1", result1)

n = 25
result2 = example.tribonacci(n)
assert result2 == 1389537
print( "result2", result2)

n = 31
result3 = example.tribonacci(n)
assert result2 == 53798080
print( "result3", result3)


