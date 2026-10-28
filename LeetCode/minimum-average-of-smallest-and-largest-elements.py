# У вас есть массив чисел с плавающей запятой `averages`, который изначально пуст. Вам дан массив `nums`, состоящий из `n` целых чисел, где `n` — чётное число.
# Выполните следующую процедуру `n / 2` раза:
# Удалите из массива `nums` наименьший элемент (`minElement`) и наибольший элемент (`maxElement`). 
# Добавьте значение `(minElement + maxElement) / 2` в массив `averages`.
# Верните минимальный элемент из массива `averages`.

class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        result: float = 0.0

        averages = []

        nums = sorted(nums)
        for i in range(len(nums) // 2):
            minElement = nums[0]
            maxElement = nums[-1]

            nums.pop(0)
            nums.pop(-1)
            averages.append((minElement+maxElement)/2)


        result = min(averages)
        return result

example = Solution()

nums = [7,8,3,4,15,13,4,1]
result1 = example.minimumAverage(nums)
assert result1 == 5.5
print( "result1", result1)