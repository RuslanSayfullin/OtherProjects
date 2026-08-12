# Перевернуть целое число означает перевернуть все его цифры.
# Например, перевернув 2021, получим 1202. Перевернув 12300, получим 321, поскольку ведущие нули не сохраняются.
# Дано целое число num. Переверните num, чтобы получить reversed1, затем переверните reversed1, чтобы получить reversed2. 
# Верните true, если reversed2 равно num. В противном случае верните false.

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:


        new_num = str(num)
        new_num = int(new_num[::-1])
        new_num = str(new_num)
        new_num = int(new_num[::-1])

        return new_num == num



example = Solution()

num = 526
result1 = example.isSameAfterReversals(num)
# Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
assert result1
print( "result1", result1)

num = 1800
result2 = example.isSameAfterReversals(num)
# Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
assert not result2
print( "result2", result2)