# Простая задача 3.0
# Вспомним, что простые числа — те натуральные числа, у которых два делителя: оно само и 1.
# Напишите программу для определения количества простых чисел среди введённых.
#
# Формат ввода
# В первой строке записано число N Во всех последующих N строках — по одному числу.
#
# Формат вывода
# Требуется вывести общее количество простых чисел среди введённых (кроме N).
numbers_count = int(input())
prime_numbers_count = 0

for i in range(numbers_count):
    number = int(input())

    if number <= 1:
        continue

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            break
    else:
        prime_numbers_count += 1

print(prime_numbers_count)
