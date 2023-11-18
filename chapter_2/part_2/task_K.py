# Красота спасёт мир
# Одно из древних поверий гласит, что трёхзначное число красиво, 
# если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.

# Напишите систему определяющую красоту числа.

# Формат ввода
# Одно трёхзначное число

# Формат вывода
# YES — если число красивое, иначе — NO
number = int(input())
first_number = number // 100
second_number = number // 10 % 10
third_number = number % 10
min = min(first_number, second_number, third_number)
max = max(first_number, second_number, third_number)
sum = min + max

if min < first_number < max and sum == first_number * 2:
    print('YES')
elif min < second_number < max and sum == second_number * 2:
    print('YES')
elif min < third_number < max and sum == third_number * 2:
    print('YES')
else:
    print('NO')