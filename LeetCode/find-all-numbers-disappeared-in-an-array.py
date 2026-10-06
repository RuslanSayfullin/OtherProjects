# Дан массив nums из n целых чисел, где каждое число nums[i] находится в диапазоне [1, n]. 
# Верните массив, содержащий все целые числа из диапазона [1, n], которые отсутствуют в nums.

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result: list[int] = []

        for i in range(1, len(nums)+1):
            if i in nums:
                pass
            else:
                result.append(i)

        return result

example = Solution()

nums = [4,3,2,7,8,2,3,1]
result1 = example.findDisappearedNumbers(nums)
assert result1 == [5,6]
print( "result1", result1)

nums = [1,1]
result2 = example.findDisappearedNumbers(nums)
assert result2 == [2]
print( "result2", result2)