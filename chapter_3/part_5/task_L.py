# Разделяй и властвуй
# Напишите утилиту, которая разделяет числа, записанные в файле, на три группы:
#
# числа с преобладающим количеством чётных цифр;
# числа с преобладающим количеством нечётных цифр;
# числа с одинаковым количеством чётных и нечётных цифр.
# Формат ввода
# Пользователь вводит четыре имени файла.
# Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
#
# Формат вывода
# В три другие файла выведите числа, которые подходят под требуемое условие.
# Сохраните положение чисел в строках.
input_file_name = input()
even_numbers_file_name = input()
odd_numbers_file_name = input()
equal_numbers_file_name = input()

even_number_lines = []
odd_number_lines = []
equal_number_lines = []

with open(input_file_name, 'r', encoding='UTF-8') as input_file:
    for line in input_file.readlines():
        numbers = line.split()
        even_numbers = []
        odd_numbers = []
        equal_numbers = []

        for number in numbers:
            number_value = int(number)
            even_digits_count = 0
            odd_digits_count = 0

            while number_value != 0:
                last_digit = number_value % 10
                number_value //= 10

                if last_digit % 2 == 0:
                    even_digits_count += 1
                else:
                    odd_digits_count += 1

            if even_digits_count == odd_digits_count:
                equal_numbers.append(number)
            elif even_digits_count > odd_digits_count:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)

        even_number_lines.append(' '.join(even_numbers))
        odd_number_lines.append(' '.join(odd_numbers))
        equal_number_lines.append(' '.join(equal_numbers))

with open(even_numbers_file_name, 'w', encoding='UTF-8') as even_numbers_file:
    print(*even_number_lines, sep='\n', file=even_numbers_file)
with open(odd_numbers_file_name, 'w', encoding='UTF-8') as odd_numbers_file:
    print(*odd_number_lines, sep='\n', file=odd_numbers_file)
with open(equal_numbers_file_name, 'w', encoding='UTF-8') as equal_numbers_file:
    print(*equal_number_lines, sep='\n', file=equal_numbers_file)
