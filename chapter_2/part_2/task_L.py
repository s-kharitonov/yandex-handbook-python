# Музыкальный инструмент
# Есть много музыкальных инструментов, но Вася обожает треугольник.

# У него завалялось немного алюминиевых трубочек разной длины, и он задаётся вопросом, 
# а можно ли из них сделать любимый музыкальный инструмент.

# Формат ввода
# Три числа — длины трубочек, каждое с новой строки.

# Формат вывода
# YES — если Васе удастся создать музыкальный треугольник, иначе — NO

# Примечание
# Обратите внимание, что в треугольнике любая сторона меньше суммы двух других.
first_number = int(input())
second_number = int(input())
third_number = int(input())
first_sum = first_number + second_number
second_sum = second_number + third_number
third_sum = first_number + third_number

if first_sum > third_number and second_sum > first_number and third_sum > second_number:
    print('YES')
else:
    print('NO')