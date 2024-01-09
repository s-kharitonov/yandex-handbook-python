# Обновление данных
# Часто приходится обновлять данные.
#
# Создайте программу, которая обновляет JSON файл.
#
# Формат ввода
# Пользователь вводит имя файла.
# Затем вводятся строки вида ключ == значение.
#
# Формат вывода
# В заданный пользователем файл следует записать обновленный JSON.`
from sys import stdin
import json

input_file_name = input()
values_to_update = {}

for line in stdin:
    print(line.rstrip('\n').split(' == '))
    key, value = line.rstrip('\n').split(' == ')
    values_to_update[key] = value

with open(input_file_name, 'r', encoding='UTF-8') as input_file:
    values_by_key = json.load(input_file)

    for key in values_to_update:
        values_by_key[key] = values_to_update[key]

with open(input_file_name, 'w', encoding='UTF-8') as output_file:
    json.dump(values_by_key, output_file, ensure_ascii=False)
