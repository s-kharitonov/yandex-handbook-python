# Шахматная подготовка
# Представьте, что вы пишете компьютерную игру «Шахматы».
# Вам надо смоделировать шахматную доску, которая представляет собой матрицу.
# Чёрная клетка представляется нулём, а белая — единицей.
# Если смотреть на доску сверху, то левая верхняя клетка — белая.
#
# Напишите функцию make_board, которая принимает размер шахматной доски,
# и возвращает матрицу, моделирующую заданную доску.
#
# Установите тип элементов матрицы int8.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import numpy as np

BLACK = 0
WHITE = 1


def get_square_color(x, y):
    if x % 2 == 0 and y % 2 == 0 or x % 2 != 0 and y % 2 != 0:
        return WHITE
    return BLACK


def make_board(size):
    squares_generator = np.vectorize(get_square_color, otypes=[np.int8])
    return np.fromfunction(squares_generator, (size, size))
