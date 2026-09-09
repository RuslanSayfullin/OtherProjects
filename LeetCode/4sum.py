# Дан массив `nums`, состоящий из `n` целых чисел. 
# Необходимо вернуть массив всех уникальных четверок `[nums[a], nums[b], nums[c], nums[d]]`, таких что:
# 0 <= a, b, c, d < n
# a, b, c и d — различные индексы. 
# nums[a] + nums[b] + nums[c] + nums[d] == target
# Ответ можно вернуть в любом порядке.

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result: list = []

        nums.sort()
        
        for i in range(len(nums)-3):
            for i2 in range(i+1, len(nums)-2):
                for i3 in range(i2+1, len(nums)-1):
                    for i4 in range(i3+1, len(nums)):
                        if nums[i] + nums[i2] + nums[i3] + nums[i4] == target:
                            element = [nums[i], nums[i2], nums[i3], nums[i4]]
                            if element not in result:
                                result.append([nums[i], nums[i2], nums[i3], nums[i4]])

        return result


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result: list[list[int]] = []

        for i in range(n - 3):
            # Пропуск дубликатов для первого числа
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Пропуск дубликатов для второго числа
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Пропускаем дубликаты для третьего числа
                        left_val = nums[left]
                        while left < right and nums[left] == left_val:
                            left += 1

                        # Пропускаем дубликаты для четвёртого числа
                        right_val = nums[right]
                        while left < right and nums[right] == right_val:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result

example = Solution()
    
nums = [1,0,-1,0,-2,2]
target = 0
result1 = example.fourSum(nums, target)
assert result1 == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print( "result1", result1) 

nums = [2,2,2,2,2]
target = 8
result2 = example.fourSum(nums, target)
assert result2 == [[2,2,2,2]]
print( "result2", result2) 