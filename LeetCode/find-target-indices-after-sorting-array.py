# Вам дан массив целых чисел nums с индексацией от 0 и целевой элемент target.
# Целевой индекс — это индекс i такой, что nums[i] == target.
# Верните список целевых индексов nums после сортировки nums в порядке неубывания. 
# Если целевых индексов нет, верните пустой список. Возвращаемый список должен быть отсортирован в порядке возрастания.

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result: list[int] = []

        nums.sort()
        #print(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result


example = Solution()

nums = [1,2,5,2,3]
target = 2
result1 = example.targetIndices(nums, target)
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
assert result1 == [1,2]
print( "result1", result1)

nums = [1,2,5,2,3]
target = 3
result2 = example.targetIndices(nums, target)
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
assert result2 == [3]
print( "result2", result2)