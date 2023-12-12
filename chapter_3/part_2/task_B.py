# Символическая разница
# А ещё в промышленных задачах часто требуется находить общее среди данных, полученных из разных источников.
# Напишите программу, которая по двум строкам определяет их общие символы.
#
# Формат ввода
# Вводится две строки.
#
# Формат вывода
# Требуется вывести все символы этой строки без повторений.
# Порядок вывода не имеет значения.
first_line = input()
second_line = input()
unique_letters_first_line = set(first_line)
unique_letters_second_line = set(second_line)
lines_intersection = unique_letters_first_line & unique_letters_second_line

print(''.join(lines_intersection))
