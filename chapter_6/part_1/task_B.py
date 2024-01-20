# Потоковый НОД
# Напишите программу, находящую наибольшие общие делители для всех переданных
# в стандартный поток последовательностей чисел.
#
# Формат ввода
# Вводятся строки чисел, разделённых пробелами.
#
# Формат вывода
# Последовательность чисел — наибольшие общие делители всех последовательностей.
import math
from sys import stdin

for line in stdin:
    numbers = map(int, line.rstrip('\n').split())
    print(math.gcd(*numbers))