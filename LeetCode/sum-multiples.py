# Дано положительное целое число n. Найдите сумму всех целых чисел в диапазоне [1, n] включительно, которые делятся на 3, 5 или 7.
# Верните целое число, обозначающее сумму всех чисел в заданном диапазоне, удовлетворяющих условию.

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result: int = 0
        divizers: list = []

        for k in range(1, n+1):

            if k % 3 == 0 or k % 5 == 0 or k % 7 == 0:
                divizers.append(k)


        result = sum(divizers)
        return result

example = Solution()
    
n = 7
result1 = example.sumOfMultiples(n)
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
assert result1 == 21
print( "result1", result1)

n = 10
result2 = example.sumOfMultiples(n)
# Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
assert result2 == 40
print( "result2", result2)

n = 9
result3 = example.sumOfMultiples(n)
# Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.
assert result3 == 30
print( "result3", result3)