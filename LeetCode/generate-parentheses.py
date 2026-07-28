# Даны n пар скобок. Напишите функцию для генерации всех комбинаций правильно сформированных скобок.
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_string: str, open_count: int, close_count: int):
            # Базовый случай: если длина строки равна 2*n, комбинация готова
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Вариант 1: Добавляем '(', если лимит не исчерпан
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # Вариант 2: Добавляем ')', если их меньше, чем открывающих
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        # Запуск рекурсии с пустой строкой и нулевыми счетчиками
        backtrack("", 0, 0)
        return result
    
example = Solution()
    
n = 3
result1 = example.generateParenthesis(n)
assert result1 == ["((()))","(()())","(())()","()(())","()()()"]
print( "result1", result1)

n = 1
result2 = example.generateParenthesis(n)
assert result2 == ["()"]
print( "result2", result2)