# Длина числа
# Разработайте функцию number_length, которая принимает одно целое число и возвращает его длину без учёта знака.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def number_length(number):
    counter = 0
    absolute_number = abs(number)
    while absolute_number > 0:
        absolute_number //= 10
        counter += 1
    return counter
