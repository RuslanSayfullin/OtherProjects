# Вам дана строка allowed, состоящая из различных символов, и массив строк words. 
# Строка считается согласованной, если все символы в ней встречаются в строке allowed.
# Верните количество согласованных строк в массиве words.
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result: int = 0
        flag: bool = True

        for word in words:
            for symbol in word:
                if symbol in allowed:
                    pass
                else:
                    flag = False

            if flag:
                result += 1

            flag = True

        # print(result)
        return result

example = Solution()

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
result1 = example.countConsistentStrings(allowed, words)
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
assert result1 == 2
print( "result1", result1)

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
result2 = example.countConsistentStrings(allowed, words)
# Explanation: All strings are consistent.
assert result2 == 7
print( "result2", result2)

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
result3 = example.countConsistentStrings(allowed, words)
assert result3 == 4
print( "result3", result3)

