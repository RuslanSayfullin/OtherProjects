# Следующий больший элемент некоторого элемента x в массиве — это первый больший элемент, расположенный справа от x в том же массиве.
# Вам даны два различных целочисленных массива с индексацией 0, nums1 и nums2, где nums1 является подмножеством nums2.
# Для каждого 0 <= i < nums1.length найдите индекс j такой, что nums1[i] == nums2[j], и определите следующий больший элемент nums2[j] в nums2. 
# Если следующего большего элемента нет, то ответ на этот запрос равен -1.
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Словарь: элемент -> его следующий больший элемент в nums2
        next_greater = {}
        stack = []  # будет хранить элементы, для которых мы ещё не нашли следующий больший
        
        for num in nums2:
            # Пока текущий num больше вершины стека — значит, num является
            # следующим большим элементом для вершины стека
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        # Оставшиеся в стеке элементы не имеют следующего большего — им будет -1
        while stack:
            prev = stack.pop()
            next_greater[prev] = -1
        
        # Формируем ответ для nums1
        return [next_greater[x] for x in nums1]

    
example = Solution()

nums1 = [4,1,2]
nums2 = [1,3,4,2]
result1 = example.nextGreaterElement(nums1, nums2)
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
print( "result1", result1)
assert result1 == [-1,3,-1]

nums1 = [2,4]
nums2 = [1,2,3,4]
result2 = example.nextGreaterElement(nums1, nums2)
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
print( "result2", result2)
assert result2 == [3,-1]

nums1 = [1,3,5,2,4]
nums2 = [5,4,3,2,1]
result3 = example.nextGreaterElement(nums1, nums2)
print( "result3", result3)
assert result3 == [-1,-1,-1,-1,-1]
