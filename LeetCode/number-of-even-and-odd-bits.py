# Вам дано положительное целое число n.
# Пусть even обозначает количество четных индексов в двоичном представлении числа n со значением 1.
# Пусть odd обозначает количество нечетных индексов в двоичном представлении числа n со значением 1.
# Обратите внимание, что в двоичном представлении числа биты индексируются справа налево.
# Верните массив [even, odd].

class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        even: int = 0
        odd: int = 0

        bin_n = bin(n)
        bin_n = bin_n[2:]
        bin_n = bin_n[::-1]
        
        for i in range(len(bin_n)):
            #print(bin_n, bin_n[i], i+1)
            if bin_n[i] == "1":
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            else:
                pass

        #print(even, odd)      
        return [even, odd]
    
example = Solution()
    
n = 50
result1 = example.evenOddBit(n)
# Explanation: The binary representation of 50 is 110010.
# It contains 1 on indices 1, 4, and 5.
assert result1 == [1,2]
print( "result1", result1)

n = 2
result2 = example.evenOddBit(n)
# Explanation: The binary representation of 2 is 10.
# It contains 1 only on index 1.
assert result2 == [0,1]
print( "result2", result2)

n = 5
result3 = example.evenOddBit(n)
assert result3 == [2,0]
print( "result3", result3)

        