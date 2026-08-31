# Вам дан целочисленный массив nums. Преобразуйте массив nums, выполнив следующие операции в точно указанном порядке:
# Замените каждое четное число на 0.
# Замените каждое нечетное число на 1.
# Отсортируйте измененный массив в порядке убывания.
# Верните результирующий массив после выполнения этих операций.

class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        result: list[int] = []

        for element in nums:
            if element % 2 == 0:
                result.append(0)
            else:
                result.append(1)

        result.sort()
        # print(result)
        return result

example = Solution()
    
nums = [4,3,2,1]
result1 = example.transformArray(nums)
assert result1 == [0,0,1,1]
# Explanation: 
#   * Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
#   * After sorting nums in non-descending order, nums = [0, 0, 1, 1].

print( "result1", result1)