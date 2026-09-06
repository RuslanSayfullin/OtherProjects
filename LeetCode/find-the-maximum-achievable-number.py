# Даны два целых числа, num и t. Число x достижимо, если оно может стать равным num после выполнения не более чем t операций:
# Увеличить или уменьшить x на 1 и одновременно увеличить или уменьшить num на 1.
# Вернуть максимально возможное значение x.

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        result: int = 0

        result = num + t + t

        return result

    
example = Solution()

num = 4
t = 1
result1 = example.theMaximumAchievableX(num, t)
# Explanation: Apply the following operation once to make the maximum achievable number equal to num:
# Decrease the maximum achievable number by 1, and increase num by 1.
assert result1 == 6
print( "result1", result1)

num = 3
t = 2
result2 = example.theMaximumAchievableX(num, t)
# Explanation: Apply the following operation twice to make the maximum achievable number equal to num:
# Decrease the maximum achievable number by 1, and increase num by 1.
assert result2 == 7
print( "result2", result2)
