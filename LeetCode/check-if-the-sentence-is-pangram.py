# Панграмма — это предложение, в котором каждая буква английского алфавита встречается хотя бы один раз.
# Дана строка `sentence`, содержащая только строчные буквы английского алфавита. Верните `true`, если `sentence` является панграммой, и `false` в противном случае.
import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        result: bool = True

        s = string.ascii_lowercase

        for symbol in s:
            if symbol in sentence:
                pass
            else:
                result = False
                break

        return result

example = Solution()

sentence = "thequickbrownfoxjumpsoverthelazydog"
result1 = example.checkIfPangram(sentence)
# Explanation: sentence contains at least one of every letter of the English alphabet.
assert result1
print( "result1", result1)

sentence = "leetcode"
result2 = example.checkIfPangram(sentence)
assert not result2
print( "result2", result2)