# НОК
# Спустя время НИИ потребовалось находить наименьшее общее кратное (НОК) двух чисел.
# К нам вновь обратились за помощью.
#
# Формат ввода
# Вводится два натуральных числа, каждое на своей строке.
#
# Формат вывода
# Требуется вывести одно натуральное число — НОК двух данных чисел.
first_number = int(input())
second_number = int(input())
max_number = max(first_number, second_number)
min_number = min(first_number, second_number)

while (remainder := max_number % min_number) != 0:
    max_number = min_number
    min_number = remainder

least_common_multiple = (first_number * second_number) // min_number

print(least_common_multiple)
