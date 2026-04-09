"""
    Вам даны две строки s и t.
    Строка t генерируется путем случайного перемешивания строки s, а затем добавления еще одной буквы в случайную позицию.
    Верните букву, которая была добавлена ​​к строке t.

"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = "None"

        list_s = list(s)
        list_t = list(t)
        for symbol in list_t:
            if symbol in list_s:
                index = list_s.index(symbol)
                list_s.pop(index)
            else:
                result = symbol

        return result



s = "abcd"
t = "abcde"
example = Solution()
result1 = example.findTheDifference(s, t)
print("result1", result1)

s = ""
t = "y"
result2 = example.findTheDifference(s, t)
print("result2", result2)

s = "a"
t = "aa"
result3 = example.findTheDifference(s, t)
print("result2", result3)