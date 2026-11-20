# Дана строка s и символ c, который присутствует в строке s. 
# Необходимо вернуть массив целых чисел answer, где длина массива равна длине строки s, а элемент answer[i] представляет собой расстояние от индекса i до ближайшего вхождения символа c в строку s.
# Расстояние между двумя индексами i и j определяется как abs(i - j), где abs — функция взятия абсолютного значения.

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        result: list[int] = []

        indices = [i for i, ch in enumerate(s) if ch == c]
        print(indices)

        for char in range(len(s)):
            distance = 1000
            for index in indices:
                r = abs(index - char)
                if r < distance:
                    distance = r

            result.append(distance)

        return result
    
example = Solution()

s = "loveleetcode"
c = "e"
result1 = example.shortestToChar(s, c)
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
print( "result1", result1)
assert result1 == [3,2,1,0,1,0,0,1,2,2,1,0]