# Дана строка s; отсортируйте её в порядке убывания частоты встречаемости символов. Частота символа — это количество его вхождений в строку.
# Верните отсортированную строку. Если существует несколько вариантов ответа, верните любой из них.
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        result: str = ""
        s_counted = Counter(s)

        sorted_s = dict(sorted(s_counted.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_s.items():
            result = result + (key * value)

        return result

example = Solution()

s = "tree"
result1 = example.frequencySort(s)
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
print( "result1", result1)
assert result1 == "eetr"