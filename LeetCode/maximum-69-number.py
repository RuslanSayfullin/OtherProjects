# Вам дано положительное целое число, состоящее только из цифр 6 и 9.
# Верните максимальное число, которое можно получить, изменив не более одной цифры (6 становится 9, а 9 становится 6).


class Solution:
    def maximum69Number(self, num: int) -> int:
        maximum: int = 0

        str_num = str(num)
        if '6' in str_num:
            index6 = str_num.index('6')
            str_num = str_num[0:index6] + "9" + str_num[index6 + 1:]
            #print(str_num)
            maximum = int(str_num)
        else:
            maximum = num

        return maximum


example = Solution()

num = 9669
result1 = example.maximum69Number(num)
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
assert result1 == 9969
print( "result1", result1)

num = 9996
result2 = example.maximum69Number(num)
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
assert result2 == 9999
print( "result2", result2)

num = 9999
result3 = example.maximum69Number(num)
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
assert result3 == 9999
print( "result3", result3)

num = 99
result4 = example.maximum69Number(num)
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
assert result4 == 99
print( "result4", result4)