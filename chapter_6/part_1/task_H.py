# Числовая змейка 3.0
# Когда-то вы помогали детсадовцам с различными змейками. Давайте реализуем её на основе массивов.
#
# Напишите функцию snake, которая принимает ширину (M) и высоту (N) змейки, а также именованный параметр direction.
#
# Параметр direction могут принимать значения:
#
# H — горизонтальная змейка, используется по умолчанию;
# V — вертикальная змейка.
# Функция должна вернуть матрицу, представляющую змейку, с ячейками типа int16.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import numpy as np


def snake(width, height, direction='H'):
    array = np.arange(1, width * height + 1, dtype=np.int16)
    if direction == 'H':
        matrix = array.reshape(height, width)
        matrix[1::2] = np.flip(matrix[1::2], axis=1)
        return matrix
    matrix = array.reshape(width, height)
    matrix[1::2] = np.flip(matrix[1::2], axis=1)
    return matrix.transpose()
