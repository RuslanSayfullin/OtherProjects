# Перевернуть биты заданного 32-битного знакового целого числа.
class Solution:
    def reverseBits(self, n: int) -> int:

        bin_n = bin(n)[2:].zfill(32)

        str_bin_n = str(bin_n)

        reversed_str_bin_n = str_bin_n[::-1]


        reverse_n: int = int(reversed_str_bin_n, 2)
        return reverse_n
    

n = 43261596
example = Solution()
result1 = example.reverseBits(n)
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
assert result1 == 964176192
print("result1", result1)

n = 2147483644
example = Solution()
result1 = example.reverseBits(n)
# Explanation:
# Integer	    Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110
assert result1 == 1073741822
print("result1", result1)
