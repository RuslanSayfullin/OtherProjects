# Вам дано целое число n.
# Нам нужно сгруппировать числа от 1 до n в соответствии с суммой их цифр. Например, числа 14 и 5 принадлежат одной группе, а 13 и 3 — разным.
# Верните количество групп с наибольшим размером, то есть максимальным числом элементов.

class Solution:
    def countLargestGroup(self, n: int) -> int:
        res_dict : dict = {}
        largest: int = 0
        result: int = 0

        memory: dict = {}
        res: int = 0

        for i in range(1, n+1):
            str_i = str(i)
            list_str_i = list(str_i)
            for k in list_str_i:
                res += int(k)

            memory[i] = res
            res = 0

        
        for key, value in memory.items():
            res_dict.setdefault(value, []).append(key)
            
            if len(res_dict[value]) > largest:
                largest = len(res_dict[value])
                result = 0
            if len(res_dict[value]) == largest:
                result +=1

        #print(res_dict, result)
        return result
    
example =Solution()

n = 13
result1 = example.countLargestGroup(n)
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
assert result1 == 4
print( "result1", result1)

n = 2
result2 = example.countLargestGroup(n)
# Explanation:  There are 2 groups [1], [2] of size 1.
assert result2 == 2
print( "result2", result2)