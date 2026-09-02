# Дано 32-битное знаковое целое число x. Верните x с перевернутыми цифрами. 
# Если переворачивание x приводит к выходу значения за пределы диапазона 32-битных знаковых целых чисел [-2**31, 2**31 - 1], верните 0.
# Предположим, что среда выполнения не позволяет хранить 64-битные целые числа (знаковые или беззнаковые).

class Solution:
    def reverse(self, x: int) -> int:
        result: int | str = ""

        str_x: str = str(x)

        if x < 0:
            result = result + "-"
            for symbol in range(len(str_x)-1, 0, -1):
                result = result + str_x[symbol]
        else:
            for symbol in range(len(str_x)-1, -1, -1):
                print(symbol, str_x[symbol])
                result = result + str_x[symbol]

        #print(result)
        result = int(result)

        if -2147483648 < result < 2147483647:
            return result
        else:
            return 0

example = Solution()
    
x = 123
result1 = example.reverse(x)
assert result1 == 321
print( "result1", result1)

x = -123
result2 = example.reverse(x)
assert result2 == -321
print( "result2", result2)

x = 120
result3 = example.reverse(x)
assert result3 == 21
print( "result3", result3)
