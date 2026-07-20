# Предложение — это последовательность слов, разделённых одним пробелом, где каждое слово состоит только из строчных букв.
# Слово считается редким, если оно встречается ровно один раз в одном из предложений и не встречается в другом.
# Даны два предложения s1 и s2. Верните список всех редких слов. Вы можете вернуть ответ в любом порядке.
from typing  import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon: list = []

        s1_list = s1.split()
        s2_list = s2.split()

        common_list = s1_list + s2_list
        counting = Counter(common_list)

        for key, value in counting.items():
            if value == 1:
                uncommon.append(key)

        return uncommon
    
example =Solution()

s1 = "this apple is sweet"
s2 = "this apple is sour"
result1 = example.uncommonFromSentences(s1, s2)
# Explanation: The word "sweet" appears only in s1, while the word "sour" appears only in s2.
assert result1 == ["sweet","sour"]
print( "result1", result1)

s1 = "apple apple"
s2 = "banana"
result2 = example.uncommonFromSentences(s1, s2)
assert result2 == ["banana"]
print( "result2", result2)