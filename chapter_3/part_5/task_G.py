# Файловая статистика
# Напишите программу, которая для заданного файла вычисляет следующие параметры:
#
# количество всех чисел;
# количество положительных чисел;
# минимальное число;
# максимальное число;
# сумма всех чисел;
# среднее арифметическое всех чисел с точностью до двух знаков после запятой.
# Формат ввода
# Пользователь вводит имя файла.
# Файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
#
# Формат вывода
# Выведите статистику в указанном порядке.
file_name = input()

with open(file_name, 'r', encoding='UTF-8') as file_in:
    numbers_count = 0
    positive_numbers_count = 0
    min_number = 0
    max_number = 0
    numbers_sum = 0
    avg_number = 0

    for line in file_in:
        numbers = line.split()
        numbers_count += len(numbers)

        for number in numbers:
            int_number = int(number)

            if int_number > 0:
                positive_numbers_count += 1
            min_number = min(min_number, int_number)
            max_number = max(max_number, int_number)
            numbers_sum += int_number

    print(numbers_count)
    print(positive_numbers_count)
    print(min_number)
    print(max_number)
    print(numbers_sum)
    print(round(numbers_sum / numbers_count, 2))
