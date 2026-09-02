
# Дано целое число num. Верните количество цифр в num, которые делят num на 0.
# Целое число val делит num на 0, если num % val == 0.

class Solution:
    def countDigits(self, num: int) -> int:
        result: int = 0

        str_num: str = str(num)

        for val in str_num:
            if num % int(val) == 0:
                result += 1
        #print(result)
        return result

example = Solution()
    
num = 7
result1 = example.countDigits(num)
assert result1 == 1
# Explanation: 7 divides itself, hence the answer is 1.
print( "result1", result1)

num =121
result2 = example.countDigits(num)
assert result2 == 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
print( "result2", result2)

num =1248
result3 = example.countDigits(num)
assert result3 == 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
print( "result3", result3)
