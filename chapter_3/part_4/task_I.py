# Таблица умножения 3.0
# Местная фабрика канцелярских товаров заказала программу, которая генерирует таблицы умножения.
# Давайте поможем производителю.
#
# Формат ввода
# Вводится одно натуральное число — требуемый размер таблицы.
#
# Формат вывода
# Таблица умножения заданного размера.
#
# Примечание
# itertools.product отличный способ, чтобы избавиться от вложенных циклов.
from itertools import product

table_size = int(input())
numbers = [number for number in range(1, table_size + 1)]

for first_number, second_number in product(numbers, numbers):
    if second_number != table_size:
        print(first_number * second_number, end=' ')
    else:
        print(first_number * second_number)
