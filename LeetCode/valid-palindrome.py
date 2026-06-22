# Фраза является палиндромом, если после преобразования всех заглавных букв в строчные и удаления всех небуквенно-цифровых символов она читается одинаково как в прямом, 
# так и в обратном порядке. Буквенно-цифровые символы включают буквы и цифры.
# Полученная строка s должна возвращать true, если она является палиндромом, или false в противном случае.
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome: bool = False

        new_string = s.lower()
        new_string = new_string.replace(" ", "")
        
        for p in string.punctuation:
            if p in new_string:
                # банальная замена символа в строке
                new_string = new_string.replace(p, '')

        if new_string == new_string[::-1]:
            is_palindrome = True

        return is_palindrome
    
example = Solution()
    
s = "A man, a plan, a canal: Panama"
result1 = example.isPalindrome(s)
# Explanation: "amanaplanacanalpanama" is a palindrome.
assert result1
print( "result1", result1)

s = "race a car"
result2 = example.isPalindrome(s)
# Explanation: "raceacar" is not a palindrome.
assert not result2
print( "result2", result2)

s = " "
result3 = example.isPalindrome(s)
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
assert result3
print( "result3", result3)


