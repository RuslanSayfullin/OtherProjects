# Даны два целых числа n и k.
# Положительное целое число x называется совместимым, если оно удовлетворяет следующим двум условиям:
# abs(n - x) <= k
# (n & x) == 0
# Верните сумму всех совместимых целых чисел x.
# Примечание:
# Здесь & обозначает операцию побитового «И» (bitwise AND). Абсолютная разность между целыми числами i и j определяется как abs(i - j).

class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        result: int = 0

        for x in range(1, abs(n+k)+1):
            if abs(n - x) <= k and (n & x) == 0:
                    result += x

        return result

example = Solution()

n = 2
k = 3
result1 = example.sumOfGoodIntegers(n, k)
# Explanation: The compatible integers are:
# x = 1, since abs(2 - 1) = 1 and 2 & 1 = 0.
# x = 4, since abs(2 - 4) = 2 and 2 & 4 = 0.
# x = 5, since abs(2 - 5) = 3 and 2 & 5 = 0.
# Thus, the answer is 1 + 4 + 5 = 10.
assert result1 == 10
print( "result1", result1)