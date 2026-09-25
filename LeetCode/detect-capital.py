# Использование заглавных букв в слове считается правильным, если выполняется одно из следующих условий:
# Все буквы в слове — заглавные (например, «USA»). 
# Все буквы в слове — строчные (например, «leetcode»). 
# Только первая буква — заглавная (например, «Google»).
# Дана строка `word`; верните `true`, если использование заглавных букв в ней правильное.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital: bool = True

        if len(word) > 1:
            if word[0].isupper() and not word[1].isupper():
                if len(word) > 2:
                    for i in range(2, len(word)):
                        if word[i].isupper():
                            capital = False
                            break
            elif word[0].isupper() and word[1].isupper():
                if len(word) > 2:
                    for i in range(2, len(word)):
                        if not word[i].isupper():
                            capital = False
                            break
            elif not word[0].isupper() and not word[1].isupper():
                if len(word) > 2:
                    for i in range(2, len(word)):
                        if word[i].isupper():
                            capital = False
                            break
            else:
                capital = False

        return capital

    
example = Solution()

word = "USA"
result1 = example.detectCapitalUse(word)
print( "result1", result1)
assert result1

word = "FlaG"
result2 = example.detectCapitalUse(word)
print( "result2", result2)
assert not result2