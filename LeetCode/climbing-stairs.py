# Вы поднимаетесь по лестнице. Чтобы добраться до вершины, нужно сделать n шагов.
# Каждый раз вы можете подняться либо на 1, либо на 2 шага. Сколькими различными способами можно подняться на вершину?
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Инициализируем первые два значения последовательности Фибоначчи
        prev2 = 1  # f(1)
        prev1 = 2  # f(2)
        
        # Вычисляем значения от 3 до n
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1


example = Solution()

n = 2
result1 = example.climbStairs(n)
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
assert result1 == 2
print( "result1", result1)

n = 3
result2 = example.climbStairs(n)
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
assert result2 == 3
print( "result2", result2)

n = 6
result3 = example.climbStairs(n)
assert result3 == 13
print( "result3", result3)

n = 8
result4 = example.climbStairs(n)
assert result4 == 20
print( "result3", result3)