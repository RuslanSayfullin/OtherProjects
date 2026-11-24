# Дан массив положительных целых чисел `nums`.
# Алиса и Боб играют в игру. В этой игре Алиса может выбрать либо все однозначные числа из `nums`, либо все двузначные числа; 
# оставшиеся числа достаются Бобу. Алиса выигрывает, если сумма её чисел строго больше суммы чисел Боба.
# Верните `true`, если Алиса может выиграть в этой игре, в противном случае верните `false`.

class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        result: bool = False

        sum1: int = 0
        sum2: int = 0

        for i in nums:
            if i > 9:
                sum1 += i
            else:
                sum2 += i

        if sum1 != sum2:
            result = True

        return result

example = Solution()

nums = [1,2,3,4,10]
result1 = example.canAliceWin(nums)
print( "result1", result1)
assert not result1