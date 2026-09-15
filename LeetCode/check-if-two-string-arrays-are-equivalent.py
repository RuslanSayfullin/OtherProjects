# Даны два массива строк — `word1` и `word2`. 
# Верните `true`, если эти массивы представляют собой одну и ту же строку, и `false` в противном случае.
# Массив представляет строку, если при объединении его элементов в порядке их следования образуется эта строка.

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        result: bool = False

        string1 = ""
        string2 = ""

        for s in word1:
            string1 = string1 + s

        for s in word2:
            string2 = string2 + s

        if string1 == string2:
            result = True
        

        return result

example = Solution()

word1 = ["ab", "c"]
word2 = ["a", "bc"]
result1 = example.arrayStringsAreEqual(word1, word2)
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
assert result1 == True
print(result1)

word1 = ["a", "cb"]
word2 = ["ab", "c"]
result2 = example.arrayStringsAreEqual(word1, word2)
assert result2 == False
print(result2)