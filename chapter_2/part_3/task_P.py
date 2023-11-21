# А роза упала на лапу Азора 2.0
# Вспомним о палиндромах, которые в обоих направлениях читаются одинаково.
# Напишите программу, которая проверяет, является ли число палиндромом.
#
# Формат ввода
# Одно натуральное число.
#
# Формат вывода
# YES — если число является палиндромом, иначе — NO.
number = int(input())
number_copy = number
reversed_number = ''

while number_copy != 0:
    reversed_number += str(number_copy % 10)
    number_copy = number_copy // 10

if int(reversed_number) == number:
    print('YES')
else:
    print('NO')
