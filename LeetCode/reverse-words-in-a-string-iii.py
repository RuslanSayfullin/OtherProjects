# Дана строка s. Необходимо изменить порядок символов в каждом слове предложения на обратный, сохранив при этом пробелы и исходный порядок слов.

class Solution:
    def reverseWords(self, s: str) -> str:
        reversed: str = ""

        s_list = s.split()
        
        for slovo in s_list:
            reversed += slovo[::-1] + " "

        reversed = reversed[0:len(reversed)-1]
        #print(reversed)
        return reversed

example = Solution()

s = "Let's take LeetCode contest"
result1 = example.reverseWords(s)
assert result1 == "s'teL ekat edoCteeL tsetnoc"
print( "result1", result1)

s = "Mr Ding"
result2 = example.reverseWords(s)
assert result2 == "rM gniD"
print( "result2", result2)
