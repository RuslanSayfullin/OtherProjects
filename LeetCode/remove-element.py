# Дан массив целых чисел nums и массив целых чисел val. Необходимо удалить все вхождения val из массива nums на месте. 
# Порядок элементов может быть изменен. Затем верните количество элементов в массиве nums, которые не равны val.
# Рассмотрим количество элементов в массиве nums, которые не равны значению k. 
# Для того чтобы запрос был принят, необходимо выполнить следующие действия:
#   - Измените массив nums таким образом, чтобы первые k элементов nums содержали элементы, не равные val. Остальные элементы nums, а также размер массива nums, не имеют значения.
#   - Верните k.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # счётчик «хороших» элементов
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


nums = [3,2,2,3]
val = 3

example = Solution()
output1 = example.searchInsert(nums, val)
print(output1, nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
output1 = example.searchInsert(nums, val)
print(output1, nums)