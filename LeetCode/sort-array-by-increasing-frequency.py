# Дан массив целых чисел nums. Отсортируйте массив в порядке возрастания частоты встречаемости значений. 
# Если несколько значений имеют одинаковую частоту, отсортируйте их в порядке убывания.
# Верните отсортированный массив.
from collections import Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        result: list[int] = []

        frequency = Counter(nums)

        # 1. Сортируем по ключу по убыванию
        step1 = sorted(frequency.items(), key=lambda x: x[0], reverse=True)
        # 2. Потом по значению по возрастанию (устойчивая сортировка сохранит порядок ключей внутри одинаковых значений)
        soreted_frequency = sorted(step1, key=lambda x: x[1])

        #print(soreted_frequency)

        for element in soreted_frequency:
            for i in range(element[1]):
                result.append(element[0])
        #print(result)
        return result


example = Solution()

nums = [1,1,2,2,2,3]
result1 = example.frequencySort(nums)
assert result1 == [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
print("result1", result1)

nums = [2,3,1,3,2]
result2 = example.frequencySort(nums)
assert result2 == [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
print("result2", result2)



        