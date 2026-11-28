# Дан список неотрицательных целых чисел `nums`. 
# Расположите их таким образом, чтобы в результате получилось максимально возможное число, и верните его.
# Поскольку результат может быть очень большим, его следует вернуть в виде строки, а не целого числа.

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1   # a раньше
            elif a + b < b + a:
                return 1    # b раньше
            return 0

        strs = list(map(str, nums))
        strs.sort(key=cmp_to_key(compare))
        result = "".join(strs)

        # Крайний случай: если получились одни нули ("000"), нужен один "0"
        return "0" if result[0] == "0" else result


example = Solution()

nums = [3,30,34,5,9]
result1 = example.largestNumber(nums)
print( "result1", result1)
assert result1 == "9534330"