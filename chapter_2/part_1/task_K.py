# Автоматизация игры
# Всё в том же детском саду ребята очень любят играть с цифрами.
# Одна из таких игр — перестановка цифр четырёхзначного числа.
# Напишите программу для робота-няни, 
# которая из числа вида abcd составляет число badc.

# Формат ввода
# Одно четырёхзначное число.

# Формат вывода
# Одно четырёхзначное число — результат перестановки.
number = input()
print(number[1], number[0], number[3], number[2], sep='')