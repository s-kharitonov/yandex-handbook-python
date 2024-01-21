# Лесенка
# Напишите функцию stairs, принимающую вектор и возвращающую матрицу,
# в которой каждая строка является копией вектора со смещением.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import numpy as np


def stairs(vector):
    vector_length = len(vector)
    matrix = np.zeros((vector_length, vector_length), dtype=int)

    for i in range(vector_length):
        matrix[i] = np.roll(vector, i)

    return matrix
