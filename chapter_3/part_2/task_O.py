# Двоичная статистика!
# У программистов особые отношения с двоичной системой счисления.
# Продолжим тренировки в статистической обработке данных и проанализируем данные числа.
# Напишите программу, которая для переданных чисел вычисляет:
#
# - количество разрядов;
# - количество единиц;
# - количество нулей.

# Формат ввода
# Вводится последовательность чисел, записанных через пробел.
#
# Формат вывода
# Вывести список словарей с требуемой статистикой.
#
# Примечание
# Вывод в примерах отформатирован только для визуальной наглядности.
# Все пробельные символы при проверке игнорируются.
# Порядок словарей обязан совпадать с порядком переданных чисел.
# Порядок ключей в словаре не имеет значения.
numbers = input().split()
numbers_statistics = []

for number in numbers:
    int_value = int(number)
    units_counter = 0
    zeros_counter = 0
    digits_counter = 0

    while int_value > 0:
        last_digit = int_value % 2

        if last_digit == 1:
            units_counter += 1
        elif last_digit == 0:
            zeros_counter += 1

        digits_counter += 1
        int_value //= 2

    numbers_statistics.append({
        'digits': digits_counter,
        'units': units_counter,
        'zeros': zeros_counter
    })

print(numbers_statistics)
