# Сбалансированными считаются строки, содержащие равное количество символов «L» и «R».
# Дана сбалансированная строка s, разбейте её на некоторое количество подстрок таким образом, чтобы:
# Каждая подстрока была сбалансированной.
# Верните максимальное количество сбалансированных строк, которое можно получить.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result: int = 0

        r_symbols: int = 0
        l_symbols: int = 0

        for symbol in s:
            if symbol == "R":
                r_symbols += 1
            elif symbol == "L":
                l_symbols += 1

            if r_symbols == l_symbols:
                result += 1
                r_symbols = 0
                l_symbols = 0


        return result

example = Solution()
    
s = "RLRRLLRLRL"
result1 = example.balancedStringSplit(s)
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'
assert result1 == 4
print( "result1", result1)

s = "RLRRRLLRLL"
result2 = example.balancedStringSplit(s)
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
assert result2 == 2
print( "result2", result2)

s = "LLLLRRRR"
result3 = example.balancedStringSplit(s)
# Explanation: s can be split into "LLLLRRRR".
assert result3 == 1
print( "result3", result3)