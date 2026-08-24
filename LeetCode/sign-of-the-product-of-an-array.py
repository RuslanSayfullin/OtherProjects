# Реализуйте функцию signFunc(x), которая возвращает:
# 1, если x положительное.
# -1, если x отрицательное.
# 0, если x равно 0.
# Вам дан целочисленный массив nums. Пусть product — произведение всех значений в массиве nums.
# Верните signFunc(product).

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        result: int = 0

        generation: int = 1

        for element in nums:
            generation *= element

        #print(generation)

        if generation > 0:
            result = 1
        elif generation < 0:
            result = -1

        return result
    
example = Solution()

nums = [-1,-2,-3,-4,3,2,1]
result1 = example.arraySign(nums)
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
assert result1 == 1
print( "result1", result1)

