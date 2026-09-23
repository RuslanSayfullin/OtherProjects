# Дан массив строк `words` и строка `pref`.
# Верните количество строк в массиве `words`, которые начинаются со строки `pref` (то есть для которых `pref` является префиксом).

# Префикс строки `s` — это любая начальная непрерывная подстрока строки `s`

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        result: int = 0

        for word in words:
            if word.startswith(pref):
                result += 1

        return result

example = Solution()

words = ["pay","attention","practice","attend"]
pref = "at"
result1 = example.prefixCount(words, pref)
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
print( "result1", result1)
assert result1 == 2

words = ["leetcode","win","loops","success"]
pref = "code"
result2 = example.prefixCount(words, pref)
# Explanation: There are no strings that contain "code" as a prefix.
print( "result2", result2)
assert result2 == 0