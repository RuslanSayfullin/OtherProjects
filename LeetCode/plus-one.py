from typing import List


# Вам дано большое целое число, представленное в виде целочисленного массива digits, где каждый digits[i] — это i-я цифра числа. 
# Цифры упорядочены слева направо от старшей к младшей. Большое целое число не содержит ведущих нулей.
# Увеличьте большое целое число на единицу и верните полученный массив digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result: list[int] = []

        str_to_dig = ""
        
        for d in digits:
            str_to_dig += str(d)

        dig_to_str = int(str_to_dig) + 1   
        str_to_dig = str(dig_to_str)

        for s in str_to_dig:
            result.append(int(s))
        
        
        return result


digits = [1,2,3]
example =Solution()
result1 = example.plusOne(digits)
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#assert result1 == [1,2,4]
print( "result1", result1)

digits = [4,3,2,1]
example =Solution()
result2 = example.plusOne(digits)
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#assert result2 == [4,3,2,2]
print( "result2", result2)

digits = [9]
example =Solution()
result3 = example.plusOne(digits)
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#assert result3 == [1,0]
print( "result3", result3)