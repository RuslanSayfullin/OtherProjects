# Дан массив положительных целых чисел `nums`, индексация которого начинается с нуля. Найдите количество троек (i, j, k), удовлетворяющих следующим условиям:
# 0 <= i < j < k < nums.length
# Числа `nums[i]`, `nums[j]` и `nums[k]` попарно различны. 
# Иными словами, `nums[i] != nums[j]`, `nums[i] != nums[k]` и `nums[j] != nums[k]`.
# Верните количество таких троек.
from collections import Counter

class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        freq = Counter(nums)
        
        # Получаем уникальные числа и сортируем их (сортировка нужна только для порядка, 
        # чтобы разделять на left/mid/right; сами значения не важны, важен порядок обхода)
        unique_nums = sorted(freq.keys())
        
        n = len(nums)
        left = 0
        result = 0
        
        for num in unique_nums:
            mid = freq[num]
            right = n - left - mid
            
            # Добавляем количество троек, где:
            # одно число из "left", текущее число "mid", и одно из "right"
            result += left * mid * right
            
            left += mid
        
        return result

example = Solution()

nums = [4,4,2,4,3]
result1 = example.unequalTriplets(nums)
# Explanation: The following triplets meet the conditions:
# - (0, 2, 4) because 4 != 2 != 3
# - (1, 2, 4) because 4 != 2 != 3
# - (2, 3, 4) because 2 != 4 != 3
# Since there are 3 triplets, we return 3.
# Note that (2, 0, 4) is not a valid triplet because 2 > 0.
assert result1 == 3
print( "result1", result1)