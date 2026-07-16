# Самоделяющееся число — это число, которое делится на каждую свою цифру.
# Например, 128 — самоделяющееся число, потому что 128 % 1 == 0, 128 % 2 == 0 и 128 % 8 == 0.
# Самоделяющееся число не может содержать цифру ноль.
# Даны два целых числа: левый и правый. Верните список всех самоделящихся чисел в диапазоне [левый, правый] (включительно).
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers: List[int] = []

        for i in range(left, right+1):
            if i < 10 :
                numbers.append(i)
            else:
                str_i = list(str(i))

                is_self_div = True
                for s in str_i:
                    int_str_i = int(s)
                    if int_str_i == 0 or i % int_str_i != 0:
                        is_self_div = False
                        break

                if is_self_div:
                    numbers.append(i)

        return numbers

        
example =Solution()

left = 1
right = 22
result1 = example.selfDividingNumbers(left, right)
assert result1 == [1,2,3,4,5,6,7,8,9,11,12,15,22]
print( "result1", result1)

left = 47
right = 85
result2 = example.selfDividingNumbers(left, right)
assert result2 == [48,55,66,77]
print( "result2", result2)