# Даны две строки s и t. Определите, изоморфны ли они.
# Две строки s и t изоморфны, если символы в строке s можно заменить, чтобы получить строку t.
# Все вхождения одного символа должны быть заменены другим символом с сохранением порядка символов. 
# Никакие два символа не могут соответствовать одному и тому же символу, но один символ может соответствовать самому себе.
from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for c1, c2 in zip(s, t):
            if c1 in map_s_to_t:
                if map_s_to_t[c1] != c2:
                    return False
            else:
                map_s_to_t[c1] = c2

            if c2 in map_t_to_s:
                if map_t_to_s[c2] != c1:
                    return False
            else:
                map_t_to_s[c2] = c1

        return True

example = Solution()

s = "egg"
t = "add"
result1 = example.isIsomorphic(s, t)
# Explanation: The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'
assert result1
print( "result1", result1)

s = "f11"
t = "b23"
result2 = example.isIsomorphic(s, t)
# Explanation: The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.
assert not result2
print( "result2", result2)

s = "paper"
t = "title"
result3 = example.isIsomorphic(s, t)
assert result3
print( "result3", result3)

s = "bbbaaaba"
t = "aaabbbba"
result4 = example.isIsomorphic(s, t)
assert not result4
print( "result3", result4)