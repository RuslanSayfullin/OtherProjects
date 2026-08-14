# Дан массив целых чисел arr. Замените каждый элемент его рангом.
# Ранг обозначает размер элемента. К рангу применяются следующие правила:
# Ранг — целое число, начиная с 1.
# Чем больше элемент, тем больше ранг. Если два элемента равны, их ранги должны быть одинаковыми.
# Ранг должен быть как можно меньше.
import copy

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        result: list[int] = []

        new_arr = copy.deepcopy(arr)
        new_arr = list(set(new_arr))
        new_arr.sort()

        enum_set_arr = {integer: i for integer, i in enumerate(new_arr, start=1)}

        for element in arr:
            for key, value in enum_set_arr.items():
                if element == value:
                    result.append(key)

        return result
    

example = Solution()

arr = [40,10,20,30]
result1 = example.arrayRankTransform(arr)
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
assert result1 == [4,1,2,3]
print( "result1", result1)

arr = [100,100,100]
result2 = example.arrayRankTransform(arr)
# Explanation: Same elements share the same rank.
assert result2 == [1,1,1]
print( "result2", result2)

arr = [37,12,28,9,100,56,80,5,12]
result3 = example.arrayRankTransform(arr)
assert result3 == [5,3,4,2,8,6,7,1,3]
print( "result3", result3)


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:


        # 1. Создаем отсортированную копию уникальных элементов
        sorted_unique = sorted(set(arr))
        
        # 2. Создаем словарь: значение -> его ранг (индекс + 1)
        rank_map = {value: i + 1 for i, value in enumerate(sorted_unique)}
        
        # 3. Заменяем каждый элемент в исходном массиве на его ранг
        return [rank_map[x] for x in arr]