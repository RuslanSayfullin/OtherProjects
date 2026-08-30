# Дан массив целых чисел nums, отсортированный в порядке неубывания.
# Необходимо вернуть массив квадратов каждого числа, также отсортированный в порядке неубывания.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        result = [x * x for x in nums]
        
        result.sort()
        #print(result)
        return result

example = Solution()
    
nums = [-4,-1,0,3,10]
result1 = example.sortedSquares(nums)
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
assert result1 == [0,1,9,16,100]
print( "result1", result1)
        