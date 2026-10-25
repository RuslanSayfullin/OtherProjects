# Дана матрица `grid` размера `m x n`, элементы которой отсортированы в порядке невозрастания как по строкам, так и по столбцам. 
# Верните количество отрицательных чисел в этой матрице.

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        result: int = 0

        for element in grid:
            for i in element:
                if i < 0:
                    result += 1
        
        return result

example = Solution()

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
result1 = example.countNegatives(grid)
# Explanation: There are 8 negatives number in the matrix.
assert result1 == 8
print( "result1", result1)