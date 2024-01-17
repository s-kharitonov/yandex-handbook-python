# Классный прямоугольник 2.0
# Расширим функционал класса написанного вами в предыдущей задаче.
#
# Реализуйте методы:
#
# get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
# get_size() — возвращает размеры в виде кортежа;
# move(dx, dy) — изменяет положение на заданные значения;
# resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Все результаты вычислений нужно округлить до сотых.

class Rectangle:

    def __init__(self, left, right):
        left_x, left_y = left
        right_x, right_y = right
        self.left_angle_x = left_x
        self.left_angle_y = left_y
        self.right_angle_x = right_x
        self.right_angle_y = right_y
        self.top_left_x = round(min(left_x, right_x), 2)
        self.top_left_y = round(max(left_y, right_y), 2)
        self.bottom_right_x = round(max(left_x, right_x), 2)
        self.bottom_right_y = round(min(left_y, right_y), 2)
        self.width = abs(left_x - right_x)
        self.height = abs(left_y - right_y)

    def get_pos(self):
        return self.top_left_x, self.top_left_y

    def get_size(self):
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx, dy):
        left_angle = self.left_angle_x + dx, self.left_angle_y + dy
        right_angle = self.right_angle_x + dx, self.right_angle_y + dy
        self.__init__(left_angle, right_angle)

    def resize(self, width, height):
        left_angle = self.get_pos()
        right_angle = self.top_left_x + width, self.top_left_y - height
        self.__init__(left_angle, right_angle)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)
