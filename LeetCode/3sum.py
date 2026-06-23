# Дана целочисленная матрица nums. 
# Верните все тройки [nums[i], nums[j], nums[k]] такие, что i != j, i != k и j != k, а также nums[i] + nums[j] + nums[k] == 0.
# Обратите внимание, что множество решений не должно содержать повторяющихся троек.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sum: list[list[int]] = []
        flag: bool = True

        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums) -1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        for element in three_sum:

                            if set([nums[i], nums[j], nums[k]]) == set(element):
                                flag= False
                            
                        if flag:
                            three_sum.append([nums[i], nums[j], nums[k]])
                        else:
                            flag = True

        return three_sum
    

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Сортировка массива
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Пропускаем дубликаты для первого элемента
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Если текущий элемент положительный, дальше тройки с суммой 0 не найдём
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Пропускаем дубликаты для левого указателя
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Пропускаем дубликаты для правого указателя
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1  # Увеличиваем сумму, сдвигая левый указатель
                else:
                    right -= 1  # Уменьшаем сумму, сдвигая правый указатель

        return result

    

example = Solution()
    
nums = [-1,0,1,2,-1,-4]
result1 = example.threeSum(nums)
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#assert result1 == [[-1,-1,2],[-1,0,1]]
print( "result1", result1)

nums = [0,1,1]
result2 = example.threeSum(nums)
# Explanation: The only possible triplet does not sum up to 0.
assert result2 == []
print( "result2", result2)

nums = [0,0,0]
result3 = example.threeSum(nums)
# Explanation: The only possible triplet sums up to 0.
assert result3 == [[0,0,0]]
print( "result3", result3)

