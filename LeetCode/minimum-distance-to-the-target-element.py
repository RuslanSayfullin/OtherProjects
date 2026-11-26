# Дан целочисленный массив nums (с индексацией от 0) и два целых числа target и start. 
# Найдите индекс i такой, что nums[i] == target и abs(i - start) минимизируется. Обратите внимание, что abs(x) — это абсолютное значение x.
# Верните abs(i - start).
# Гарантируется, что target существует в массиве nums.

class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:

        distanse: int = 1000

        for i in range(len(nums)):
            if nums[i] == target:
                if abs(i - start) < distanse:
                    distanse = abs(i - start)

        return distanse

example = Solution()

nums = [1,2,3,4,5]
target = 5
start = 3
result1 = example.getMinDistance(nums, target, start)
# Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
print( "result1", result1)
assert result1 == 1