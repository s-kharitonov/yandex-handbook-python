# Зайка — 7
# Вновь поищем заек за окном поезда.
#
# Формат ввода
# В первой строке записано натуральное число N — количество выделенных придорожных местностей.
# В каждой из N последующих строк записано описание придорожной местности.
#
# Формат вывода
# Для каждой строки нужно найти положение первого зайки.
# Если в строке нет заек, то об этом нужно непременно сообщить.
terrain_descriptions_count = int(input())

for i in range(terrain_descriptions_count):
    terrain_description = input()
    first_hare_position = terrain_description.find('зайка')

    if first_hare_position != - 1:
        print(first_hare_position + 1)
    else:
        print('Заек нет =(')
