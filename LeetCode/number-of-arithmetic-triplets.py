# Вам дан массив целых чисел nums с нулевой индексацией, строго возрастающий, и положительное целое число diff. 
# Тройка (i, j, k) является арифметической тройкой, если выполняются следующие условия:
#   i < j < k,
#   nums[j] - nums[i] == diff, и
#   nums[k] - nums[j] == diff.
# Верните количество уникальных арифметических троек.
from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets: int = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == diff:
                    
                    for k in range(j + 1, len(nums)):
                        if nums[k] - nums[j] == diff:
                            #print(nums[k], nums[j], nums[i])
                            triplets += 1

        return triplets
    
example = Solution()

nums = [0,1,4,6,7,10]
diff = 3
result1 = example.arithmeticTriplets(nums, diff)
# Explanation: (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
assert result1 == 2
print( "result1", result1)

nums = [4,5,6,7,8,9]
diff = 2
result1 = example.arithmeticTriplets(nums, diff)
# Explanation: (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
assert result1 == 2
print( "result1", result1)