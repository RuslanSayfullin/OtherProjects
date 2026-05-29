# Вам дан отсортированный массив уникальных целых чисел nums.
# Диапазон [a,b] — это множество всех целых чисел от a до b (включительно).
# Возвращает наименьший отсортированный список диапазонов, который точно покрывает все числа в массиве. 
# То есть каждый элемент массива nums покрывается ровно одним из диапазонов, и не существует целого числа x такого, 
# что x находится в одном из диапазонов, но не в массиве nums.
# Каждый диапазон [a,b] в списке должен выводиться следующим образом:
# "a->b", если a != b
# "a", если a == b
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:  # Обрабатываем пустой массив
            return []
        
        result = []
        start = nums[0]  # Начало текущего диапазона
        end = nums[0]    # Конец текущего диапазона
        
        for i in range(1, len(nums)):
            if nums[i] == end + 1:  # Число продолжает последовательность
                end = nums[i]  # Расширяем текущий диапазон
            else:  # Последовательность прервалась
                # Добавляем текущий диапазон в результат
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                
                # Начинаем новый диапазон
                start = nums[i]
                end = nums[i]
        
        # Добавляем последний диапазон
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        
        return result



example = Solution()

nums = [0,1,2,4,5,7]
result1 = example.summaryRanges(nums)
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
assert result1 == ["0->2","4->5","7"]
print( "result1", result1)

nums = [0,2,3,4,6,8,9]
result2 = example.summaryRanges(nums)
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
assert result2 == ["0","2->4","6","8->9"]
print( "result2", result2)