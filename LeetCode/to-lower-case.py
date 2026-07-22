# Дана строка s. Верните строку, заменив все прописные буквы на одинаковые строчные.

class Solution:
    def toLowerCase(self, s: str) -> str:
        result: str = ""

        result = s.lower()

        return result

example =Solution()

s = "Hello"
result1 = example.toLowerCase(s)
assert result1 == "hello"
print( "result1", result1)

s = "here"
result2 = example.toLowerCase(s)
assert result2 == "here"
print( "result2", result2)

s = "LOVELY"
result3 = example.toLowerCase(s)
assert result3 == "lovely"
print( "result3", result3)