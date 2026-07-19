# Верните количество перестановок чисел от 1 до n, при которых простые числа находятся в индексах простых чисел (с индексом 1).
# (Напомним, что целое число является простым тогда и только тогда, когда оно больше 1, 
# и не может быть записано как произведение двух положительных целых чисел, оба меньших его.)
# Поскольку ответ может быть большим, верните ответ по модулю 10^9 + 7.

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Функция проверки простоты числа
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        # Считаем количество простых чисел от 1 до n
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime_count = n - prime_count

        # Вычисляем факториал с учётом модуля
        def factorial_mod(k: int) -> int:
            res = 1
            for i in range(2, k + 1):
                res = (res * i) % MOD
            return res

        fact_p = factorial_mod(prime_count)
        fact_np = factorial_mod(non_prime_count)

        return (fact_p * fact_np) % MOD
    

example =Solution()

digits = 5
result1 = example.numPrimeArrangements(digits)
# For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
assert result1 == 12
print( "result1", result1)