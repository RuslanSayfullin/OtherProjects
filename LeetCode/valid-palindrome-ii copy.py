# Если задана строка s, вернуть true, если строка s может стать палиндромом после удаления из неё не более одного символа.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        valid_palindrome: bool = False


        for k in range(len(s)):
            #print(s[k])

            res_str = s[:k] + s[k+1:]

            rev_str = res_str[::-1]
            if res_str == rev_str:
                
                valid_palindrome = True
                return valid_palindrome

        return valid_palindrome
    

example =Solution()

s = "aba"
result1 = example.validPalindrome(s)
assert result1 == True
print( "result1", result1)

s = "abca"
result2 = example.validPalindrome(s)
# Explanation: You could delete the character 'c'.
assert result2 == True
print( "result2", result2)

s = "abc"
result3 = example.validPalindrome(s)
assert result3 == False
print( "result3", result3)

s = "bddb"
result4 = example.validPalindrome(s)
assert result4 == True
print( "result4", result4)

s = "aydmda"
result5 = example.validPalindrome(s)
assert result5 == True
print( "result5", result5)

s = "eeccccbebaeeabebccceea"
result6 = example.validPalindrome(s)
assert result6 == False
print( "result6", result6)

s = "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"
result7 = example.validPalindrome(s)
assert result7 == False
print( "result7", result7)

s = "bebeb"
result8 = example.validPalindrome(s)
#assert result8 == True
print( "result8", result8)