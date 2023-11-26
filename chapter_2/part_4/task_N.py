# Числовая змейка
# Увы, обыкновенные прямоугольники детям быстро наскучили.
# Теперь воспитательнице требуется новая программа.
# Напишите программу, которая строит числовую змейку требуемого размера.
#
# Формат ввода
# В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.
#
# Формат вывода
# Нужно вывести сформированную числовую змейку требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.
height = int(input())
width = int(input())
max_number_digits_count = len(str(height * width))
last_row_number = 0

for i in range(1, height + 1):
    row = ''

    if i % 2 == 0:
        for j in range(last_row_number + width, last_row_number, -1):
            row += f'{j:>{max_number_digits_count}} '
    else:
        for j in range(last_row_number + 1, last_row_number + width + 1):
            row += f'{j:>{max_number_digits_count}} '

    last_row_number += width
    print(row, end='\n')
