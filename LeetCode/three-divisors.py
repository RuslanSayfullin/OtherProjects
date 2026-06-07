# Если n — целое число, верните true, если n имеет ровно три положительных делителя. В противном случае верните false.
# Целое число m является делителем n, если существует целое число k такое, что n = k * m.

class Solution:
    def isThree(self, n: int) -> bool:
        has_three_divisor: bool= False
        count = 1   # число всегда делится само на себя
        
        for i in range(1, (n // 2 + 1) ):
         
            if n % i == 0:
                count += 1
           
        if count == 3:
            has_three_divisor = True

        return has_three_divisor
    
example = Solution()

n = 2
result1 = example.isThree(n)
# Explanation: 2 has only two divisors: 1 and 2.
assert not result1
print( "result1", result1)

n = 4
result2 = example.isThree(n)
# Explanation: 4 has three divisors: 1, 2, and 4.
assert result2
print( "result2", result2)
