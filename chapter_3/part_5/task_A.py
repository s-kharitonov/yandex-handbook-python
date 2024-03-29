# A+B+...
# Наконец-то мы можем обрабатывать данные, не имея ни малейшего понятия об их количестве.
#
# Напишите программу, которая находит сумму всех чисел введённых пользователем.
#
# Формат ввода
# Вводятся строки чисел.
#
# Формат вывода
# Одно число — сумма всех чисел в потоке ввода.
from sys import stdin

sum = 0

for line in stdin:
    numbers = line.split()

    for number in numbers:
        sum += int(number)

print(sum)
