# Предложение представляет собой последовательность слов, разделенных одинарными пробелами; при этом в начале и в конце строки пробелы отсутствуют. 
# Каждое слово состоит из строчных и прописных букв английского алфавита.
# Предложение можно «перемешать», добавив к каждому слову его порядковый номер (начиная с 1), а затем изменив порядок слов в предложении. 
# Например, предложение «This is a sentence» можно перемешать так: «sentence4 a3 is2 This1» или «is2 sentence4 This1 a3».
# Дано перемешанное предложение $s$, содержащее не более 9 слов. Восстановите и верните исходное предложение.

class Solution:
    def sortSentence(self, s: str) -> str:
        result: str = ""

        words = s.split()
        result_dict = {}

        for elem in words:
            result_dict[int(elem[-1])] = elem[:len(elem) - 1]
        sorted_data = dict(sorted(result_dict.items()))


        for key, value in sorted_data.items():
            result = result+value+" "

        result = result[:len(result)-1]
        return result

example = Solution()

s = "is2 sentence4 This1 a3"
result1 = example.sortSentence(s)
print( "result1", result1)
assert result1 == "This is a sentence"