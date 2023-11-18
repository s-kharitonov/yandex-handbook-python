# Властелин Чисел: Братство общей цифры
# Во времена магии и драконов существовало мнение, 
# что числа обладают великой силой, способной изменить мир.

# Всё началось с написания великих чисел. Три числа были переданы эльфам. 
# Семь — отданы повелителям гномов. А девять... были переданы человеческому роду.

# Но все они оказались обмануты, потому что существовало ещё одно число. 
# В стране Нумия на бумаге из тёмного папируса властелин Зерон 
# тайно написал Единую Цифру, подчиняющую себе все великие числа.

# Давайте выясним, что это за цифра.

# Формат ввода
# В первой строке записано двузначное число одного из эльфов.
# Во второй строке — Гномов.
# В третьей — Людей.

# Формат вывода
# Одна цифра — общая у всех трёх чисел в одинаковой позиции
elf_number = int(input())
dwarf_number = int(input())
human_number = int(input())
first_elf_digit = elf_number // 10

if first_elf_digit == dwarf_number // 10 == human_number // 10:
    print(first_elf_digit)
else:
    print(elf_number % 10)
    