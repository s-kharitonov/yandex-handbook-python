# Работа не волк
# Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов.
# Каждая должность имеет собственный оклад (заработную плату за час работы).
# В нашей импровизированной компании существуют 3 должности:
#
# Junior — с окладом 10 тугриков в час;
# Middle — с окладом 15 тугриков в час;
# Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
# Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю).
# Класс реализует следующие методы:
#
# work(time) — отмечает новую отработку в количестве часов time;
# rise() — повышает программиста;
# info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <
# накопленная зарплата>тгр.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Programmer:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.worked_time = 0
        self.rise_count = 0
        self.salary_rates = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20,
        }
        self.salary = 0

    def work(self, time):
        self.worked_time += time
        self.salary += time * (self.salary_rates[self.grade] + self.rise_count)

    def rise(self):
        match self.grade:
            case 'Junior':
                self.grade = 'Middle'
            case 'Middle':
                self.grade = 'Senior'
            case 'Senior':
                self.rise_count += 1

    def info(self):
        return f'{self.name} {self.worked_time}ч. {self.salary}тгр.'
