# Простая задача
# Один из самых интересных видов чисел в математике — простые числа.
# Их объединяет то, что делятся они лишь на 1 и само себя.
# До сих пор их изучают учёные по всему миру.
# Также они применяются в вычислительной технике: с их помощью можно писать алгоритмы, чтобы шифровать данные.
# Давайте напишем программу, чтобы определять — простое перед нами число или нет.
#
# Формат ввода
# Вводится одно натуральное число.
#
# Формат вывода
# Требуется вывести сообщение YES если число простое, иначе — NO.
#
# Примечание
# Простым называется число, которое имеет ровно два делителя.
import math
number = int(input())


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if is_prime(number):
    print('YES')
else:
    print('NO')
