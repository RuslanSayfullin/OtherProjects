# Дано положительное целое число n. Верните наименьшее положительное целое число, которое является кратным одновременно 2 и n

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        result: int = n

        while True:

            if result % n != 0 or result % 2 != 0:
                result += 1
            else:
                break  

        return result


example = Solution()
    
n = 5
result1 = example.smallestEvenMultiple(n)
# Explanation: The smallest multiple of both 5 and 2 is 10.
assert result1 == 10
print( "result1", result1)