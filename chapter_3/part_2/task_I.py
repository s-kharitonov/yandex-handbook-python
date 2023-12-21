# Зайка — 9
# Поможем детям подсчитать, сколько за окном поезда встречается животных и деревьев каждого вида.
#
# Формат ввода
# В каждой строке записано описание придорожной местности.
# Конец ввода обозначается пустой строкой.
#
# Формат вывода
# Список увиденного и их количество.
# Порядок вывода не имеет значения.
things_by_count = dict()

while (terrain_description := input()) != '':
    things = terrain_description.split()

    for thing in things:
        counter = things_by_count.get(thing, 0)
        counter += 1
        things_by_count[thing] = counter

for thing in things_by_count:
    print(f'{thing} {things_by_count[thing]}')
