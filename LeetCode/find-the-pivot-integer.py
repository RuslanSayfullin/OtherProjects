# Дано положительное целое число n. Найдите опорное целое число x такое, что:
# Сумма всех элементов от 1 до x включительно равна сумме всех элементов от x до n включительно.
# Верните опорное целое число x. Если такого числа не существует, верните -1. 
# ​​Гарантируется, что для заданного входного значения будет не более одного опорного индекса.

class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot: int = -1

        if n == 1:
            pivot = n
        else:
            for i in range(1, n):
                if sum(range(i+1)) == sum(range(i, n+1)):
                    #print(i, sum(range(i+1)), sum(range(i, n+1)))
                    pivot = i

        return pivot
    
example = Solution()

n = 8
result1 = example.pivotInteger(n)
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
#assert result1 == 6
print( "result1", result1)

n = 1
result2 = example.pivotInteger(n)
# Explanation: 1 is the pivot integer since: 1 = 1.
#assert result2 == 1
print( "result2", result2)

n = 4
result3 = example.pivotInteger(n)
# Explanation: It can be proved that no such integer exist.
#assert result3 == -1
print( "result3", result3)
    