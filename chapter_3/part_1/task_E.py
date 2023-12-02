# А роза упала на лапу Азора 4.0
# Вернёмся к палиндромам — числам, словам и предложениям, которые читаются одинаково в оба направления.
# Напишите программу, которая определяет, относится ли введённая строка к палиндромам.
#
# Формат ввода
# Вводится строка.
#
# Формат вывода
# Требуется вывести YES — если введенная строка является палиндромом, иначе – NO.
phrase = input()
is_palindrome = True

for i, letter in enumerate(phrase):
    current_letter_pair = phrase[-i - 1]

    if letter != current_letter_pair:
        is_palindrome = False
        break

if is_palindrome:
    print('YES')
else:
    print('NO')
