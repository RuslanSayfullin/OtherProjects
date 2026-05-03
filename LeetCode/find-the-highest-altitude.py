# Мотоциклист отправляется в автомобильное путешествие. 
# Путешествие состоит из n + 1 точек на разных высотах. Мотоциклист начинает свое путешествие в точке 0, на высоте, равной 0.
# Вам дан целочисленный массив gain длиной n, где gain[i] — это чистый прирост высоты между точками i и i + 1 для всех (0 <= i < n). 
# Верните максимальную высоту точки.
from typing import List
from itertools import accumulate

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        trassa = [0,] + gain
        res_it = accumulate(trassa)
        res = list(res_it)

        return max(res)


gain = [-5,1,5,0,-7]
example = Solution()
result1 = example.largestAltitude(gain)
assert result1 == 1
print(result1)

gain = [-4,-3,-2,-1,4,3,2]
result2 = example.largestAltitude(gain)
assert result1 == 0
print(result2)

        