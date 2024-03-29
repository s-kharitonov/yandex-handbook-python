# Корень зла
# Не все любят математику, а кто-то даже считает её настоящим злом во плоти, хотя от неё никуда не деться. 
# К примеру, Python изначально разрабатывался только для решения математических задач, 
# поэтому давайте используем его, чтобы найти корни уравнения.

# Формат ввода
# Вводится 3 вещественных числа a, b, c — коэффициенты уравнения вида:
# ax^2+bx+c=0.

# Формат вывода
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».

# Примечание
# Обратите внимание, что ограничения на значения коэффициентов отсутствуют.
import math

a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c

if a == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0:
    print('No solution')
elif a == 0:
    print(f'{-c / b:.2f}')
elif d < 0:
    print('No solution')
elif d == 0:
    print(f'{-b / (2 * a):.2f}')
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f'{min(x1, x2):.2f} {max(x1, x2):.2f}')
    