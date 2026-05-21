
# Дана строка s, состоящая из слов и пробелов. Верните длину последнего слова в строке.
# Слово является максимальным, состоящим только из символов, не являющихся пробелами.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        
        if len(s) < 1:
            pass
        else:
            lst = s.split()

            length = len(lst[-1])

        return length

s = "Hello World"
example =Solution()
result1 = example.lengthOfLastWord(s)
assert result1 == 5
print( "result1", result1)

s =  "   fly me   to   the moon  "
example =Solution()
result2 = example.lengthOfLastWord(s)
assert result2 == 4
print( "result2", result2)

s =  "luffy is still joyboy"
example =Solution()
result3 = example.lengthOfLastWord(s)
assert result3 == 6
print( "result3", result3)