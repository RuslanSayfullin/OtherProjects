# Дан целочисленный массив `nums`. За одну операцию можно прибавить 1 к любому элементу массива или вычесть из него 1.
# Верните минимальное количество операций, необходимых для того, чтобы все элементы массива `nums` делились на 3.

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        result: int = 0
        for k in nums:
            if k % 3 == 0:
                pass
            else:
                while k % 3 != 0:
                    if (k + 1) % 3 == 0 or (k -1) % 3 == 0:
                        result += 1
                    if (k + 1) % 3 == 0:
                        k += 1
                    elif (k - 1) % 3 == 0:
                        k -= 1

        return result

    
example = Solution()

nums = [1,2,3,4]
result1 = example.minimumOperations(nums)
# Explanation: All array elements can be made divisible by 3 using 3 operations:
# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
assert result1 == 3
print( "result1", result1)