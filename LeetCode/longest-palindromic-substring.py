# Дана строка s. Верните самую длинную полиндромную строку в этой строке.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]


        longest = ""
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring
        return longest



example = Solution()

s = "babad"
result1 = example.longestPalindrome(s)
# Explanation: "aba" is also a valid answer.
assert result1 == "bab"
print( "result1", result1)

s = "cbbd"
result2 = example.longestPalindrome(s)
#assert result2 == "bb"
print( "result2", result2)

