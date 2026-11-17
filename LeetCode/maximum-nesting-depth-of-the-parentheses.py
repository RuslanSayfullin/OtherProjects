# Для заданной корректной скобочной последовательности s верните её глубину вложенности. 
# Глубина вложенности — это максимальное количество вложенных друг в друга скобок.

class Solution:
    def maxDepth(self, s: str) -> int:
        result: int = 0
        temp_max = 0

        for symbol in s:
            if symbol == "(":
                temp_max += 1
                if temp_max > result:
                    result = temp_max
            elif symbol == ")":
                temp_max -= 1


        return result
    

example = Solution()

s = "(1+(2*3)+((8)/4))+1"
result1 = example.maxDepth(s)
print( "result1", result1)
assert result1 == 3