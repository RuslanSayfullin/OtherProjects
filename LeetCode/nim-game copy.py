# Вы играете в следующую игру «Ним» со своим другом:
# * Изначально на столе лежит куча камней.
# * Вы и ваш друг будете по очереди ходить, и вы ходите первым.
# * В каждом ходу тот, чей ход, убирает от 1 до 3 камней из кучи.
# * Побеждает тот, кто уберет последний камень.
# Дано n, количество камней в куче. Верните true, если вы можете выиграть игру, предполагая, что и вы, и ваш друг играете оптимально, в противном случае верните false.

class Solution:
    def canWinNim(self, n: int) -> bool:
        
        can_win: bool = False
        steps: list = [1, 2, 3]
        minstep = 1

        if n < max(steps):
            can_win = True
            return can_win
        
        
        stepi = True
        while n != 0:
            
            if stepi:
                print(n, stepi)
                if n in steps:
                    n = 0
                    can_win = True
                    return can_win
        
                # мой ход
                if n + minstep > 3:
                    


                if (n - 1) > 1:
                    n -= 1
                    stepi = False
                elif (n - 2) > 2:
                    n -= 2
                    stepi = False
                elif (n - 3) > 3:
                    n -= 3
                    stepi = False
                else:
                    n = 0
                    can_win = False
                    return can_win
            elif not stepi:
                print(n, stepi)
                if n in steps:
                    n = 0
                    can_win = False
                    return can_win

                # ход оппонента
                if (n - 1) > 1:
                    n -= 1
                    stepi = True
                elif (n - 2) > 2:
                    n -= 2
                    stepi = True
                elif (n - 3) > 3:
                    n -= 3
                    stepi = True
                else:
                    n = 0
                    can_win = True
                    return can_win

        return can_win
"""
n = 4
example = Solution()
result1 = example.canWinNim(n)
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
assert result1 == False
print("result1", result1)

n = 1
example = Solution()
result2 = example.canWinNim(n)
assert result2 == True
print("result2", result2)

n = 2
example = Solution()
result3 = example.canWinNim(n)
assert result3 == True
print("result3", result3)

n = 4
example = Solution()
result4 = example.canWinNim(n)
assert result4 == False
print("result4", result4)

n = 5
example = Solution()
result5 = example.canWinNim(n)
assert result5 == True
print("result5", result5)
"""
n = 6
example = Solution()
result6 = example.canWinNim(n)
assert result6 == True
print("result6", result6)

