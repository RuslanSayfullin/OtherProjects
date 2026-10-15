# Дано целое число numRows; верните первые numRows строк треугольника Паскаля.
# В треугольнике Паскаля каждое число равно сумме двух чисел, расположенных непосредственно над ним.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result: list[list[int]] = []

        if numRows < 1:
            pass
        elif numRows == 1:
            result.append([1])
        elif numRows == 2:
            result.extend([[1], [1, 1]])
        else:
            result.extend([[1], [1, 1]])
            for i in range(3, numRows+1):
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

        return result

example = Solution()

numRows = 5
result1 = example.generate(numRows = 5)

assert result1 == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print( "result1", result1)