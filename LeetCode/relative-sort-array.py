# Даны два массива arr1 и arr2. Элементы массива arr2 различны, и все элементы массива arr2 также присутствуют в массиве arr1.
# Отсортируйте элементы массива arr1 так, чтобы относительный порядок элементов в arr1 совпадал с порядком в arr2. 
# Элементы, отсутствующие в arr2, следует поместить в конец массива arr1 в порядке возрастания.
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sort_array: list = []
        sort_array2: list = []
        
        arr1.sort()

        for element in arr2:

            for i in range(len(arr1)):

                if element == arr1[i]:
                    sort_array.append(arr1[i])


        for element in arr1:
            if element not in arr2:
                sort_array2.append(element)


        sort_array += sort_array2
        return sort_array
    
example = Solution()

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
result1 = example.relativeSortArray(arr1, arr2)
assert result1 == [2,2,2,1,4,3,3,9,6,7,19]
print( "result1", result1)

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
result2 = example.relativeSortArray(arr1, arr2)
assert result2 == [22,28,8,6,17,44]
print( "result2", result2)

