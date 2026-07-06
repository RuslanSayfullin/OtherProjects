# Вам дано положительное целое число num. 
# Вы можете поменять местами любые две цифры num, имеющие одинаковую четность (т.е. обе нечетные цифры или обе четные цифры).
# Верните максимально возможное значение num после любого количества замен.

class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        
        # Собираем чётные и нечётные цифры
        evens = sorted([d for d in s if int(d) % 2 == 0], reverse=True)
        odds = sorted([d for d in s if int(d) % 2 != 0], reverse=True)
        
        res = []
        e_idx, o_idx = 0, 0
        
        # Восстанавливаем число, подставляя отсортированные цифры
        for d in s:
            digit = int(d)
            if digit % 2 == 0:
                res.append(evens[e_idx])
                e_idx += 1
            else:
                res.append(odds[o_idx])
                o_idx += 1
        
        return int("".join(res))
    
example = Solution()

num = 1234
result1 = example.largestInteger(num)
# Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
# Swap the digit 2 with the digit 4, this results in the number 3412.
# Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
# Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
print( "result1", result1)
assert result1 == 3412

num = 65875
result2 = example.largestInteger(num)
# Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
# Swap the first digit 5 with the digit 7, this results in the number 87655.
# Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
print( "result2", result2)
assert result2 == 87655

num = 8
result3 = example.largestInteger(num)
print( "result3", result3)
assert result3 == 8

num = 27
result4 = example.largestInteger(num)
print( "result4", result4)
assert result4 == 27

num = 247
result5 = example.largestInteger(num)
print( "result5", result5)
assert result5 == 427