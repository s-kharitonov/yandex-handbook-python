# Властелин Чисел: Возвращение Цезаря
# До победы над злом остался один шаг — разрушить логово Зерона.

# Для этого нужно создать трёхзначное магическое число, 
# которое будет сильнее двух двухзначных защитных чисел Зерона.

# Самый простой способ создать сильное число:

# первой взять максимальную цифру из всех защитных чисел;
# последней — минимальную;
# в середину поставить сумму оставшихся без учёта переноса разряда.
# Помогите одолеть зло.

# Формат ввода
# В двух строках записаны защитные числа Зерона.

# Формат вывода
# Одно трёхзначное число, которое приведёт к победе.
first_defense_number = int(input())
second_defense_number = int(input())
first_digit = first_defense_number // 10
second_digit = first_defense_number % 10
third_digit = second_defense_number // 10
fourth_digit = second_defense_number % 10
first_strong_digit = max(first_digit, second_digit, third_digit, fourth_digit)
third_strong_digit = min(first_digit, second_digit, third_digit, fourth_digit)
digits_sum = first_digit + second_digit + third_digit + fourth_digit
second_strong_digit = (digits_sum - first_strong_digit - third_strong_digit) % 10

print(f'{first_strong_digit}{second_strong_digit}{third_strong_digit}')