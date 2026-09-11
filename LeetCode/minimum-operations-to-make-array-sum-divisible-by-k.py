# Дан целочисленный массив `nums` и целое число `k`. Вы можете любое количество раз выполнять следующую операцию:
# Выбрать индекс `i` и заменить `nums[i]` на `nums[i] - 1`.
# Верните минимальное количество операций, необходимое для того, чтобы сумма элементов массива стала кратной `k`.

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        result: int = 0

        nums.sort()

        if sum(nums) % k == 0:
            pass
        else:
            while sum(nums) % k != 0:
                result += 1
                nums[0] = nums[0] - 1

        return result


example =Solution()

nums = [3,9,7]
k = 5
result1 = example.minOperations(nums, k)
# Explanation: Perform 4 operations on nums[1] = 9. Now, nums = [3, 5, 7].
# The sum is 15, which is divisible by 5.
assert result1 == 4
print( "result1", result1)

nums = [4,1,3]
k = 4
result2 = example.minOperations(nums, k)
# Explanation: The sum is 8, which is already divisible by 4. Hence, no operations are needed.
assert result2 == 0
print( "result2", result2)

nums = [3,2]
k = 6
result3 = example.minOperations(nums, k)
# Explanation: The sum is 8, which is already divisible by 4. Hence, no operations are needed.
assert result3 == 0
print( "result3", result3)