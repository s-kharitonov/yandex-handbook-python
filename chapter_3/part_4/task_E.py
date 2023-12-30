# Список покупок
# Поход в магазин часто вызывает проблемы.
# Если не подготовить список, можно уйти в магазин за хлебом, а вернуться с десятком пакетов.
# Напишите программу, которая собирает пожелания семьи (мамы, папы и дочки) в единый список.
#
# Формат ввода
# В трёх строках записаны желаемые продукты (через запятую и пробел).
#
# Формат вывода
# Отсортированный по алфавиту список продуктов с нумерацией.
#
# Примечание
# Помните, что итераторы можно применять к другим итераторам.
from itertools import chain

first_wish_list = input().split(', ')
second_wish_list = input().split(', ')
third_wish_list = input().split(', ')
common_wish_list = chain(first_wish_list, second_wish_list, third_wish_list)

for number, product in enumerate(sorted(common_wish_list), 1):
    print(f'{number}. {product}')
