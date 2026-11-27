# Дана строка s и целое число k. Необходимо перевернуть первые k символов в каждом блоке из 2k символов, считая от начала строки.
# Если осталось менее k символов, переверните их все. Если осталось менее 2k, но не менее k символов, то переверните первые k символов, а остальные оставьте без изменений.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = list(s)  # работаем со списком, т.к. строки неизменяемы

        for i in range(0, len(s), 2 * k):
            # Переворачиваем кусок от i до i + k (или до конца строки, если его короче)
            result[i:i + k] = result[i:i + k][::-1]

        return "".join(result)


example = Solution()

s = "abcdefg"
k = 2
result1 = example.reverseStr(s, k)
print( "result1", result1)
assert result1 == "bacdfeg"