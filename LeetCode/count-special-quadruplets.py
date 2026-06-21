# Дан массив целых чисел nums с индексацией от 0. Верните количество различных четверок (a, b, c, d) таких, что:
# nums[a] + nums[b] + nums[c] == nums[d], и a < b < c < d
from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        quadruplets: int = 0
        n = len(nums)
        
        # Перебираем все возможные комбинации a < b < c < d
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                for c in range(b + 1, n - 1):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            quadruplets += 1
        
        return quadruplets

example = Solution()

nums = [1,2,3,6]
result1 = example.countQuadruplets(nums)
# Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
assert result1 == 1
print( "result1", result1)

nums = [3,3,6,4,5]
result2 = example.countQuadruplets(nums)
# Explanation: There are no such quadruplets in [3,3,6,4,5].
assert result2 == 0
print( "result2", result2)

nums = [1,1,1,3,5]
result3 = example.countQuadruplets(nums)
# Explanation: The 4 quadruplets that satisfy the requirement are:
#- (0, 1, 2, 3): 1 + 1 + 1 == 3
#- (0, 1, 3, 4): 1 + 1 + 3 == 5
#- (0, 2, 3, 4): 1 + 1 + 3 == 5
#- (1, 2, 3, 4): 1 + 1 + 3 == 5
assert result3 == 4
print( "result3", result3)