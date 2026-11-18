# Дано положительное целое число `num`, состоящее ровно из четырех цифр. Разбейте `num` на два новых целых числа, `new1` и `new2`, используя все цифры, входящие в состав `num`. 
# В числах `new1` и `new2` допускается наличие незначащих нулей (нулей в начале числа).
# Например, если `num = 2932`, то в вашем распоряжении следующие цифры: две двойки, одна девятка и одна тройка. 
# Возможные варианты разбиения на пары `[new1, new2]` включают, в частности, такие комбинации, как `[22, 93]`, `[23, 92]`, `[223, 9]` и `[2, 329]`.
# Верните минимально возможную сумму чисел `new1` и `new2`.
class Solution:
    def minimumSum(self, num: int) -> int:
        result: int = 0

        nums_str = list(str(num))
        nums_int = []
        for symbol in nums_str:
            nums_int.append(int(symbol))

        new1 = ""
        new2 = ""
        flag = False
        while len(nums_int) != 0:
            min_val = min(nums_int)
            nums_int.remove(min_val)
            if flag:
                new1 = new1 + str(min_val)
                flag = False
            elif not flag:
                new2 = new2 + str(min_val)
                flag = True

        result = int(new1) + int(new2)
        return result


example = Solution()

num = 2932
result1 = example.minimumSum(num)
# Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
# The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
print( "result1", result1)
assert result1 == 52

num = 4009
result2 = example.minimumSum(num)
# Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
# The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
print( "result2", result2)
assert result2 == 13