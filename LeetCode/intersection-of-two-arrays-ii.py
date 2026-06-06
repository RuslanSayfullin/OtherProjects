# Даны два целочисленных массива nums1 и nums2. Верните массив, содержащий их пересечение. 
# Каждый элемент в результате должен встречаться столько раз, сколько он встречается в обоих массивах, 
# и вы можете вернуть результат в любом порядке.
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect_list = []

        if len(nums1) >= len(nums2):
            for s in nums1:
                if s in nums2:
                    intersect_list.append(s)
                    nums2.remove(s)

                    if len(nums2) < 1:
                        return intersect_list
        else:
            for s in nums2:
                if s in nums1:
                    intersect_list.append(s)
                    nums1.remove(s)

                    if len(nums1) < 1:
                        return intersect_list
                    
        return intersect_list

        
example = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
result1 = example.intersect(nums1, nums2)
assert result1 == [2,2]
print( "result1", result1)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result2 = example.intersect(nums1, nums2)
assert result2 == [9,4]
print( "result2", result2)