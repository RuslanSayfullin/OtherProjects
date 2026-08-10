# Дано целое число, верните количество шагов, необходимых для его приведения к нулю.
# За один шаг, если текущее число четное, его нужно разделить на 2, в противном случае — вычесть из него 1.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        result: int = 0

        while num != 0:
            if num % 2 != 0:
                num -= 1
                result += 1
            else:
                num = num / 2
                result += 1

        return result

    
example = Solution()
    
num = 14
result1 = example.numberOfSteps(num)
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
assert result1 == 6
print( "result1", result1)

num = 8
result2 = example.numberOfSteps(num)
# Explanation: 
# Step 1) 8 is even; divide by 2 and obtain 4. 
# Step 2) 4 is even; divide by 2 and obtain 2. 
# Step 3) 2 is even; divide by 2 and obtain 1. 
# Step 4) 1 is odd; subtract 1 and obtain 0.
assert result2 == 4
print( "result2", result2)
