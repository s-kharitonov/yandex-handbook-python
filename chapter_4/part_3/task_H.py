# Генератор Фибоначчи
# Числа Фибоначчи весьма интересная последовательность и используется в различных математических задачах.
# В ней каждый следующий элемент равен сумме двух предыдущих.
# Математики начинают эту последовательность с двух единиц, но мы же с вами программисты,
# поэтому привыкли вести счет с нуля.
#
# Напишите генератор fibonacci, который последовательно возвращает заданное количество чисел Фибоначчи
# по "правилам программистов".
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def fibonacci(number):
    first_number = 0
    second_number = 1
    for i in range(number):
        yield first_number
        first_number, second_number = second_number, first_number + second_number
