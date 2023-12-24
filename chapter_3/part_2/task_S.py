# Частная собственность
# Ребята приносят игрушки в детский сад и играют все вместе.
# Сегодня они решили выяснить, игрушки какого типа принадлежат только одному из детей.
# Напишите программу, которая по списку детей и их игрушек определит «частную собственность».
#
# Формат ввода
# В первой строке задается количество детей в группе (N).
# В каждой из следующих N строк записано имя ребенка и его игрушки в формате:
# Имя: игрушка1, игрушка2, ....
#
# Формат вывода
# Список игрушек, которые есть только у одного из детей в алфавитном порядке.
children_count = int(input())
owners_with_toy_count_by_toy = dict()

for i in range(children_count):
    child, one_owner_toys = input().split(': ')

    for toy in one_owner_toys.split(', '):
        toy_counters_by_owner = owners_with_toy_count_by_toy.get(toy, {})
        counter = toy_counters_by_owner.get(child, 0) + 1

        owners_with_toy_count_by_toy[toy] = toy_counters_by_owner
        owners_with_toy_count_by_toy[toy][child] = counter

one_owner_toys = []

for toy, toy_counters_by_child in owners_with_toy_count_by_toy.items():
    if len(toy_counters_by_child.keys()) == 1:
        one_owner_toys.append(toy)

one_owner_toys.sort()
print('\n'.join(one_owner_toys))
