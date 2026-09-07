# Дана строка s. Необходимо перевернуть её в соответствии со следующими правилами:
# Все символы, кроме английских букв, остаются на своих местах.
# Все английские буквы (строчные и прописные) должны быть перевернуты.
# Верните строку s после переворачивания.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            # Двигаем left вперёд, пока символ не буква
            while left < right and not chars[left].isalpha():
                left += 1
            # Двигаем right назад, пока символ не буква
            while left < right and not chars[right].isalpha():
                right -= 1

            # Меняем буквы местами
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)

example = Solution()
    
s = "ab-cd"
result1 = example.reverseOnlyLetters(s)
assert result1 == "dc-ba"
print( "result1", result1)

s = "a-bC-dEf-ghIj"
result2 = example.reverseOnlyLetters(s)
assert result2 == "j-Ih-gfE-dCba"
print( "result2", result2)

s = "Test1ng-Leet=code-Q!"
result3 = example.reverseOnlyLetters(s)
assert result3 == "Qedo1ct-eeLg=ntse-T!"
print( "result3", result3)