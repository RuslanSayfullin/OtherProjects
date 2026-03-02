"""
    Дано положительное целое число num. Верните количество положительных целых чисел, меньших или равных num, суммы цифр которых четные.
    Сумма цифр положительного целого числа равна сумме всех его цифр.
"""


class Solution:
    def countEven(self, num: int) -> int:
        result = 0
        for i in range(1, num + 1):
            is_sum_even = sum(int(symbol) for symbol in str(i)) % 2 == 0
            print(i, sum(int(symbol) for symbol in str(i)))
            if is_sum_even:
                result += 1
            
        return result

#num = 4
#example = Solution()
#result1 = example.countEven(num)
#print(result1)
# Единственными целыми числами меньше или равными 4, у которых сумма цифр четная, являются 2 и 4.

num = 30
example = Solution()
result2 = example.countEven(num)
print(result2)
# Четырнадцать целых чисел, меньших или равных 30, суммы цифр которых четные, это: 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26 и 28.