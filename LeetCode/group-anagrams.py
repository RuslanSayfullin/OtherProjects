# Дан массив строк `strs`; сгруппируйте анаграммы. Ответ можно вернуть в любом порядке.
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
    
        for s in strs:
            # Сортируем символы строки и используем как ключ
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
    
example = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
result1 = example.groupAnagrams(strs)
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
assert result1 == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print( "result1", result1)

strs = ["",""]
result2 = example.groupAnagrams(strs)
assert result2 == [["",""]]
print( "result2", result2)

strs = ["c","c"]
result3 = example.groupAnagrams(strs)
assert result3 == [["c","c"]]
print( "result3", result3)