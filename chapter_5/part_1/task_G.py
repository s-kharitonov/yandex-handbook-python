# Классный прямоугольник 3.0
# Необходимо ещё немного доработать предыдущую задачу.
#
# Разработайте методы:
#
# turn() — поворачивает прямоугольник на 90&deg; по часовой стрелке вокруг его центра;
# scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
# Все вычисления производить с округлением до сотых.
#
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Rectangle:

    def __init__(self, coord1, coord2):
        self.left = min(coord1[0], coord2[0])
        self.top = max(coord1[1], coord2[1])
        self.right = max(coord1[0], coord2[0])
        self.bottom = min(coord1[1], coord2[1])
        self.width = round(abs(coord1[0] - coord2[0]), 2)
        self.height = round(abs(coord1[1] - coord2[1]), 2)
        self.x = min(coord1[0], coord2[0])
        self.y = max(coord1[1], coord2[1])
        self.flag = False

    def perimeter(self):
        return round(abs(self.left - self.right) * 2 + abs(self.top - self.bottom) * 2, 2)

    def area(self):
        return round(abs(self.left - self.right) * abs(self.top - self.bottom), 2)

    def get_pos(self):
        return self.left, self.top

    def get_size(self):
        if self.flag:
            return self.width, self.height
        return round(abs(self.left - self.right), 2), round(abs(self.top - self.bottom), 2)

    def resize(self, width, height):
        self.flag = False
        self.right = round(self.left + width, 2)
        self.bottom = round(self.top + height, 2)
        self.width, self.height = width, height

    def turn(self):
        self.flag = False
        width, height = self.get_size()
        d = (width - height) / 2
        self.left = round(self.left + d, 2)
        self.right = round(self.right - d, 2)
        self.top = round(self.top + d, 2)
        self.bottom = round(self.bottom - d, 2)
        d = (self.width - self.height) / 2
        self.x = round(self.x + d, 2)
        self.y = round(self.y + d, 2)
        self.width, self.height = self.height, self.width

    def scale(self, factor):
        self.flag = False
        width, height = self.get_size()
        self.flag = False
        if abs(width - self.width) <= 0.01:
            width = self.width
        if abs(height - self.height) <= 0.02:
            height = self.height
        self.left = round(self.left - (factor * width - width) / 2, 2)
        self.top = round(self.top + (factor * height - height) / 2, 2)
        width = round(width * factor, 2)
        height = round(height * factor, 2)
        self.right = round(self.left + width, 2)
        self.bottom = round(self.top - height, 2)
        self.x = round(self.x - (factor * self.width - self.width) / 2, 2)
        self.y = round(self.y + (factor * self.height - self.height) / 2, 2)
        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)
