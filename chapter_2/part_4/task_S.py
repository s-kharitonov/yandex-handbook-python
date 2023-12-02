# Числовой квадрат
# К сожалению, и змейки детям надоели, поэтому воспитательнице нужна новая программа.
# Напишите программу, которая строит числовой квадрат требуемого размера.
#
# Формат ввода
# В первой строке записано число N — высота и ширина числового квадрата.
#
# Формат вывода
# Требуется вывести сформированный числовой квадрат требуемого размера.
# Чтобы квадрат был красивым, каждый его столбец — одинаковой ширины.
square_size = int(input())
cell_width = len(str((square_size + 1) // 2))

for i in range(1, square_size + 1):
    for j in range(1, square_size + 1):
        number = min(i, j, square_size - i + 1, square_size - j + 1)
        print(f'{number:>{cell_width}}', end=' ')
    print()
