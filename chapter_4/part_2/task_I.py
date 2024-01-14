# Чётная фильтрация
# Напишите lambda выражение для фильтрации чисел с чётной суммой цифр.
#
# Примечание
# В решении не должно быть ничего, кроме выражения.
#
lambda number: sum([int(digit) for digit in str(number)]) % 2 == 0
