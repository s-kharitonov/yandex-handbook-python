# Дроби v0.5
# Следующим этапом разработки будет реализация методов сравнения: >, <, >=, <=, ==, !=.
#
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче,
# следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
#
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            self.n, self.d = map(int, args[0].split('/'))
        else:
            self.n, self.d = args
        self.__simplify()

    def __simplify(self):
        numerator, denominator = self.n, self.d
        while denominator:
            numerator, denominator = denominator, numerator % denominator
        self.n, self.d = self.n // numerator, self.d // numerator

    def __add__(self, other):
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __iadd__(self, other):
        self.n, self.d = self.n * other.d + other.n * self.d, self.d * other.d
        self.__simplify()
        return self

    def __sub__(self, other):
        return Fraction(self.n * other.d - other.n * self.d, self.d * other.d)

    def __isub__(self, other):
        self.n, self.d = self.n * other.d - other.n * self.d, self.d * other.d
        self.__simplify()
        return self

    def __mul__(self, other):
        return Fraction(self.n * other.n, self.d * other.d)

    def __imul__(self, other):
        self.n, self.d = self.n * other.n, self.d * other.d
        self.__simplify()
        return self

    def __truediv__(self, other):
        return Fraction(self.n * other.d, self.d * other.n)

    def __itruediv__(self, other):
        self.n, self.d = self.n * other.d, self.d * other.n
        self.__simplify()
        return self

    def __lt__(self, other):
        return self.n / self.d < other.n / other.d

    def __le__(self, other):
        return self.n / self.d <= other.n / other.d

    def __eq__(self, other):
        return self.n / self.d == other.n / other.d

    def __ne__(self, other):
        return self.n / self.d != other.n / other.d

    def __gt__(self, other):
        return self.n / self.d > other.n / other.d

    def __ge__(self, other):
        return self.n / self.d >= other.n / other.d

    def reverse(self):
        self.n, self.d = self.d, self.n
        self.__simplify()
        return self

    def numerator(self, number=0):
        if not number:
            return abs(self.n)
        if self.n > 0:
            self.n = abs(number)
            self.__simplify()
            if number < 0:
                self.n = -self.n
        elif self.n < 0:
            self.n = abs(number)
            self.__simplify()
            if number > 0:
                self.n = -self.n
        return abs(self.n)

    def denominator(self, number=0):
        if not number:
            return self.d
        if self.n > 0:
            self.d = abs(number)
            self.__simplify()
            if number < 0:
                self.n = -self.n
        elif self.n < 0:
            self.n = abs(self.n)
            self.d = abs(number)
            self.__simplify()
            if number > 0:
                self.n = -self.n
        return self.d

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __str__(self):
        return f'{self.n}/{self.d}'

    def __repr__(self):
        return f"Fraction('{self.n}/{self.d}')"
