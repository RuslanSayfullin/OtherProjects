# Даны две строки, s и goal. Верните true, если можно поменять местами два символа в строке s так, чтобы она стала равна goal, в противном случае верните false.
# Под обменом символов понимается выбор двух индексов i и j (нумерация с нуля), таких что i != j, и перестановка символов s[i] и s[j] местами. 
# Например, обмен символов по индексам 0 и 2 в строке "abcd" дает "cbad".

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Случай 1: разная длина — невозможно
        if len(s) != len(goal):
            return False

        # Случай 2: строки равны
        if s == goal:
            # Нужно, чтобы был хотя бы один повторяющийся символ
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

        # Случай 3: строки разные — ищем позиции различий
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                # Если различий больше двух, одним обменом не исправить
                if len(diff) > 2:
                    return False

        # Должно быть ровно два различия
        if len(diff) != 2:
            return False

        i, j = diff[0], diff[1]
        # Проверяем, что обмен делает строки равными
        return s[i] == goal[j] and s[j] == goal[i]

example = Solution()

s = "ab"
goal = "ba"
result1 = example.buddyStrings(s, goal)
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
assert result1
print( "result1", result1)

s = "ab"
goal = "ab"
result2 = example.buddyStrings(s, goal)
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
assert not result2
print( "result2", result2)

s = "aa"
goal = "aa"
result3 = example.buddyStrings(s, goal)
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
assert result3
print( "result3", result3)

s = "aaaaaaabc"
goal = "aaaaaaacb"
result4 = example.buddyStrings(s, goal)
assert result4
print( "result4", result4)