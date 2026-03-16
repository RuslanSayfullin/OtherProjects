"""
    Вам дан массив цифр, называемый digits. 
    Ваша задача — определить количество различных трехзначных четных чисел, которые можно составить из этих цифр.
    Каждая копия цифры может быть использована только один раз в числе, и в начале числа не должно быть нулей.
"""
from typing import List

from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        
        # Генерируем все возможные перестановки из 3 цифр
        for perm in permutations(digits, 3):
            # Проверяем условия:
            # 1. Число не начинается с нуля
            # 2. Число чётное (последняя цифра чётная)
            if perm[0] != 0 and perm[2] % 2 == 0:
                # Преобразуем тройку цифр в число
                num = perm[0] * 100 + perm[1] * 10 + perm[2]
                seen.add(num)
        
        return len(seen)




digits = ([1,2,3,4], [0,2,2], [6,6,6], [1,3,5])
example = Solution()
for digit in digits:
    result = example.totalNumbers(digit)
    print("result", result)

