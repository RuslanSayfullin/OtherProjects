# Дана строка s.
# Префикс строки s считается допустимым, если его символы можно переставить так, чтобы получилась чередующаяся строка.
# Верните количество допустимых префиксов строки s.
# Строка называется чередующейся, если никакие два соседних символа в ней не совпадают.

class Solution:
    def countValidPrefixes(self, s: str) -> int:
        result: int = 0
        counts: dict[str, int] = {}
        max_count = 0

        for n, ch in enumerate(s, start=1):
            counts[ch] = counts.get(ch, 0) + 1
            max_count = max(max_count, counts[ch])

            if max_count <= (n + 1) // 2:
                result += 1

        return result
    
example = Solution()

s = "00101"
result1 = example.countValidPrefixes(s)
# Explanation: The valid prefixes are:
# "0": It is already an alternating string.
# "001": It can be rearranged into "010", which is an alternating string.
# "00101": It can be rearranged into "01010", which is an alternating string
print( "result1", result1)
assert result1 == 3