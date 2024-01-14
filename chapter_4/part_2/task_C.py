# Функциональный нод 2.0
# Напишите функцию gcd, которая вычисляет наибольший общий делитель последовательности чисел.
# Параметрами функции выступают натуральные числа в произвольном количестве, но не менее одного.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def gcd(*numbers):
    prev_gcd = numbers[0]

    for i in range(1, len(numbers)):
        current_number = numbers[i]
        max_number = max(prev_gcd, current_number)
        min_number = min(prev_gcd, current_number)

        while (remainder := max_number % min_number) != 0:
            max_number = min_number
            min_number = remainder

        prev_gcd = min_number

    return prev_gcd
