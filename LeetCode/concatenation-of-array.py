# Дан целочисленный массив nums длиной n. 
# Вам нужно создать массив ans длиной 2n, где ans[i] == nums[i] и ans[i + n] == nums[i] для 0 <= i < n (индексация начинается с 0).
# В частности, ans — это конкатенация двух массивов nums.
# Возвращает массив ans.
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums * 2
        return ans


nums = [1,2,1]
example1 = Solution()
result1 = example1.getConcatenation(nums)
assert result1 == [1,2,1,1,2,1]
print(result1)

nums = [1,3,2,1]
example2 = Solution()
result2 = example2.getConcatenation(nums)
assert result2 == [1,3,2,1,1,3,2,1]
print(result2)


