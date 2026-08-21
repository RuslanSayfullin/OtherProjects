# Целое число без нуля — это положительное целое число, которое не содержит ни одного нуля в своем десятичном представлении.
# Дано целое число n, верните список из двух целых чисел [a, b], где:
# a и b — целые числа без нуля.
# a + b = n
# Тестовые примеры генерируются таким образом, чтобы существовало хотя бы одно допустимое решение. Если допустимых решений много, вы можете вернуть любое из них.

class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        result: list[int] = []

        flag: bool = False
        first: int = 1
        second: int = n - first

        while not flag:
            tmp1 = list(str(first))
            tmp2 = list(str(second))

            if '0' not in tmp1 and '0' not in tmp2:
                flag = True
            else:
                first += 1
                second -= 1
                
        result.append(first)
        result.append(second)
        return result
    
example = Solution()

n = 2
result1 = example.getNoZeroIntegers(n)
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
assert result1 == [1, 1]
print( "result1", result1)

n = 11
result2 = example.getNoZeroIntegers(n)
assert result2 == [2, 9]
print( "result2", result2)
        