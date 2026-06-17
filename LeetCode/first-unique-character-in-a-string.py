# Дана строка s. Найдите в ней первый неповторяющийся символ и верните его индекс. Если его нет, верните -1.
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        first: int = -1

        countered = Counter(s)
        for symbol in s:
            if countered[symbol] == 1:
                first = s.index(symbol)
                break

        return first
    
example = Solution()

s = "leetcode"
result1 = example.firstUniqChar(s)
# Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.
assert result1 == 0
print( "result1", result1)

s = "loveleetcode"
result2 = example.firstUniqChar(s)
assert result2 == 2
print( "result2", result2)

s = "aabb"
result3 = example.firstUniqChar(s)
assert result3 == -1
print( "result3", result3)
