# Дан массив строковых слов. Верните первую палиндромную строку в массиве. Если такой строки нет, верните пустую строку "".
# Строка называется палиндромной, если она читается одинаково как в прямом, так и в обратном направлении.
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        first_palindrome: str = ""
        for word in words:
            if word == word[::-1]:
                first_palindrome = word
                break

        return first_palindrome

example = Solution()
    
words = ["abc","car","ada","racecar","cool"]
result1 = example.firstPalindrome(words)
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
assert result1 == "ada"
print( "result1", result1)

words = ["notapalindrome","racecar"]
result2 = example.firstPalindrome(words)
# Explanation: The first and only string that is palindromic is "racecar".
assert result2 == "racecar"
print( "result2", result2)

words = ["def","ghi"]
result3 = example.firstPalindrome(words)
# Explanation: There are no palindromic strings, so the empty string is returned.
assert result3 == ""
print( "result3", result3)