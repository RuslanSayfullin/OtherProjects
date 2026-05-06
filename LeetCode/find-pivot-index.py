# Дан массив целых чисел nums. Необходимо вычислить опорный индекс этого массива.
# Опорный индекс — это индекс, сумма всех чисел, расположенных строго слева от него, 
# равна сумме всех чисел, расположенных строго справа от него.
# Если индекс находится на левом краю массива, то левая сумма равна 0, поскольку слева нет элементов. 
# Это также относится и к правому краю массива.
# Возвращает самый левый индекс опорного элемента. Если такого индекса не существует, возвращает -1.
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Правая сумма = общая сумма - левая сумма - текущий элемент
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            # Обновляем левую сумму для следующего элемента
            left_sum += nums[i]
        
        return -1
    

nums = [1,7,3,6,5,6]
example = Solution()
result1 = example.pivotIndex(nums)
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
assert result1 == 3
print(result1)

nums = [1,2,3]
example = Solution()
result2 = example.pivotIndex(nums)
# There is no index that satisfies the conditions in the problem statement.
assert result2 == -1
print(result2)

nums = [2,1,-1]
example = Solution()
result3 = example.pivotIndex(nums)
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
assert result3 == 0
print(result3)

nums = [-1,-1,-1,-1,-1,0]
example = Solution()
result4 = example.pivotIndex(nums)
#assert result4 == 2
print(result4)