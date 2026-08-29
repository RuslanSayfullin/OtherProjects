# Вам дана двоичная строка s, содержащая как минимум одну «1».
# Вы должны переставить биты таким образом, чтобы полученное двоичное число было максимальным нечётным двоичным числом, которое можно составить из данной комбинации.
# Верните строку, представляющую максимальное нечётное двоичное число, которое можно составить из данной комбинации.
# Обратите внимание, что полученная строка может содержать ведущие нули.

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        result: str = ""

        if len(s) == 1:
            return s
        else:
            #print(s.count("1"))
            edinisa: int = s.count("1")
            for i in range(len(s) - 1):
                if edinisa > 1:
                    result = result + "1"
                    edinisa -= 1
                else:
                    result = result + "0"
                 
        result = result + "1"   # единица в конце для "нечеиности числа"
        #print(result)   
        return result
    
example = Solution()
    
s = "010"
result1 = example.maximumOddBinaryNumber(s)
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
assert result1 == "001"
print( "result1", result1)

s = "0101"
result2 = example.maximumOddBinaryNumber(s)
# Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
assert result2 == "1001"
print( "result2", result2)