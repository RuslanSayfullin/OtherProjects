# Дан строковый массив words. Верните массив всех символов, встречающихся во всех строках этого массива words (включая дубликаты). 
# Вы можете вернуть ответ в любом порядке.
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Начинаем с частот первой строки
        common_count = Counter(words[0])
        
        # Для каждой следующей строки обновляем общие частоты (берём минимум)
        for word in words[1:]:
            word_count = Counter(word)
            # Оставляем только пересечение с учётом количества
            for char in common_count:
                common_count[char] = min(common_count[char], word_count.get(char, 0))
        
        # Превращаем частоты обратно в список символов
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result


example =Solution()

words = ["bella","label","roller"]
result1 = example.commonChars(words)
assert result1 == ["e","l","l"]
print( "result1", result1)

words = ["cool","lock","cook"]
result2 = example.commonChars(words)
assert result2 == ["c","o"]
print( "result2", result2)

words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
result3 = example.commonChars(words)
assert result3 == ["b","d","d"]
print( "result3", result3)