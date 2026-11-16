# Мощность строки — это максимальная длина непустой подстроки, состоящей только из одного уникального символа.
# Дана строка s; верните мощность строки s.

class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        
        max_len = 1
        current_len = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_len += 1
            else:
                current_len = 1
            
            if current_len > max_len:
                max_len = current_len
        
        return max_len

example = Solution()

s = "leetcode"
result1 = example.maxPower(s)
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
print( "result1", result1)
assert result1 == 2

s = "abbcccddddeeeeedcba"
result2 = example.maxPower(s)
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
print( "result2", result2)
assert result2 == 5

