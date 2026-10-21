# Дано целое число rowIndex; верните строку с индексом rowIndex (нумерация начинается с 0) треугольника Паскаля.
# В треугольнике Паскаля каждое число равно сумме двух чисел.

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result: list[list[int]] = []

        if rowIndex == 0:
            result.append([1])
        elif rowIndex == 1:
            result.extend([[1], [1, 1]])
        else:
            result.extend([[1], [1, 1]])
            for i in range(3, rowIndex+2):
                temp = []
                for j in range(i):
                   
                    if j == 0:
                        temp.append(1)
                    elif j == (i - 1):
                        temp.append(1)
                    else:
                        sum1 = result[i-2][j-1]
                        sum2 = result[i-2][j]
                        temp.append(sum1+sum2)

                result.append(temp)
                temp = []

        return result[rowIndex]

example = Solution()

rowIndex = 3
result1 = example.getRow(rowIndex)

assert result1 == [1,3,3,1]
print( "result1", result1)