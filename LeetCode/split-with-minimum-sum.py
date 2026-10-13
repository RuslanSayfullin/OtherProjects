# Дано целое положительное число `num`. Разбейте его на два неотрицательных целых числа `num1` и `num2` так, чтобы:
# Конкатенация `num1` и `num2` представляла собой перестановку цифр числа `num`. 
# Иными словами, суммарное количество вхождений каждой цифры в числах `num1` и `num2` должно быть равно количеству вхождений этой цифры в числе `num`. 
# Числа `num1` и `num2` могут содержать ведущие нули.
# Верните минимально возможную сумму чисел `num1` и `num2`.
# Примечания:
# Гарантируется, что число `num` не содержит ведущих нулей. 
# Порядок следования цифр в числах `num1` и `num2` может отличаться от порядка следования цифр в числе `num`.

class Solution:
    def splitNum(self, num: int) -> int:
        result: int = 0

        sorted_num = "".join(sorted(str(num)))
        chunk1 = ""
        chunk2 = ""

        for s in range(len(sorted_num)):
            if s % 2 != 0:
                chunk1 = chunk1 + sorted_num[s]
            else:
                chunk2 = chunk2 + sorted_num[s]

        result = int(chunk1) + int(chunk2)
        return result
        


example = Solution()

num = 4325
result1 = example.splitNum(num)
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. 
# We can prove that 59 is indeed the minimal possible sum.
assert result1 == 59
print( "result1", result1)

num = 687
result2 = example.splitNum(num)
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. 
# We can prove that 59 is indeed the minimal possible sum.
assert result2 == 75
print( "result2", result2)