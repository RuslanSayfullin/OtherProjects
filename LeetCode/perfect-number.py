# Совершенное число — это положительное целое число, равное сумме его положительных делителей, за исключением самого числа. 
# Делитель целого числа x — это целое число, которое делит x нацело.
# Дано целое число n. Верните true, если n — совершенное число, в противном случае верните false.

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1:
            return False
        
        divisor_sum = 1  # 1 всегда является делителем

        
        # Перебираем делители до √num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:

                divisor_sum += i
                # Добавляем парный делитель, если он не равен i
                if i != num // i:
                    divisor_sum += num // i
        
        return divisor_sum == num
    

example =Solution()

num = 28
result1 = example.checkPerfectNumber(num)
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
assert result1 == True
print( "result1", result1)

num = 7
result2 = example.checkPerfectNumber(num)
assert result2 == False
print( "result2", result2)

num = 99999994
result3 = example.checkPerfectNumber(num)
assert result3 == False
print( "result3", result3)