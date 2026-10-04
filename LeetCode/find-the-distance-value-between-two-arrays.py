# Даны два целочисленных массива arr1 и arr2, а также целое число d.
# Необходимо вернуть значение расстояния между этими массивами.
# Значение расстояния определяется как количество таких элементов arr1[i], для которых не существует ни одного элемента arr2[j], 
# удовлетворяющего условию |arr1[i] - arr2[j]| <= d.

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result: int = 0

        for i in arr1:
            flag: bool = False
            for i2 in arr2:
                if abs(i-i2) <= d:
                    flag = True
                    break

            if not flag:
                result += 1

        return result

example = Solution()

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
result1 = example.findTheDistanceValue(arr1, arr2, d)
# Explanation: For arr1[0]=4 we have: 
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# For arr1[1]=5 we have: 
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2
assert result1 == 2
print( "result1", result1)

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
result2 = example.findTheDistanceValue(arr1, arr2, d)
assert result2 == 2
print( "result2", result2)

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6
result3 = example.findTheDistanceValue(arr1, arr2, d)
assert result3 == 1
print( "result3", result3)

