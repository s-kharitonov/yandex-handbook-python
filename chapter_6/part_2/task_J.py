# Экстремум функции
# Экстремум в математике — максимальное или минимальное значение функции на заданном множестве.
#
# Чаще всего математики для поиска экстремума функции прибегают к её дифференцированию.
# Однако мы можем обойти этот трудоёмкий процесс и схитрить.
#
# Напишите три функции:
#
# values(func, start, end, step), строящую Series значений функции в точках диапазона и принимающую:
# функцию одной переменной;
# начало диапазона;
# конец диапазона;
# шаг вычисления;
# min_extremum(data) возвращает точку, в которой был достигнут минимум на диапазоне;
# max_extremum(data) возвращает точку, в который был достигнут максимум на диапазоне.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import numpy as np
import pandas as pd


def values(func, start, end, step):
    index = np.arange(start, end + step, step)
    return pd.Series(map(func, index), index=index, dtype='float64')


def min_extremum(data):
    return min(data[data == min(data)].index)


def max_extremum(data):
    return max(data[data == max(data)].index)
