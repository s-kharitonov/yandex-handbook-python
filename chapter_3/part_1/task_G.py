# А и Б сидели на трубе
# Сложение чисел весьма простая задача.
# К сожалению, пользователи не всегда вводят данные так, как нам удобно.
#
# Формат ввода
# Два целых числа, разделённые пробелом.
#
# Формат вывода
# Одно целое число — сумма переданных чисел.
numbers = input().split()
numbers_sum = int(numbers[0]) + int(numbers[1])

print(numbers_sum)
