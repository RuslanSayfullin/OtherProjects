# Перестановка (perm) n + 1 целых чисел из всех целых чисел в диапазоне [0, n] может быть представлена ​​в виде строки s длиной n, где:
# s[i] == 'I', если perm[i] < perm[i + 1], и
# s[i] == 'D', если perm[i] > perm[i + 1].
# Получив строку s, восстановите перестановку (perm) и верните её. Если существует несколько допустимых перестановок (perm), верните любую из них.

from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result: list[int] = []

        low: int = 0
        high: int = len(s)

        for i in range(len(s)):
            if s[i] == "I":
                result.append(low)
                low += 1
            elif s[i] == "D":
                result.append(high)
                high -= 1

        result.append(high)
        return result

       
example = Solution()
    
s = "IDID"
result1 = example.diStringMatch(s)
assert result1 == [0,4,1,3,2]
print( "result1", result1)

s = "III"
result2 = example.diStringMatch(s)
assert result2 == [0,1,2,3]
print( "result2", result2)

s = "DDI"
result3 = example.diStringMatch(s)
assert result3 == [3,2,0,1]
print( "result3", result3)