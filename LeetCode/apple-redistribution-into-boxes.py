# Дан массив `apple` размера `n` и массив `capacity` размера `m`.
# Имеется `n` упаковок, причём `i`-я упаковка содержит `apple[i]` яблок.
# Также есть `m` коробок, где `i`-я коробка вмещает `capacity[i]` яблок.
# Необходимо найти минимальное количество коробок, которое потребуется для размещения всех `n` упаковок яблок.
# Обратите внимание: яблоки из одной упаковки можно распределять по разным коробкам.

class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total_apples = sum(apple)
        
        # Сортируем коробки по вместимости от большей к меньшей
        capacity.sort(reverse=True)
        
        current_capacity = 0
        boxes_used = 0
        
        for cap in capacity:
            current_capacity += cap
            boxes_used += 1
            if current_capacity >= total_apples:
                return boxes_used
        
        # Если не хватило всех коробок
        return -1

example = Solution()

apple = [1,3,2]
capacity = [4,3,1,5,2]
result1 = example.minimumBoxes(apple, capacity)
# Explanation: We will use boxes with capacities 4 and 5.
# It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.
assert result1 == 2
print( "result1", result1)