# Дана строка s. Разбейте строку s на части так, чтобы каждая из них была палиндромом. 
# Верните все возможные варианты такого разбиения строки s.
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        res = []
        path = []

        # Предпосчёт палиндромов: dp[i][j] == True, если s[i:j+1] — палиндром
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        def backtrack(start: int):
            if start == n:
                res.append(path.copy())
                return
            for end in range(start, n):
                if dp[start][end]:           # s[start:end+1] — палиндром
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()               # откат

        backtrack(0)
        return res

example = Solution()

s = "aab"
result1 = example.partition(s)
assert result1 == [["a","a","b"],["aa","b"]]
print( "result1", result1)

s = "a"
result2 = example.partition(s)
assert result2 == [["a"]]
print( "result2", result2)

s = "ab"
result3 = example.partition(s)
assert result3 == [["a","b"]]
print( "result3", result3)

s = "efe"
result4 = example.partition(s)
assert result4 == [["e","f","e"],["efe"]]
print( "result4", result4)