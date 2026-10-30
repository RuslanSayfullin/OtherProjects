# Даны массив строк `words` и бинарный массив `groups`, оба длиной `n`.
# Последовательность строк называется «чередующейся», 
# если для любых двух соседних строк в этой последовательности соответствующие им элементы в массиве `groups` различаются 
# (то есть в `groups` не могут идти подряд одинаковые значения — 0 или 1).
# Ваша задача — выбрать самую длинную чередующуюся подпоследовательность из `words`.
# Верните выбранную подпоследовательность. Если существует несколько подходящих вариантов, верните любой из них.
# Примечание: все элементы в массиве `words` уникальны.

class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        if not words or not groups:
            return []

        result = [words[0]]
        last_group = groups[0]

        for i in range(1, len(words)):
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]

        return result


example = Solution()

words = ["e","a","b"]
groups = [0,0,1]
result1 = example.getLongestSubsequence(words, groups)
# Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. 
# Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. 
# It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.
assert result1 == ["e","b"]
print( "result1", result1)