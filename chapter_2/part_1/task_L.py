# Интересное сложение
# Один малыш из детского сада услышал от старшей сестры 
# о некоем действии с числами — сложении.
# И как это часто бывает — он не до конца разобрался, как работает сложение. 
# Например, не совсем понял, как произвести перенос разряда.
# Теперь он хочет научить сложению остальных ребят и просит написать программу, 
# которая поможет ему в качестве наглядного материала.

# Формат ввода
# В первой и второй строках записаны натуральные числа меньше 1000.

# Формат вывода
# Одно число — результат сложения введённых чисел без учёта переносов.
number_1 = int(input())
number_2 = int(input())
first_result_digit = (int(number_1 / 100) + int(number_2 / 100)) % 10
second_result_digit = (int(number_1 / 10 % 10) + int(number_2 / 10 % 10)) % 10
third_result_digit = (int(number_1 % 10) + int(number_2 % 10)) % 10

if first_result_digit > 0:
    print(first_result_digit, second_result_digit, third_result_digit, sep='')
elif second_result_digit > 0 and first_result_digit == 0:
    print(second_result_digit, third_result_digit, sep='')
else:
    print(third_result_digit)
