# Даны два положительных целых числа a и b. Верните количество общих делителей этих чисел.
# Целое число x является общим делителем чисел a и b, если x делит как a, так и b.

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common_divisers: int = 0
        #divisers: list = []

        big_element = a if a >= b else b
        little_element = a if a <= b else b

        for d in range(1, (big_element // 2 + 1)):
            if big_element % d == 0 and little_element % d == 0:

                #divisers.append(d)
                common_divisers += 1

        if a == b:
            common_divisers += 1 # если элементы равны, само число общий делитель

        return common_divisers
    
example = Solution()
    
a = 12
b = 6
result1 = example.commonFactors(a, b)
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
assert result1 == 4
print( "result1", result1)

a = 25
b = 30
result2 = example.commonFactors(a, b)
# Explanation: The common factors of 25 and 30 are 1, 5.
assert result2 == 2
print( "result2", result2)

a = 32
b = 408
result3 = example.commonFactors(a, b)
assert result3 == 4
print( "result3", result3)

a = 885
b = 885
result4 = example.commonFactors(a, b)
assert result4 == 8
print( "result4", result4)

