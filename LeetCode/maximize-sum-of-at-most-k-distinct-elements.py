# Дан массив положительных целых чисел `nums` и целое число `k`.
# Выберите не более `k` элементов из `nums` так, чтобы их сумма была максимальной. При этом выбранные числа должны быть различными.
# Верните массив, содержащий выбранные числа в строго убывающем порядке.

class Solution:
    def maxKDistinct(self, nums: list[int], k: int) -> list[int]:
        result: list[int] = []

        nums = list(set(nums))
        if k > len(nums):
            k = len(nums)
            
        sorted_nums = sorted(nums, reverse=True)
        
        for symbol in range(k):
            result.append(sorted_nums[symbol])

        return result

example = Solution()

nums = [84,93,100,77,90]
k = 3
result1 = example.maxKDistinct(nums, k)
# The maximum sum is 283, which is attained by choosing 93, 100 and 90. We rearrange them in strictly descending order as [100, 93, 90].
assert result1 == [100,93,90]
print( "result1", result1)

nums = [84,93,100,77,93]
k = 3
result2 = example.maxKDistinct(nums, k)
assert result2 == [100,93,84]
print( "result2", result2)