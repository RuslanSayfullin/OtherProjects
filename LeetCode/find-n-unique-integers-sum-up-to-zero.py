# Дано целое число n. Верните любой массив, содержащий n уникальных целых чисел, сумма которых равна 0.

class Solution:
    def sumZero(self, n: int) -> list[int]:
        result: list = []

        if n < 2:
            result.append(0)

        else:
            for k in range(1, n // 2 + 1):
                element = 0 - k - n
                result.append(element)

            for k in range(1, n // 2 + 1):
                element = 0 + k + n
                result.append(element)

        if n % 2 != 0 and n > 1:
            result.append(0)

        #print(result)
        return result

example = Solution()
    
n = 5
result1 = example.sumZero(n)
assert sum(result1) == 0 and len(result1) == n
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
print( "result1", result1)

n = 3
result2 = example.sumZero(n)
assert sum(result2) == 0 and len(result2) == n
print( "result2", result2)