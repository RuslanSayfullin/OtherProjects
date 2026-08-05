# Получив действительный IP-адрес (IPv4), верните его обезличенную версию.
# Обезличенный IP-адрес заменяет каждую точку "." на "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        for symbol in address:
            if symbol != ".":
                result += symbol
            else:
                result += "[.]"

        return result

example = Solution()

address = "1.1.1.1"
result1 = example.defangIPaddr(address)
assert result1 == "1[.]1[.]1[.]1"
print( "result1", result1)

address = "255.100.50.0"
result2 = example.defangIPaddr(address)
assert result2 == "255[.]100[.]50[.]0"
print( "result2", result2)