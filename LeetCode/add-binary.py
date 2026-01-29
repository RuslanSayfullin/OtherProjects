

# Даны две двоичные строки a и b. Верните их сумму в виде двоичной строки.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Переводим двоичные строки в десятичные числа
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # Складываем и переводим обратно в двоичную строку
        result = bin(num1 + num2)
        
        # Убираем префикс '0b'
        return result[2:]


a = "11"
b = "1"
example = Solution()
result1 = example.addBinary(a, b)
print(result1)

a = "1010"
b = "1011"
result2 = example.addBinary(a, b)
print(result2)
