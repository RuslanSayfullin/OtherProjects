# Дан массив строковых слов. 
# Верните все строки в массиве words, которые являются подстрокой другого слова. Вы можете вернуть ответ в любом порядке.
from copy import deepcopy
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring: list[str] = []

        for word in words:
            new_list = deepcopy(words)
            new_list.pop(words.index(word))
            new_list.insert(0, word)

            for index in range(1, len(new_list)):
                if new_list[0] in new_list[index]:
                    
                    substring.append(new_list[0])
                    break

        return substring

example = Solution()
    
words = ["mass","as","hero","superhero"]
result1 = example.stringMatching(words)
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero". ["hero","as"] is also a valid answer.
assert result1 == ["as","hero"]
print( "result1", result1)

words = ["leetcode","et","code"]
result2 = example.stringMatching(words)
# Explanation: "et", "code" are substring of "leetcode".
assert result2 == ["et","code"]
print( "result2", result2)

words = ["blue","green","bu"]
result3 = example.stringMatching(words)
# Explanation: No string of words is substring of another string.
assert result3 == []
print( "result3", result3)