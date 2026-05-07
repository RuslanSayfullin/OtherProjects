# Вам дан целочисленный массив cost, где cost[i] — стоимость i-й ступени лестницы. 
# После оплаты вы можете подняться либо на одну, либо на две ступени.
# Вы можете начать либо с шага с индексом 0, либо с шага с индексом 1.
# Верните минимальную стоимость, необходимую для достижения верхней границы этажа.
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        
        return dp[n]
    
cost = [10,15,20]
example = Solution()
result1 = example.minCostClimbingStairs(cost)
# You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
assert result1 == 15
print(result1)

cost = [1,100,1,1,1,100,1,1,100,1]
example = Solution()
result2 = example.minCostClimbingStairs(cost)
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
assert result2 == 6
print(result2)