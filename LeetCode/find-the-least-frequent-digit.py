"""
    Дано целое число n. Найдите цифру, которая встречается реже всего в его десятичном представлении. 
    Если несколько цифр имеют одинаковую частоту, выберите наименьшую цифру.
    Верните выбранную цифру в виде целого числа.
    Частота цифры x — это количество раз, которое она встречается в десятичном представлении числа n.
"""
from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        cnt = Counter(n)
        cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]))

        result = int(cnt[0][0])
        return result


n = 1553322
example = Solution()
result1 = example.getLeastFrequentDigit(n)
print("result1", result1)

n = 723344511
result2 = example.getLeastFrequentDigit(n)
print("result2", result2)

