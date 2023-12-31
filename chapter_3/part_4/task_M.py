# Расстановка спортсменов
# Расстановка спортсменов на старте — сложная задача.
# Однако при помощи итераторов она решается за пару строк.
# Напишите программу, которая выводит список возможных расстановок спортсменов на старте.
#
# Формат ввода
# В первой строке задано натуральное число N — количество спортсменов.
# В следующих N строках записаны имена спортсменов.
#
# Формат вывода
# Отсортированный по алфавиту список расстановок.
# Имена в каждой строке выводить через запятую и пробел.
from itertools import product

athletes_count = int(input())
athletes = [input() for i in range(athletes_count)]

athletes.sort()

for arrangement in product(athletes, repeat=athletes_count):
    if len(set(arrangement)) == athletes_count:
        print(*arrangement, sep=', ')
