# Рациональная считалочка
# Напишите программу, которая производит счёт по заданным параметрам.
#
# Формат ввода
# В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.
#
# Формат вывода
# Последовательность чисел с заданными параметрами.
import itertools

parameters = input().split()
start = float(parameters[0])
end = float(parameters[1])
step = float(parameters[2])

for number in itertools.count(start, step):
    if number > end:
        break

    print(f'{number:.2f}')
