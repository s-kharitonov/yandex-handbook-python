# Простая задача 5.0
# Напишите функцию is_prime, которая принимает натуральное число,
# а возвращает булево значение: True — если переданное число простое, а иначе — False.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
