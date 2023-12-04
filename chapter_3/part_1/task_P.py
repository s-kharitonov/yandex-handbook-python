# Анонс новости 2.0
# Попробуем ещё раз сократить заголовки для статей в ленте новостного сайта.
# Давайте сделаем программу, которая сокращает длинный заголовок
# до требуемой длины и завершает его многоточием ..., если это требуется.
#
# Формат ввода
# Вводится натуральное число L — необходимая длина заголовка.
# Вводится натуральное число N — количество строк в заголовке новости.
# В каждой из последующих N строк записано по одной строке заголовка.
#
# Формат вывода
# Сокращённый заголовок.
max_title_length = int(input()) - 3
title_lines_count = int(input())
title_length = 0

for i in range(title_lines_count):
    title_line = input()
    title_line_length = len(title_line)

    if title_line_length + title_length < max_title_length:
        title_length += title_line_length
        print(title_line)
    else:
        print(title_line[:max_title_length - title_length] + '...')
        break
