# Если задана строка s, вернуть true, если строка s может стать палиндромом после удаления из неё не более одного символа.
from collections import Counter

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # При первом расхождении пробуем пропустить left или right
                # or вычисляется лениво: если первый вариант True, второй не запустится
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1
            
        return True  # Строка уже палиндром (0 удалений)

example =Solution()

s = "aba"
result1 = example.validPalindrome(s)
assert result1 == True
print( "result1", result1)

s = "abca"
result2 = example.validPalindrome(s)
# Explanation: You could delete the character 'c'.
assert result2 == True
print( "result2", result2)

s = "abc"
result3 = example.validPalindrome(s)
assert result3 == False
print( "result3", result3)

s = "bddb"
result4 = example.validPalindrome(s)
assert result4 == True
print( "result4", result4)

s = "aydmda"
result5 = example.validPalindrome(s)
assert result5 == True
print( "result5", result5)

s = "eeccccbebaeeabebccceea"
result6 = example.validPalindrome(s)
#assert result6 == False
print( "result6", result6)