# Числовая змейка 2.0
# Воспитательнице вновь нужна программа, которая будет генерировать змейку из чисел.
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
max_digits_count = len(str(height * width))
current_odd_number = 1

for i in range(1, height + 1):
    row = f'{i:>{max_digits_count}} '
    prev_number = i

    for j in range(1, width):
        prev_number += height

        if j % 2 != 0:
            next_number = prev_number + height
            current_number = next_number - current_odd_number
            row += f'{current_number:>{max_digits_count}} '
        else:
            row += f'{prev_number:>{max_digits_count}} '

    current_odd_number += 2
    print(row, end='\n')
