# Числовая строка
# Разработайте функцию split_numbers,
# которая принимает строку целых чисел, разделённых пробелами, и возвращает кортеж из этих чисел.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
#
# Вы можете спросить: почему кортеж, а не список.
# Всё дело в безопасности.
# Кортежи неизменяемые коллекции и их безопаснее передавать в функцию или из неё.

def split_numbers(numbers):
    return tuple(int(number) for number in numbers.split())
