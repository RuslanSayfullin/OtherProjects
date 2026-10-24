# Дано целое число n.
# Целое число называется «монобитным» (Monobit), если все биты в его двоичном представлении одинаковы.
# Верните количество монобитных чисел в диапазоне [0, n] (включительно).

class Solution:
    def countMonobit(self, n: int) -> int:
        result: int = 0

        for i in range(n+1):
            bit = str(bin(i)[2:])

            if len(set(bit)) == 1:
                result +=1


        return result

example = Solution()

n = 1
result1 = example.countMonobit(n)
# Explanation: 
# The integers in the range [0, 1] have binary representations "0" and "1".
# Each representation consists of identical bits. Thus, the answer is 2.
assert result1 == 2
print( "result1", result1)

n = 4
result2 = example.countMonobit(n)
# Explanation: 
# The integers in the range [0, 4] include binaries "0", "1", "10", "11", and "100".
# Only 0, 1 and 3 satisfy the Monobit condition. Thus, the answer is 3.
assert result2 == 3
print( "result2", result2)