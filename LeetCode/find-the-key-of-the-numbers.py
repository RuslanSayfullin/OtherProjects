# Даны три положительных целых числа: num1, num2 и num3.
# Ключ для чисел num1, num2 и num3 определяется как четырехзначное число, сформированное следующим образом:
# Если какое-либо из чисел содержит менее четырех цифр, оно дополняется ведущими нулями. 
# i-я цифра ключа (где 1 ≤ i ≤ 4) получается путем выбора наименьшей из i-х цифр чисел num1, num2 и num3.
# Верните ключ для этих трех чисел, исключив ведущие нули (если они есть).

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Преобразуем числа в строки и дополняем ведущими нулями до длины 4
        s1 = f"{num1:04d}"
        s2 = f"{num2:04d}"
        s3 = f"{num3:04d}"

        # Собираем ключ посимвольно: на каждой позиции берём минимальную цифру
        key_digits = []
        for i in range(4):
            d1 = s1[i]
            d2 = s2[i]
            d3 = s3[i]
            min_digit = min(d1, d2, d3)  # сравнение символов корректно для цифр
            key_digits.append(min_digit)

        key_str = "".join(key_digits)
        # Преобразование в int убирает ведущие нули
        return int(key_str)


example = Solution()

num1 = 1
num2 = 10
num3 = 1000
result1 = example.generateKey(num1, num2, num3)
# Explanation: On padding, num1 becomes "0001", num2 becomes "0010", and num3 remains "1000".
# The 1st digit of the key is min(0, 0, 1).
# The 2nd digit of the key is min(0, 0, 0).
# The 3rd digit of the key is min(0, 1, 0).
# The 4th digit of the key is min(1, 0, 0).
# Hence, the key is "0000", i.e. 0
assert result1 == 0
print( "result1", result1)

num1 = 987
num2 = 879
num3 = 798
result2 = example.generateKey(num1, num2, num3)
assert result2 == 777
print( "result2", result2)

num1 = 1
num2 = 2
num3 = 3
result3 = example.generateKey(num1, num2, num3)
assert result3 == 1
print( "result3", result3)