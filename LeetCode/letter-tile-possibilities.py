# У вас есть n tiles плиток, на каждой из которых написана одна буква (из массива `tiles`).
# Верните количество возможных непустых последовательностей букв, которые можно составить, используя буквы с этих плиток.

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)  # сортируем, чтобы легко пропускать дубли
        used = [False] * len(tiles)
        count = 0

        def backtrack():
            nonlocal count
            # каждая непустая собранная строка — это один вариант
            # мы увеличиваем счётчик каждый раз, когда делаем шаг (добавляем букву)
            for i in range(len(tiles)):
                # если уже использовали эту плитку — пропускаем
                if used[i]:
                    continue
                # пропускаем дубликат на этом уровне рекурсии
                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                count += 1  # новая уникальная строка (текущий префикс)
                backtrack()
                used[i] = False

        backtrack()
        return count

example = Solution()

tiles = "AAB"
result1 = example.numTilePossibilities(tiles)
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
print( "result1", result1)
assert result1 == 8