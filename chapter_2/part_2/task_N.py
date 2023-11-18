# Властелин Чисел: Две Башни
# Во времена, когда люди верили в великую силу чисел, оказалось, 
# что волшебник Пифуман предал все народы и стал помогать Зерону.

# Чтобы посетить башни обоих злодеев одновременно,
# нам следует разделить магию числа, которое защищало нас в дороге.

# Чтобы поделить трёхзначное число, нам нужно составить из 
# него минимально и максимально возможные двухзначные числа.

# Формат ввода
# Одно трёхзначное число.

# Формат вывода
# Два защитных числа для каждого отряда, записанные через пробел.
number = int(input())
first_digit = number // 100
second_digit = number // 10 % 10
third_digit = number % 10
max_digit = max(first_digit, second_digit, third_digit)
min_digit = min(first_digit, second_digit, third_digit)
mid_digit = first_digit + second_digit + third_digit - min_digit - max_digit

if min_digit == 0 and mid_digit == 0:
    print(f'{max_digit}0 {max_digit}{max_digit}')
elif min_digit == 0:
    print(f'{mid_digit}{min_digit} {max_digit}{mid_digit}')
else:
    print(f'{min_digit}{mid_digit} {max_digit}{mid_digit}')