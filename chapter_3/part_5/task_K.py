# Файловая статистика 2.0
# Напишите программу, которая для заданного файла вычисляет следующие параметры:
#
# количество всех чисел;
# количество положительных чисел;
# минимальное число;
# максимальное число;
# сумма всех чисел;
# среднее арифметическое всех чисел с точностью до двух знаков после запятой.
# Формат ввода
# Пользователь вводит два имени файла.
# Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
#
# Формат вывода
# Выведите статистику во второй файл в формате JSON.
#
# Ключи значений задайте соответственно:
#
# count — количество всех чисел;
# positive_count — количество положительных чисел;
# min — минимальное число;
# max — максимальное число;
# sum — сумма всех чисел;
# average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.
import json

file_name = input()
result_file_name = input()

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

with open(result_file_name, 'w', encoding='UTF-8') as result_file:
    json.dump({
        "count": numbers_count,
        "positive_count": positive_numbers_count,
        "min": min_number,
        "max": max_number,
        "sum": numbers_sum,
        "average": round(numbers_sum / numbers_count, 2),
    }, result_file, ensure_ascii=False)
