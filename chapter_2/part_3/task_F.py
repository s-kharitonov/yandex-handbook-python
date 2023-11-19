# НОД
# В одном из местных НИИ часто требуется находить наибольший общий делитель (НОД) двух чисел.
# Вам уже доверяют, как одному из лучших «автоматизаторов» в округе, так что руководство НИИ решило заказать ПО у вас.
#
# Формат ввода
# Вводится два натуральных числа, каждое на своей строке.
#
# Формат вывода
# Требуется вывести одно натуральное число — НОД двух данных чисел.
first_number = int(input())
second_number = int(input())
max_number = max(first_number, second_number)
min_number = min(first_number, second_number)

while (remainder := max_number % min_number) != 0:
    max_number = min_number
    min_number = remainder
print(min_number)
