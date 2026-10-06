# Вам даны массив строк words и массив строк chars.
# Строка считается хорошей, если она может быть составлена ​​из символов массива chars (каждый символ может быть использован только один раз для каждого слова в массиве words).
# Верните сумму длин всех «хороших» строк из списка слов.
from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        result: int = 0

        count_chars = Counter(chars)
        for word in words:
            count_word = Counter(word)
            flag = True
            for k, v in count_word.items():
                if v <= count_chars[k]:
                    pass
                else:
                    flag = False
                    break
            
            if flag:
                result += len(word)

        return result

example = Solution()

words = ["cat","bt","hat","tree"]
chars = "atach"
result1 = example.countCharacters(words, chars)
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
assert result1 == 6
print( "result1", result1)
