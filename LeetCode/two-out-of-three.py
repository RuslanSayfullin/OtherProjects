# Даны три целочисленных массива nums1, nums2 и nums3. 
# Верните массив уникальных значений, содержащий все значения, которые присутствуют как минимум в двух из трех массивов. 
# Вы можете вернуть значения в любом порядке.
from typing import List
from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        intersection = []
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        num3 = list(set(nums3))

        biglist = num1 + num2 + num3
        bigdict = Counter(biglist)
        print(bigdict)
        for key, value in bigdict.items():
            if value > 1:
                intersection.append(key)

        return intersection
    
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
example = Solution()
result1 = example.twoOutOfThree(nums1, nums2,nums3) 
assert result1 == [3,2]
print("result1", result1)

nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
example = Solution()
result2 = example.twoOutOfThree(nums1, nums2,nums3) 
assert result2 == [2,3,1]
print("result2", result1)