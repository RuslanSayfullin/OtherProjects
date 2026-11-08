# Дана строка s; необходимо поменять местами только гласные буквы в этой строке и вернуть полученный результат.
# К гласным относятся «a», «e», «i», «o» и «u»; они могут встречаться как в нижнем, так и в верхнем регистре, 
# причём каждая из них может появляться в строке неоднократно.
from collections import OrderedDict

class Solution:
    def reverseVowels(self, s: str) -> str:
        result: str = ""

        vowels = "aeiouAEIOU"
        vowels_index = {}

        for symbol in range(len(s)):
            
            if s[symbol] in vowels:
                vowels_index[symbol] = s[symbol]
        

        od_index = OrderedDict(vowels_index)
        for symbol in s:
            if symbol in vowels:
                result = result + (od_index.popitem(last=True))[1]
            else:
                result = result + symbol

        return result

example = Solution()

s = "IceCreAm"
result1 = example.reverseVowels(s)
# Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
assert result1 ==  "AceCreIm"
print( "result1", result1)

s = "leetcode"
result2 = example.reverseVowels(s)
assert result2 ==  "leotcede"
print( "result2", result2)