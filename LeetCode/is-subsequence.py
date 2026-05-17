# Даны две строки s и t. Верните true, если s является подпоследовательностью t, или false в противном случае.
# Подпоследовательность строки — это новая строка, образованная из исходной строки путем удаления некоторых (может не удалять) символов
# без изменения относительного положения оставшихся символов. (например, "ace" является подпоследовательностью "abcde", а "aec" — нет).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        isSubsequence = False

        if s in t:
          isSubsequence = True
        else:
            string = ""
            for symbol in s:
                
                if symbol in t:
                    string += symbol
                    
                    t = t[t.index(symbol)+1:]

            if string == s:
                isSubsequence = True

        return isSubsequence
    

s = "abc"
t = "ahbgdc"
example = Solution()
result1 = example.isSubsequence(s, t)
print( "result1", result1)

s = "axc"
t = "ahbgdc"
example = Solution()
result2 = example.isSubsequence(s, t)
print( "result1", result2)