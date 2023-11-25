# НОД 2.0
# В одном из местных НИИ часто требуется находить наибольший общий делитель (НОД) нескольких чисел.
# Вам уже доверяют, так что вновь пришли с этой задачей.
#
# Формат ввода
# В первой строке записано одно число N — количество данных.
# В каждой из последующих N строк записано по одному натуральному числу.
#
# Формат вывода
# Требуется вывести одно натуральное число — НОД всех данных чисел (кроме N).
numbers_count = int(input())
prev_gcd = int(input())

for i in range(numbers_count - 1):
    current_number = int(input())
    max_number = max(prev_gcd, current_number)
    min_number = min(prev_gcd, current_number)

    while (remainder := max_number % min_number) != 0:
        max_number = min_number
        min_number = remainder

    prev_gcd = min_number

print(prev_gcd)
