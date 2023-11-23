# Не таблица умножения
# Фабрика вернулась с новой задачкой — другим вариантом таблицы умножения.
# Она нужна в виде списка. Продолжим помогать местному бизнесу.
#
# Формат ввода
# Вводится одно натуральное число — требуемый размер «таблицы».
#
# Формат вывода
# Не таблица умножения заданного размера.
rows_count = int(input())

for i in range(rows_count):
    second_number = i + 1

    for j in range(rows_count):
        first_number = j + 1
        print(f'{first_number} * {second_number} = {first_number * second_number}')
