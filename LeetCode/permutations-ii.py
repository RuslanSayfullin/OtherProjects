# Дан набор чисел `nums`, который может содержать дубликаты; верните все возможные уникальные перестановки в любом порядке.
import itertools

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []

        for item in itertools.permutations(nums, len(nums)):
            if list(item) not in result:
                result.append(list(item))

        return result

example = Solution()

nums = [1,1,2]
result1 = example.permuteUnique(nums)
assert result1 == [[1,1,2], [1,2,1], [2,1,1]]
print(result1)

nums = [1]
result2 = example.permuteUnique(nums)
assert result2 == [[1]]
print(result2)