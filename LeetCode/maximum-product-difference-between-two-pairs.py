# Разность произведений двух пар (a, b) и (c, d) определяется как (a * b) - (c * d). 
# Например, разность произведений для пар (5, 6) и (2, 7) равна (5 * 6) - (2 * 7) = 16.
# Дан целочисленный массив nums. Необходимо выбрать четыре различных индекса w, x, y и z так, 
# чтобы разность произведений пар (nums[w], nums[x]) и (nums[y], nums[z]) была максимальной.
# Верните эту максимальную разность произведений.

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        result: int = 0

        nums.sort()

        result = (nums[-1] * nums[-2]) - (nums[0] * nums[1])

        return result


example = Solution()

nums = nums = [5,6,2,7,4]
result1 = example.maxProductDifference(nums)
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.
assert result1 == 34
print(result1)