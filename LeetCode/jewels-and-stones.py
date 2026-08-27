# Вам даны строки «драгоценные камни», представляющие типы камней, которые считаются драгоценными камнями, и «камни», представляющие камни, которые у вас есть. 
# Каждый символ в строке «камни» обозначает тип камня, который у вас есть. Вам нужно узнать, сколько из ваших камней также являются драгоценными камнями.
# Буквы чувствительны к регистру, поэтому «a» считается другим типом камня, отличным от «A».

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result: int = 0

        for symbol in stones:
            if symbol in jewels:
                result += 1

        return result

example = Solution()
    
jewels = "aA"
stones = "aAAbbbb"
result1 = example.numJewelsInStones(jewels, stones)
assert result1 == 3
print( "result1", result1)