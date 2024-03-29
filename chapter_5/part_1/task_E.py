# Классный прямоугольник
# Давайте перейдём к более сложным геометрическим фигурам.
#
# Разработайте класс Rectangle.
#
# При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника
# (со сторонами параллельными осям координат).
#
# Класс должен реализовывать методы:
#
# perimeter — возвращает периметр прямоугольника;
# area — возвращает площадь прямоугольника.
# Все результаты вычислений нужно округлить до сотых.
#
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Rectangle:

    def __init__(self, left_angle, right_angle):
        self.first_line = abs(left_angle[0] - right_angle[0])
        self.second_line = abs(left_angle[1] - right_angle[1])

    def perimeter(self):
        return round(2 * (self.first_line + self.second_line), 2)

    def area(self):
        return round(self.first_line * self.second_line, 2)
