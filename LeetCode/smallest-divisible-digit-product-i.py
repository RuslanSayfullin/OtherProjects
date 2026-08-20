# Вам даны два целых числа n и t. 
# Верните наименьшее число, большее или равное n, такое, что произведение его цифр делится на t.

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product_of_digits(x: int) -> int:
            product = 1
            while x > 0:
                digit = x % 10
                product *= digit
                x //= 10
            return product

        i = n
        while True:
            if product_of_digits(i) % t == 0:
                return i
            i += 1
    

example = Solution()
    
n = 10
t = 2
result1 = example.smallestNumber(n, t)
# Explanation: The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.
assert result1 == 10
print( "result1", result1)

n = 15
t = 3
result2 = example.smallestNumber(n, t)
# Explanation: The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.
assert result2 == 16
print( "result2", result2)
