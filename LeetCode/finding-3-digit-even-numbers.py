# Вам дан массив целых чисел digits, где каждый элемент — это цифра. Массив может содержать повторяющиеся числа.
# Вам нужно найти все уникальные целые числа, которые соответствуют заданным требованиям:
# Целое число представляет собой конкатенацию трех элементов из массива digits в любом произвольном порядке.
# Целое число не содержит ведущих нулей.
# Целое число является четным.
# Например, если заданы числа digits [1, 2, 3], то целые числа 132 и 312 соответствуют требованиям.
# Верните отсортированный массив уникальных целых чисел.
from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even_numbers: List[int] = []

        for t in permutations(digits, 3):
            if t[0] != 0:
                element = int(str(t[0])+str(t[1])+str(t[2]))
                if element % 2 == 0:
                    even_numbers.append(element)
        
        even_numbers= list(set(even_numbers))
        even_numbers.sort()
        # print(even_numbers)
        return even_numbers
    
example =Solution()

digits = [2,1,3,0]
result1 = example.findEvenNumbers(digits)
# Explanation: All the possible integers that follow the requirements are in the output array. 
# Notice that there are no odd integers or integers with leading zeros.
assert result1 == [102,120,130,132,210,230,302,310,312,320]
print( "result1", result1)

example =Solution()

digits = [2,2,8,8,2]
result2 = example.findEvenNumbers(digits)
# Explanation: The same digit can be used as many times as it appears in digits. 
# In this example, the digit 8 is used twice each time in 288, 828, and 882. 
assert result2 == [222,228,282,288,822,828,882]
print( "result2", result2)

digits = [3,7,5]
result3 = example.findEvenNumbers(digits)
# Explanation: No even integers can be formed using the given digits.
assert result3 == []
print( "result3", result3)

