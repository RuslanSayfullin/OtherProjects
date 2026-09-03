# Вам дан целочисленный таймер, представляющий оставшееся время (в секундах) работы светофора.
# Светофор подчиняется следующим правилам:
# Если таймер == 0, сигнал «зеленый»
# Если таймер == 30, сигнал «оранжевый»
# Если 30 < таймер <= 90, сигнал «красный»
# Верните текущее состояние сигнала. Если ни одно из вышеперечисленных условий не выполняется, верните «Недопустимое значение».

class Solution:
    def trafficSignal(self, timer: int) -> str:
        result: str = "Invalid"

        if timer == 0:
            result = "Green"
        elif timer == 30:
            result = "Orange"
        elif 30 < timer <= 90:
            result = "Red"
        else:
            pass

        return result

example = Solution()
    
timer = 60
result1 = example.trafficSignal(timer)
assert result1 == "Red"
# Explanation: Since timer = 60, and 30 < timer <= 90, the answer is "Red".
print( "result1", result1)

timer = 5
result2 = example.trafficSignal(timer)
assert result2 == "Invalid"
# Explanation: Since timer = 5, it does not satisfy any of the given conditions, the answer is "Invalid".
print( "result2", result2)