# Редизайн таблицы умножения
# Согласитесь, что предыдущие таблицы умножения выглядят не очень красиво.
# Давайте зададим для всех столбцов одинаковую ширину, а значения в ячейках выровним по центру.
# И да, заказчик попросил ещё добавить в таблицу рамки между ячейками.
#
# Формат ввода
# В первой строке записан требуемый размер таблицы. Во второй строке — ширина столбцов.
#
# Формат вывода
# Таблица умножения заданного размера и вида.
size = int(input())
column_width = int(input())

for i in range(1, size + 1):
    row = ''
    row_last_number = size * i

    for j in range(i, row_last_number + 1, i):
        if j != row_last_number:
            row += f'{j: ^{column_width}}|'
        else:
            row += f'{j: ^{column_width}}'
    print(row)

    if i != size:
        print('-' * (size * column_width + size - 1))