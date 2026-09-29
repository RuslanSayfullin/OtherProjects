# Херси хочет накопить деньги на свой первый автомобиль. Каждый день он вносит деньги в банк Leetcode.
# В первый день, в понедельник, он вносит 1 доллар. Каждый день со вторника по воскресенье он вносит на 1 доллар больше, чем в предыдущий день. 
# В каждый последующий понедельник он вносит на 1 доллар больше, чем в предыдущий понедельник.
# Дано число n; верните общую сумму денег, которая будет у него в банке Leetcode в конце n-го дня.

class Solution:
    def totalMoney(self, n: int) -> int:
        result: int = 0
        
        puts = 1
        days = 0
        salary = 0

        for k in range(1, n+1):
                
            if days == 7:
                salary = k // 7 
                days = 0

            salary += puts
            result += salary
            days += 1
            #print(result, salary, puts, days)

        return result

example = Solution()

n = 4
result1 = example.totalMoney(n)
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
assert result1 == 10
print( "result1", result1)

n = 10
result2 = example.totalMoney(n)
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
assert result2 == 37
print( "result2", result2)

n = 20
result3 = example.totalMoney(n)
# After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
assert result3 == 96
print( "result3", result3)