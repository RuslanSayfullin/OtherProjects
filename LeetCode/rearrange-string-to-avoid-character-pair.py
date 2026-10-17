# Дана строка s и две различные строчные латинские буквы x и y.
# Переставьте символы в строке s так, чтобы получить новую строку t, удовлетворяющую следующим условиям:
# t является перестановкой символов строки s. 
# В строке t каждое вхождение буквы y располагается перед каждым вхождением буквы x.
# Верните любую подходящую строку t.
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        result: str = ""
        temp = ""

        t = list(s)

        for s in t:
            if s == x:
                temp = temp+s
            else:
                result = result + s

        result = result + temp


        return result


example = Solution()

s = "aabc"
x = "a"
y = "c"
result1 = example.rearrangeString(s, x, y)
# The string "cbaa" is a permutation of "aabc", and every occurrence of 'c' appears before every occurrence of 'a'.
assert result1 == "bcaa"
print( "result1", result1)

s = "dcab"
x = "d"
y = "b"
result2 = example.rearrangeString(s, x, y)
# The string "cabd" is a permutation of "dcab", and every occurrence of 'b' appears before every occurrence of 'd'.
assert result2 == "cabd"
print( "result2", result2)

s = "axe"
x = "o"
y = "x"
result3 = example.rearrangeString(s, x, y)
# The string "axe" is already valid. Since 'o' does not occur in the string, the required condition is automatically satisfied.
assert result3 == "axe"
print( "result3", result3)

s = "radp"
x = "r"
y = "d"
result4 = example.rearrangeString(s, x, y)
# The string "cabd" is a permutation of "dcab", and every occurrence of 'b' appears before every occurrence of 'd'.
print( "result4", result4)
assert result4 == "adpr"
