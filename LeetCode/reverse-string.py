# Напишите функцию, которая переворачивает строку. Входная строка задана в виде массива символов s.
# Это необходимо сделать, изменяя входной массив на месте с использованием дополнительной памяти O(1).


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

        for index in range(len(s) // 2):
            s[index], s[-index-1] = s[-index-1], s[index]
            print(index, s)

example = Solution()

s = ["h","e","l","l","o"]
example.reverseString(s)
assert s == ["o","l","l","e","h"]

s = ["H","a","n","n","a","h"]
example.reverseString(s)
assert s == ["h","a","n","n","a","H"]

  