# Дана строка s, состоящая из строчных или прописных букв. Верните длину самой длинной строки, которая может быть построена из этих букв.
# Регистр букв имеет значение; например, "Aa" не считается палиндромом.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0
        
        for char in s:
            if char in seen:
                seen.remove(char)
                length += 2
            else:
                seen.add(char)
                
        # Если остались unmatched символы, один из них можно поставить в центр
        return length + 1 if seen else length
    
example =Solution()

s = "abccccdd"
result1 = example.longestPalindrome(s)
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
assert result1 == 7
print( "result1", result1)

s = "a"
result2 = example.longestPalindrome(s)
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
assert result2 == 1
print( "result2", result2)