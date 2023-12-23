# Зайка — 10
# Поможем детям разобраться, что именно они увидели рядом с зайками.
#
# Формат ввода
# В каждой строке записано описание придорожной местности.
# Конец ввода обозначается пустой строкой.
#
# Формат вывода
# Определите список увиденного рядом с зайками без повторений.
# Порядок вывода не имеет значения.
#
# Примечание
# Считается, что объект находится рядом, если он записан справа или слева от требуемого.
hare_neighbors = set()

while terrain_description := input():
    things = terrain_description.split()

    for i, thing in enumerate(things):
        if thing.lower() != 'зайка':
            continue
        if i - 1 >= 0:
            prev_thing = things[i - 1]
            hare_neighbors.add(prev_thing)
        if i + 1 <= len(things) - 1:
            next_thing = things[i + 1]
            hare_neighbors.add(next_thing)

print('\n'.join(hare_neighbors))
