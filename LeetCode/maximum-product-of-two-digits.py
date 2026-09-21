# Дано целое положительное число n.
# Верните максимальное произведение любых двух цифр числа n.
# Примечание: можно использовать одну и ту же цифру дважды, если она встречается в числе n более одного раза.

class Solution:
    def maxProduct(self, n: int) -> int:
        result: int = 0

        int_list = list(str(n))

        for symbol in range(len(int_list)):
            int_list[symbol] = int(int_list[symbol])

        int_list.sort(reverse=True)

        result = int_list[0] * int_list[1]

        return result

example = Solution()

n = 31
result1 = example.maxProduct(n)
# Explanation: 
# The digits of n are [3, 1].
# The possible products of any two digits are: 3 * 1 = 3.
# The maximum product is 3.
print( "result1", result1)
assert result1 == 3

n = 22
result2 = example.maxProduct(n)
# Explanation: 
# The digits of n are [2, 2].
# The possible products of any two digits are: 2 * 2 = 4.
# The maximum product is 4.
print( "result2", result2)
assert result2 == 4

n = 124
result3 = example.maxProduct(n)
# Explanation: 
# The digits of n are [1, 2, 4].
# The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
# The maximum product is 8.
print( "result3", result3)
assert result3 == 8