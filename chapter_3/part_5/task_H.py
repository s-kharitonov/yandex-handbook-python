# Файловая разница
# Напишите программу, которая определяет, какие слова есть только в одном из файлов.
#
# Формат ввода
# Пользователь вводит три имени файлов.
# Каждый из входных файлов содержит произвольное количество слов, разделённых пробелами и символами перевода строки.
#
# Формат вывода
# В третий файл выведите в алфавитном порядке без повторений список слов, которые есть только в одном из файлов.
first_file_name = input()
second_file_name = input()
result_file_name = input()

with open(first_file_name, 'r', encoding='UTF-8') as first_file:
    first_file_things = set(thing for line in first_file for thing in line.split())
with open(second_file_name, 'r', encoding='UTF-8') as second_file:
    second_file_things = set(thing for line in second_file for thing in line.split())
with open(result_file_name, 'w', encoding='UTF-8') as result_file:
    print(*sorted(first_file_things.symmetric_difference(second_file_things)), sep='\n', file=result_file)
