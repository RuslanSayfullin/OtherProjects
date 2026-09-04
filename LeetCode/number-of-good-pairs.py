# Дан массив целых чисел nums. Верните количество хороших пар.
# Пара (i, j) называется хорошей, если nums[i] == nums[j] и i < j.

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result: int = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                #print(nums[i], nums[j])
                if nums[i] == nums[j]:
                    result += 1




        return result

example = Solution()

nums = [1,2,3,1,1,3]
result1 = example.numIdenticalPairs(nums)
assert result1 == 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
print( "result1", result1)

nums = [1,1,1,1]
result2 = example.numIdenticalPairs(nums)
assert result2 == 6
# Explanation: Each pair in the array are good.
print( "result2", result2)