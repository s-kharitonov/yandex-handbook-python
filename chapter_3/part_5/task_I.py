# Файловая чистка
# Python в первую очередь скриптовый язык. Такие языки часто используются для создания консольных утилит.
#
# Напишите простую утилиту, которая очищает заданный файл от:
#
# повторяющихся пробелов;
# повторяющихся символов перевода строки;
# табуляций,
# излишних пробелов в начале и конце строк.
# Формат ввода
# Пользователь вводит два имени файлов.
# Входной файл содержит неформатированный текст произвольной длины.
#
# Формат вывода
# Во второй файл выведите очищенный текст.
input_file_name = input()
output_file_name = input()
result_lines = []

with open(input_file_name, 'r', encoding='UTF-8') as input_file:
    for line in input_file.readlines():
        stripped_line = line.strip()
        result_line = ''

        for i in range(0, len(stripped_line)):
            current_symbol = stripped_line[i]
            next_symbol = stripped_line[i + 1] if i + 1 < len(stripped_line) else None

            if current_symbol.isspace() and next_symbol and next_symbol.isspace():
                continue
            if current_symbol == '\n' and next_symbol and next_symbol == '\n':
                continue
            if current_symbol == '\t':
                continue

            result_line += current_symbol

        if result_line:
            result_lines.append(result_line)

with open(output_file_name, 'w', encoding='UTF-8') as output_file:
    print(*result_lines, sep='\n', file=output_file)
