# Даны две строки, a и b. Верните длину самой длинной необычной подпоследовательности для этих строк. Если такой подпоследовательности не существует, верните -1.
# Необычная подпоследовательность для двух строк — это такая строка, которая является подпоследовательностью ровно одной из них.

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        result: int = -1

        if len(a) != len(b):
            result = max(len(a), len(b))
        else:
            if a != b:

                for i in range(len(a)):
                    if a[0: i+1] not in b:
                        result = i+1

        return result

example = Solution()

a = "aba"
b = "cdc"
result1 = example.findLUSlength(a, b)
# Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
# Note that "cdc" is also a longest uncommon subsequence.
assert result1 == 3
print( "result1", result1)

a = "aaa"
b = "bbb"
result2 = example.findLUSlength(a, b)
# Explanation: The longest uncommon subsequences are "aaa" and "bbb".
assert result2 == 3
print( "result2", result2)

a = "aaa"
b = "aaa"
result3 = example.findLUSlength(a, b)
# Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.
assert result3 == -1
print( "result3", result3)

a = "aefawfawfawfaw"
b = "aefawfeawfwafwaef"
result4 = example.findLUSlength(a, b)
assert result4 == 17
print( "result4", result4)

a = "swoegxvzsfetrdtnoucawucug"
b = "gaqrzczpmtsxlwxdacitrcgklziiya"
result5 = example.findLUSlength(a, b)
assert result5 == 30
print( "result5", result5)