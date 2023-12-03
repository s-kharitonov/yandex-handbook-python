# Массовое возведение в степень
# Часто возникают трудности, когда нужно выполнить множество однообразных операций.
# В таких случаях люди желают упростить себе работу.
# Напишите программу, которая возводит в заданную степень все числа, что передали пользователи.
#
# Формат ввода
# Вводится натуральное число N — количество чисел.
# В каждой из последующих N строк записано по одному числу.
# В последней строке записано натуральное число P — степень, в которую требуется возвести числа.
#
# Формат вывода
# Последовательность чисел, являющихся ответом.
numbers_count = int(input())
numbers = []

for i in range(numbers_count):
    numbers.append(int(input()))

power = int(input())

for number in numbers:
    print(number ** power)
