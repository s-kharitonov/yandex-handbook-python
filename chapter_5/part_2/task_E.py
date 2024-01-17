# Дроби v0.2
# Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
#
# Предусмотрите возможность задать отрицательные числитель и/или знаменатель.
# А также перепишите методы __str__ и __repr__ таким образом,
# чтобы информация об объекте согласовывалась с инициализацией строкой.
#
# Далее реализуйте оператор математического отрицания — унарный минус.
#
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать
# (называть с использованием ведущих символов нижнего подчёркивания).
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
