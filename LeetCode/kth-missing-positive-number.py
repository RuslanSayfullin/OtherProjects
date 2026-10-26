# Дан массив arr, состоящий из положительных целых чисел, отсортированных в строго возрастающем порядке, а также целое число k.
# Верните k-е по счету положительное целое число, отсутствующее в этом массиве.

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        result: int = 0

        last = (arr[-1]+k+1)
        count = 0

        for i in range(1, last):
            if i not in arr:
                count += 1
                print(i)
                if count == k:
                    result = i
                    break

        return result

example = Solution()

arr = [2,3,4,7,11]
k = 5
result1 = example.findKthPositive(arr, k)
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
assert result1 == 9
print( "result1", result1)

arr = [1,2,3,4]
k = 2
result2 = example.findKthPositive(arr, k)
assert result2 == 6
print( "result2", result2)