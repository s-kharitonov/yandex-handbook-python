# А роза упала на лапу Азора 5.0
# И снова напишем программу, которая определяет, палиндромом перед нами или нет.
#
# Формат ввода
# Вводится строка.
#
# Формат вывода
# Если введённая строка относится к палиндрому, то вывести YES, а иначе — NO.
#
# Примечание
# При проверке не обращайте внимания на регистр и пробелы.
phrase = input()
left_pointer = 0
right_pointer = len(phrase) - 1
is_palindrome = True

while left_pointer < right_pointer:
    left_char = phrase[left_pointer]
    right_char = phrase[right_pointer]

    if left_char.isspace():
        left_pointer += 1
        continue
    if right_char.isspace():
        right_pointer -= 1
        continue
    if left_char.lower() != right_char.lower():
        is_palindrome = False
        break
    else:
        left_pointer += 1
        right_pointer -= 1

if is_palindrome:
    print('YES')
else:
    print('NO')
