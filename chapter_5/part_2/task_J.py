# Дроби v0.7
# "Остался последний штрих!" Правда звучит как издевательство?
#
# Мы «научили» наши дроби работать с целыми числами и вот теперь надо провернуть обратное действие.
# Реализуйте функционал, который позволит производить все арифметические операции с дробями и числами,
# независимо от их положения (слева или справа) в операторе.
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
        if isinstance(args[0], str) and '/' in args[0]:
            self.n, self.d = map(int, args[0].split('/'))
        elif isinstance(args[0], str):
            self.n, self.d = int(args[0]), 1
        elif len(args) == 1 and isinstance(args[0], int):
            self.n, self.d = args[0], 1
        else:
            self.n, self.d = args
        self.__simplify()

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

    def __simplify(self):
        numerator, denominator = self.n, self.d
        while denominator:
            numerator, denominator = denominator, numerator % denominator
        self.n, self.d = self.n // numerator, self.d // numerator

    def __add__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __radd__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __iadd__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        self.n, self.d = self.n * other.d + other.n * self.d, self.d * other.d
        self.__simplify()
        return self

    def __sub__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.n * other.d - other.n * self.d, self.d * other.d)

    def __rsub__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(other.n * self.d - self.n * other.d, self.d * other.d)

    def __isub__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        self.n, self.d = self.n * other.d - other.n * self.d, self.d * other.d
        self.__simplify()
        return self

    def __mul__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.n * other.n, self.d * other.d)

    def __rmul__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.n * other.n, self.d * other.d)

    def __imul__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        self.n, self.d = self.n * other.n, self.d * other.d
        self.__simplify()
        return self

    def __truediv__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.n * other.d, self.d * other.n)

    def __rtruediv__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.d * other.n, self.n * other.d)

    def __itruediv__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        self.n, self.d = self.n * other.d, self.d * other.n
        self.__simplify()
        return self

    def __lt__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.n / self.d < other.n / other.d

    def __le__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.n / self.d <= other.n / other.d

    def __eq__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.n / self.d == other.n / other.d

    def __ne__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.n / self.d != other.n / other.d

    def __gt__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.n / self.d > other.n / other.d

    def __ge__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.n / self.d >= other.n / other.d

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __str__(self):
        return f'{self.n}/{self.d}'

    def __repr__(self):
        return f"Fraction('{self.n}/{self.d}')"
