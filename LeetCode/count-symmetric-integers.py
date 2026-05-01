# Вам даны два положительных целых числа: low и high.
# Целое число x, состоящее из 2 * n цифр, является симметричным, если сумма первых n цифр x равна сумме последних n цифр x. 
# Числа с нечетным числом цифр никогда не являются симметричными.
# Возвращает количество симметричных целых чисел в диапазоне [low, high].

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        quantity = 0

        for counter in range(low, high+1):
            rangelen = len(str(counter))
            if rangelen % 2 == 0:

                bound = (len(str(counter)) // 2)
                left = (str(counter))[0: bound]
                right = (str(counter))[bound: rangelen]

                digitsleft = sum([int(d) for d in left])
                digitsright = sum([int(d) for d in right])

               
                if digitsleft == digitsright:
                    #print(counter, digitsleft, digitsright)
                    quantity += 1

            
 
        return quantity
    

low = 1
high = 100
example = Solution()
result1 = example.countSymmetricIntegers(low, high) # There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
print("result1", result1)

low = 1200
high = 1230
result2 = example.countSymmetricIntegers(low, high) # There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
print("result2", result2)

