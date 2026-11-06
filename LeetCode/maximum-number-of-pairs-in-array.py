# Дан целочисленный массив `nums` (индексация начинается с 0). За одну операцию можно выполнить следующее:
# - Выбрать два равных числа в массиве `nums`. 
# - Удалить оба этих числа из `nums`, сформировав из них пару.
# - Эту операцию можно повторять до тех пор, пока это возможно.
# Верните целочисленный массив `answer` размера 2 (с индексацией от 0), где `answer[0]` — количество сформированных пар, 
# а `answer[1]` — количество чисел, оставшихся в `nums` после того, как все возможные операции были выполнены.
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        answer: list[int] = []
        cnt_nums = Counter(nums)

        summa = 0
        ostatok = 0

        for _, value in cnt_nums.items():
            if value % 2 == 0:
                summa += (value / 2)
            elif value % 2 != 0:
                if value > 1:
                    summa += (value // 2)
                    ostatok += (value % 2)
                else:
                    ostatok += value

        answer.append(int(summa))
        answer.append(int(ostatok))
        return answer


example = Solution()

nums = [1,3,2,1,3,2,2]
result1 = example.numberOfPairs(nums)
# Explanation:
# Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
# Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
# Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
# No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

print( "result1", result1)
assert result1 == [3,1]