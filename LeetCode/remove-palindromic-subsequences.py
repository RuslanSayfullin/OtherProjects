# Дана строка s, состоящая только из символов «a» и «b». За один шаг можно удалить из s одну палиндромную подпоследовательность.
# Верните минимальное количество шагов, необходимое для того, чтобы сделать строку пустой.
# Строка является подпоследовательностью данной строки, если она получена путем удаления некоторых символов из исходной строки без изменения их порядка. 
# Заметьте, что символы подпоследовательности не обязательно должны идти в исходной строке подряд.
# Строка называется палиндромом, если она читается одинаково в обоих направлениях (слева направо и справа налево).

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2

example = Solution()
    
s = "ababa"
result1 = example.removePalindromeSub(s)
# Explanation: s is already a palindrome, so its entirety can be removed in a single step.
assert result1 == 1
print( "result1", result1)

s = "abb"
result2 = example.removePalindromeSub(s)
# Explanation: "abb" -> "bb" -> "". Remove palindromic subsequence "a" then "bb".
assert result2 == 2
print( "result2", result2)

s = "baabb"
result3 = example.removePalindromeSub(s)
# Explanation: "baabb" -> "b" -> "". Remove palindromic subsequence "baab" then "b".
assert result3 == 2
print( "result3", result3)