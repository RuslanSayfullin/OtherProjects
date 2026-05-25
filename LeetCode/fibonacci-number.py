# Числа Фибоначчи, обычно обозначаемые F(n), образуют последовательность, называемую последовательностью Фибоначчи, в которой каждое число является суммой двух предыдущих, начиная с 0 и 1. 
# То есть, F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Дано n, вычислите F(n).

class Solution:
    def fib(self, n: int) -> int:
        number: int = 0

        if n == 0:
            number = 0
        elif n == 1:
            number = 1
        else:
            return self.fib(n-2) + self.fib(n-1)
        
        return number


n = 2
example =Solution()
result1 = example.fib(n)
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
assert result1 == 1
print( "result1", result1)

n = 3
example =Solution()
result2 = example.fib(n)
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
assert result2 == 2
print( "result2", result2)

n = 4
example =Solution()
result3 = example.fib(n)
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
assert result3 == 3
print( "result3", result3)