# Дано целое число n(в десятичной системе счисления) и основание системы счисления k. 
# Требуется найти сумму цифр числа n после его перевода из десятичной системы в систему счисления с основанием k.
# После перевода каждая цифра рассматривается как десятичное число, а итоговая сумма также возвращается в десятичной системе счисления.
import string

def convert_base(num, base):
    if num == 0:
        return '0'

    alphabet = string.digits + string.ascii_lowercase
    res = ''
    while num > 0:
        res = alphabet[num % base] + res
        num //= base
    return res
    
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result: int = 0

        ci = convert_base(n, k)
        strci = str(ci)
        for s in strci:
            result += int(s)

        return result

example = Solution()

n = 34
k = 6
result1 = example.sumBase(n, k)
# Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
assert result1 == 9
print( "result1", result1)