# НОД 3.0
# Местному НИИ в очередной раз нужно находить наибольший общий делитель (НОД) нескольких чисел.
# Руководство института вернулось с этой задачей к нам.
#
# Формат ввода
# В единственной строке записывается последовательность натуральных чисел, разделённых пробелами.
#
# Формат вывода
# Требуется вывести одно натуральное число — НОД всех данных чисел.
#
# Примечание
# Самый распространенный способ поиска НОД — Алгоритм Эвклида.
numbers = input().split()
prev_gcd = int(numbers[0])

for i in range(1, len(numbers)):
    current_number = int(numbers[i])
    max_number = max(prev_gcd, current_number)
    min_number = min(prev_gcd, current_number)

    while (remainder := max_number % min_number) != 0:
        max_number = min_number
        min_number = remainder

    prev_gcd = min_number

print(prev_gcd)
