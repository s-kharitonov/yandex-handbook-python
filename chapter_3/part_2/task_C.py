# Зайка — 8
# Продолжаем считать заек за окном поезда.
#
# Формат ввода
# В первой строке записано натуральное число N — количество выделенных придорожных местностей.
# В каждой из N последующих строк записано описание придорожной местности.
#
# Формат вывода
# Вывести все найденные объекты в придорожных местностях.
terrain_descriptions_count = int(input())
objects = set()

for i in range(terrain_descriptions_count):
    terrain_description = input()
    current_description_objects = terrain_description.split()

    objects.update(current_description_objects)

print('\n'.join(objects))
