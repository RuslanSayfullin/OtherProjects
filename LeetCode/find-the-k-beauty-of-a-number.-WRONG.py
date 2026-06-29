# k-красота целого числа num определяется как количество подстрок num, читаемых как строка, удовлетворяющая следующим условиям:
#   Её длина равна k.
#   Она является делителем числа num.
# Дано целое числа num и k, верните k-красивые num.

# Примечание:
# Допускаются ведущие нули.
# 0 не является делителем ни одного значения.
# Подстрока — это непрерывная последовательность символов в строке.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        divisors: int = 0

        for i in range(1, num //2 +1):
            if num % i == 0:
                if str(i) in str(num):
                    if len(str(i)) == k:
                        print(i)
                        divisors += 1

        return divisors
    
example = Solution()

num = 240
k = 2
result1 = example.divisorSubstrings(num, k)
# Explanation: The following are the substrings of num of length k:
# - "24" from "240": 24 is a divisor of 240.
# - "40" from "240": 40 is a divisor of 240.
assert result1 == 2
print( "result1", result1)

num = 430043
k = 2
result2 = example.divisorSubstrings(num, k)
# Explanation: The following are the substrings of num of length k:
# - "43" from "430043": 43 is a divisor of 430043.
# - "30" from "430043": 30 is not a divisor of 430043.
# - "00" from "430043": 0 is not a divisor of 430043.
# - "04" from "430043": 4 is not a divisor of 430043.
# - "43" from "430043": 43 is a divisor of 430043.
assert result2 == 2
print( "result2", result2)
