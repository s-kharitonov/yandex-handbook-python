# Меню питания 2.0
# В детском саду ежедневно подают новую кашу на завтрак.
#
# Напишите программу, которая строит расписание каш на ближайшие дни.
#
# Формат ввода
# Вводится натуральное число M — количество каш в меню.
# В каждой из последующих M строк записано одно название каши.
# В конце передается натуральное число N — количество дней.
#
# Формат вывода
# Вывести список каш в порядке подачи.
#
# Примечание
# Советуем изучить документацию на функцию itertools.islice, которая реализует срезы на основе итераторов.
from itertools import islice

porridge_count = int(input())
porridge = [input() for i in range(porridge_count)]
days_count = int(input())
whole_parts_count = days_count // len(porridge)
remainder_elements_count = days_count % len(porridge)
whole_part = porridge * whole_parts_count
remainder = list(islice(porridge, remainder_elements_count))
result = whole_part + remainder

print('\n'.join(result))
