# А роза упала на лапу Азора 6.0
# Мы уже писали программы, которые определяли, а палиндром перед нами или нет.
# Давайте теперь найдём все слова-палиндромы среди введённых строк.
#
# Формат ввода
# Вводятся слова.
#
# Формат вывода
# Список слов-палиндромов в алфавитном порядке без повторений.
#
# Примечание
# При проверке слов не обращайте внимание на регистр.
from sys import stdin

palindromes = []

for line in stdin:
    words = line.split()
    words[-1] = words[-1].rstrip('\n')

    for word in words:
        is_palindrome = True

        for i, letter in enumerate(word):
            letter_pair = word[-i - 1]
            if letter.lower() != letter_pair.lower():
                is_palindrome = False
                break

        if is_palindrome:
            palindromes.append(word)

print(*sorted(set(palindromes)), sep='\n')
