# Классная точка 5.0
# Согласитесь, что использовать операторы куда удобнее, чем обыкновенные методы.
# Давайте вспомним о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.
#
# При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной
# на заданное кортежем расстояние по осям x и y.
# При выполнении кода point += (x, y) производится перемещение изначальной точки.
#
# Напомним, что сейчас мы модернизируем только класс PatchedPoint.
#
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 2:
            x, y = args
            super().__init__(x, y)
        else:
            x, y = args[0]
            super().__init__(x, y)

    def __add__(self, other):
        x, y = other
        return PatchedPoint(self.x + x, self.y + y)

    def __iadd__(self, other):
        x, y = other
        self.move(x, y)
        return self

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'
