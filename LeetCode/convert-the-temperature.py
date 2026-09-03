# Вам дано неотрицательное число с плавающей запятой, округленное до двух десятичных знаков в градусах Цельсия, 
# обозначающее температуру в градусах Цельсия.
# Вы должны перевести градусы Цельсия в кельвины и фаренгейты и вернуть их в виде массива ans = [kelvin, fahrenheit].
# Верните массив ans. Принимаются ответы, отличающиеся от правильного ответа на 10-5 градусов.
# Обратите внимание:
# Кельвин = Цельсий + 273,15
# Фаренгейт = Цельсий * 1,80 + 32,00

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        result: list = []

        kelvin: float = celsius + 273.15
        result.append(kelvin)
        fahrenheit: float = celsius * 1.8 + 32.00
        result.append(fahrenheit)
        return result
    
example = Solution()
    
celsius = 36.50
result1 = example.convertTemperature(celsius)
assert result1 == [309.65000,97.70000]
# Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
print( "result1", result1)


celsius = 122.11
result2 = example.convertTemperature(celsius)
assert result2 == [395.26000,251.79800]
# Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
print( "result2", result2)