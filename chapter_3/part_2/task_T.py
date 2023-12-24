# Простая задача 4.0
# Напомним, что взаимно простыми называются числа, которые не имеют общих делителей кроме 1.
# Напишите программу, которая для каждого переданного числа находит список его взаимно простых.
#
# Формат ввода
# Задана последовательность чисел записанных через точку с запятой (;) и пробел.
#
# Формат вывода
# Список чисел с указанием взаимно простых ему среди переданных.
# Все числа должны быть выведены в порядке возрастания без повторений.
# Строки следует отформатировать по правилу:
# число - взаимно простое 1, взаимно простое 2, ...
# Если для числа не было найдено ни одного взаимно простого, то и выводить его не требуется.
numbers = input().split('; ')
prime_numbers_by_number = dict()

for first_number in numbers:
    first_int_value = int(first_number)

    for second_number in numbers:
        second_int_value = int(second_number)

        if first_int_value == second_int_value:
            continue

        max_number = max(first_int_value, second_int_value)
        min_number = min(first_int_value, second_int_value)

        while (remainder := max_number % min_number) != 0:
            max_number = min_number
            min_number = remainder

        if min_number == 1:
            prime_numbers = prime_numbers_by_number.get(first_int_value, set())

            prime_numbers.add(second_int_value)
            prime_numbers_by_number[first_int_value] = prime_numbers

for number in sorted(prime_numbers_by_number.keys()):
    prime_numbers = sorted(prime_numbers_by_number[number])

    if not prime_numbers:
        continue

    result_line = f'{number} - '

    for i, prime_number in enumerate(prime_numbers):
        if i == len(prime_numbers) - 1:
            result_line += str(prime_number)
        else:
            result_line += str(prime_number) + ', '

    print(result_line)
