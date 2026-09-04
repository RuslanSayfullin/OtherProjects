# Дан массив nums различных целых чисел. Верните все возможные варианты.
# Вы можете вернуть ответ в любом порядке.
import itertools

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list = []

        for item in itertools.permutations(nums, len(nums)):
            #print(item)
            result.append(item)
        return result

example = Solution()

nums = [1,2,3]
result1 = example.permute(nums)
#assert result1 == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print( "result1", result1)

nums = [0, 1]
result2 = example.permute(nums)
assert result2 == [[0,1],[1,0]]
print( "result2", result2)
        