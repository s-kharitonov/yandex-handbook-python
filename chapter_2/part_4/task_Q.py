# А роза упала на лапу Азора 3.0
# Вернёмся к палиндромам. Напишите программу, которая определяет количество палиндромов в переданном списке.
#
# Формат ввода
# В первой строке записано число N Во всех последующих N строках указано по одному числу.
#
# Формат вывода
# Требуется вывести общее количество палиндромов среди введённых чисел (кроме числа N).
numbers_count = int(input())
palindrome_count = 0

for i in range(numbers_count):
    number = int(input())
    number_copy = number
    reversed_number = ''

    while number_copy != 0:
        reversed_number += str(number_copy % 10)
        number_copy //= 10

    if int(reversed_number) == number:
        palindrome_count += 1

print(palindrome_count)
