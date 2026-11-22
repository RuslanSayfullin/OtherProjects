# Даны положительные целые числа n и m.
# Определим два целых числа следующим образом:
# num1: сумма всех целых чисел в диапазоне [1, n] (включительно), которые не делятся на m. 
# num2: сумма всех целых чисел в диапазоне [1, n] (включительно), которые делятся на m.
# Верните целое число, равное num1 - num2.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result: int = 0

        num1: int = 0
        num2: int = 0

        for i in range(1, n+1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i

        result = num1 - num2

        return result


example = Solution()

n = 10
m = 3
result1 = example.differenceOfSums(n, m)
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.
print( "result1", result1)
assert result1 == 19

n = 5
m = 6
result2 = example.differenceOfSums(n, m)
print( "result2", result2)
assert result2 == 15