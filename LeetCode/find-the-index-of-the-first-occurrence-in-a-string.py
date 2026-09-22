# Даны две строки: needle и haystack. 
# Верните индекс первого вхождения строки needle в строку haystack или -1, если needle не содержится в haystack.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result: int = -1

        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:(i+len(needle))] == needle:
                    result = i
                    break

        return result

example = Solution()

haystack = "sadbutsad"
needle = "sad"
result1 = example.strStr(haystack, needle)
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
print( "result1", result1)
assert result1 == 0

haystack = "a"
needle = "a"
result2 = example.strStr(haystack, needle)
print( "result2", result2)
assert result2 == 0