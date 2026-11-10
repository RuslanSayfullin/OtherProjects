# Дан массив положительных целых чисел `nums`. 
# Сумма элементов — это сумма всех чисел, входящих в массив `nums`. 
# Сумма цифр — это сумма всех цифр (не обязательно различных), встречающихся в числах массива `nums`.
# Верните абсолютную разность между суммой элементов и суммой цифр массива `nums`.
# Напомним, что абсолютная разность между двумя целыми числами `x` и `y` определяется как `|x - y|`.

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        result: int = 0

        s_of_e = sum(nums)
        s_of_d = 0
        temp = ""
        for element in nums:
            temp = temp + str(element)

        for s in temp:
            s_of_d += int(s)

        result = abs(s_of_e - s_of_d)
        
        return result

example = Solution()

nums = [1,15,6,3]
result1 = example.differenceOfSum(nums)
# Explanation: The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
assert result1 ==  9
print( "result1", result1)
