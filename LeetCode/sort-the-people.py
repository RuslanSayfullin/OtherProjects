# Вам дан массив строк names и массив heights, состоящий из различных положительных целых чисел. Оба массива имеют длину n.
# Для каждого индекса i, names[i] и heights[i] обозначают имя и рост i-го человека.
# Верните имена, отсортированные в порядке убывания по росту людей.

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        result: list[str] = []

        zipped = list(zip(names, heights))
        zipped.sort(key=lambda a: a[1], reverse=True)

        for element in zipped:
            result.append(element[0])

        return result


example = Solution()
    
names = ["Mary","John","Emma"]
heights = [180,165,170]
result1 = example.sortPeople(names, heights)
# Explanation: Mary is the tallest, followed by Emma and John.
assert result1 == ["Mary","Emma","John"]
print( "result1", result1)

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
result2 = example.sortPeople(names, heights)
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
assert result2 == ["Bob","Alice","Bob"]
print( "result2", result2)
        
        