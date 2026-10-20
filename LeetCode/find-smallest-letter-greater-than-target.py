# Дан массив символов `letters`, отсортированный в неубывающем порядке, и символ `target`. В массиве `letters` присутствует как минимум два различных символа.
# Необходимо вернуть наименьший символ из массива `letters`, который в лексикографическом порядке больше символа `target`. 
# Если такого символа не существует, следует вернуть первый символ из массива `letters`.
import string

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        result: str = ""
        flag: bool = False

        alphabet = string.ascii_lowercase
        index = alphabet.find(target)
        for s in range(index+1, len(alphabet)):

            if alphabet[s] in letters:
                result = result + alphabet[s]
                flag = True
                break
        
        if not flag:
            result = result + letters[0]

        return result

example = Solution()
    
letters = ["c","f","j"]
target = "a"
result1 = example.nextGreatestLetter(letters, target)
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
assert result1 == "c"
print( "result1", result1)