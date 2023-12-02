# Математическая выгода
# Математик Виталий Евгеньевич задумался над вопросом выгоды систем счисления.
# Он решил, что выгодной системой счисления будет являться та,
# в которой число имеет наибольшую сумму цифр.
# Напишите программу, которая по введённому числу определяет основание системы счисления с максимальной выгодой.
#
# Формат ввода
# Одно натурально число.
#
# Формат вывода
# Одно натуральное число из диапазона [2;10] — основание системы счисления с максимальной выгодой.
# Если таких оснований несколько, выбирается наименьшее.
number = int(input())
max_digits_sum = 0
max_base = 0

for i in range(2, 10 + 1):
    counter = number
    digits_sum = 0

    while counter > 0:
        last_digit = counter % i
        digits_sum += last_digit
        counter //= i

    if digits_sum > max_digits_sum:
        max_digits_sum = digits_sum
        max_base = i

print(max_base)
