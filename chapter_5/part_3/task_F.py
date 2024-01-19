# Корень зла 2
# В одной из первых лекций вы уже решали задачу о поиске корней уравнения. Давайте модернизируем её.
#
# Напишите функцию find_roots, принимающую три параметра:
# коэффициенты уравнения и возвращающую его корни в виде кортежа из двух значений.
#
# Так же создайте два собственных исключения NoSolutionsError и InfiniteSolutionsError,
# которые будут вызваны в случае отсутствия и бесконечного количества решений уравнения соответственно.
#
# Если переданные коэффициенты не являются рациональными числами, вызовите исключение TypeError.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.

class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if sum(1 for i in (a, b, c) if type(i) not in (int, float)):
        raise TypeError

    d = b ** 2 - 4 * a * c

    if a == 0 and c == 0:
        raise InfiniteSolutionsError
    elif a == 0 and b == 0:
        raise NoSolutionsError
    elif a == 0:
        return -c / b
    elif d < 0:
        raise NoSolutionsError
    elif d == 0:
        return -b / (2 * a), -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return min(x1, x2), max(x1, x2)
