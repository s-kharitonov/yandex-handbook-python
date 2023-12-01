# Новогоднее настроение 2.0
# Коллеги математика вновь хотят порадовать его и сделать математические ёлки, которые украсят кабинет учёного.
# Помогите им, написав программу, которая по введённому числу строит математическую ёлку.
#
# Формат ввода
# Вводится одно натуральное число — количество чисел в математической ёлке.
#
# Формат вывода
# Требуемая новогодня ёлка.
numbers_count = int(input())
triangle_number = 0
n = 2

while triangle_number < numbers_count:
    triangle_number = (n * (n + 1)) / 2
    n += 1

n -= 2
start = int((n * (n + 1)) / 2 + 1)
max_row_length = -1

for i in range(start, numbers_count + 1):
    max_row_length += len(str(i)) + 1

print(f'{1:^{max_row_length}}')
row_number = 2
counter = 2

while counter <= numbers_count:
    row = ''
    row_triangle_number = (row_number * (row_number + 1)) / 2

    while counter <= min(row_triangle_number, numbers_count):
        if counter < row_triangle_number:
            row += f'{counter} '
        else:
            row += f'{counter}'
        counter += 1

    print(f'{row:^{max_row_length}}')
    row_number += 1
