# Вам дана строка, представляющая собой положительное целое число, и символьная цифра.
# Верните результирующую строку после удаления ровно одного вхождения цифры из числа таким образом,
# чтобы значение результирующей строки в десятичной форме было максимальным. 
# Тестовые примеры генерируются таким образом, чтобы цифра встречалась в числе хотя бы один раз.
from collections import Counter

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        result: str = ""

        count_result = Counter(number)

        if count_result[digit] == 1:
            # если у нас только одно вхождение
            index = number.index(digit)
            result = number[:index] + number[index+1:]
        elif count_result[digit] > 1:
            max_number = 0
            for i in range(len(number)):
                if number[i] == digit:
                    var = number[:i] + number[i+1:]
                    if int(var) > max_number:
                        max_number = int(var)

            result = str(max_number)

        else:
            # если нет вхождения цивфры в число
            return result

        return result

example = Solution()

number = "123"
digit = "3"
result1 = example.removeDigit(number, digit)
# Explanation: There is only one '3' in "123". After removing '3', the result is "12".
assert result1 == "12"
print( "result1", result1)

number = "1231"
digit = "1"
result2 = example.removeDigit(number, digit)
# We can remove the first '1' to get "231" or remove the second '1' to get "123".
# Since 231 > 123, we return "231".
assert result2 == "231"
print( "result2", result2)

number = "551"
digit = "5"
result3 = example.removeDigit(number, digit)
# We can remove either the first or second '5' from "551".
# Both result in the string "51".
assert result3 == "51"
print( "result3", result3)