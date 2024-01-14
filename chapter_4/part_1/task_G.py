# Шахматный «обед»
# Напишите функцию can_eat, которая принимает положение коня и другой фигуры в виде кортежей из двух координат,
# а возвращает булево значение: True если конь съедает фигуру и False иначе.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def can_eat(knight_position, piece_position):
    x = abs(knight_position[0] - piece_position[0])
    y = abs(knight_position[1] - piece_position[1])
    return x + y == 3