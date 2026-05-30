# Дана строка s. Найдите длину самой длинной строки без повторяющихся символов.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringlen: int = 0
        result_string = ""

        while len(s) != 0:
            for i in s:
                if i not in result_string:
                    result_string +=i
                    #print(result_string)
                else:
                    if len(result_string) > substringlen:
                        substringlen = len(result_string)
                    s = s[1:]
                    result_string = ""
                    #print(s, len(s))
                    break
                

         
        return substringlen


example = Solution()

s = "abcabcbb"
result1 = example.lengthOfLongestSubstring(s)
# The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
#assert result1 == 3
print( "result1", result1)

s = "bbbbb"
result2 = example.lengthOfLongestSubstring(s)
# Explanation: The answer is "b", with the length of 1."
#assert result2 == 1
print( "result2", result2)

s = "pwwkew"
result3 = example.lengthOfLongestSubstring(s)
# The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#assert result3 == 3
print( "result3", result3)
