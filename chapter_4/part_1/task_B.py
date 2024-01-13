# Функциональный НОД
# Напишите функцию gcd, которая принимает два натуральных числа и возвращает их наибольший общий делитель.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def gcd(first_number, second_number):
    max_number = max(first_number, second_number)
    min_number = min(first_number, second_number)

    while (remainder := max_number % min_number) != 0:
        max_number = min_number
        min_number = remainder

    return min_number
