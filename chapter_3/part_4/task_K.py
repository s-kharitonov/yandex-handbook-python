# Числовой прямоугольник 3.0
# Ребята в детском саду вновь учатся считать, и воспитательница решила сделать так,
# чтобы им было проще освоить новый навык.
# Для этого она хочет оформить список изучаемых чисел особым образом.
# Дети справляются весьма быстро, поэтому ей требуется программа, которая способна строить числовые прямоугольники.
# Напишите программу, которая строит числовой прямоугольник требуемого размера.
#
# Формат ввода
# В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.
#
# Формат вывода
# Нужно вывести сформированный числовой прямоугольник требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец должен быть одинаковой ширины.
#
# Примечание
# itertools.product прекрасно подходит, чтобы избавиться от вложенных циклов.
from itertools import product

height = int(input())
width = int(input())
lines = range(1, height + 1)
line_numbers = range(1, width + 1)
max_number = height * width
max_number_digits_count = 0

while max_number > 0:
    max_number //= 10
    max_number_digits_count += 1

for i, line_with_number in enumerate(product(lines, line_numbers)):
    line, number = line_with_number
    value = ((line - 1) * width) + number
    if (i + 1) % width == 0:
        print(f'{value:{max_number_digits_count}}', end='\n')
    else:
        print(f'{value:{max_number_digits_count}}', end=' ')
