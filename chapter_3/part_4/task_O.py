# Список покупок 3.0
# В этот раз семья договорилась о том, что в целях экономии бюджета, они будут совершать в день только три покупки.
# Напишите программу, которая готовит варианты списков покупок.
#
# Формат ввода
# В первой строке задано натуральное число N — количество членов семьи.
# В следующих N строках записаны желаемые продукты (через запятую и пробел).
#
# Формат вывода
# Варианты списков покупок в алфавитном порядке.
from itertools import chain, product

family_members_count = int(input())
wish_lists = [input().split(', ') for i in range(family_members_count)]
wish_list = chain.from_iterable(wish_lists)

for products_list in product(sorted(wish_list), repeat=3):
    if len(set(products_list)) == 3:
        print(*products_list, sep=' ')
