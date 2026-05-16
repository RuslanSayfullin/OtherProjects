# Дано целое число num. Необходимо многократно складывать все его цифры до тех пор, 
# пока результат не будет состоять только из одной цифры, после чего вернуть результат.

class Solution:
    def addDigits(self, num: int) -> int:
        digit = 0

        numstr = str(num)
        numstrlen= len(numstr)
        if numstrlen < 2:
            digit = num
        else:
            while numstrlen > 1:
                digit = 0
                for i in range(numstrlen):
                    digit += int(numstr[i])
                    print(digit)

                numstr = str(digit)
                numstrlen= len(numstr)

        return digit

num = 38
example = Solution()
result1 = example.addDigits(num)
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
assert result1 == 2
print( "result1", result1)

num = 0
example = Solution()
result2 = example.addDigits(num)
assert result2 == 0
print(result2)
