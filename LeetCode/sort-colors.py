# Дан массив `nums`, содержащий `n` объектов красного, белого или синего цвета. 
# Необходимо отсортировать их на месте так, чтобы объекты одного цвета располагались рядом, а цвета шли в порядке: красный, белый, синий.
# Для обозначения цветов (красного, белого и синего) будем использовать целые числа 0, 1 и 2 соответственно.
# Задачу необходимо решить без использования встроенной функции сортировки.

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            nums[i], nums[min_idx] = nums[min_idx], nums[i]


example = Solution()

nums = [2,0,2,1,1,0]
example.sortColors(nums)
# The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.
assert nums == [0,0,1,1,2,2]
print( "nums", nums)