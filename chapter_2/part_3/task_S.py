# Игра в «Угадайку»
# Давайте сымитируем игру «Угадайка» между двумя людьми.
# Для этого нужно написать программу, которая отгадывает загаданное целое число от 1 до 1000 включительно.
# Пользователь (или тестирующая система) загадывает число и не сообщает его вашей программе.
# Угадать число нужно не более, чем за 10 попыток.
#
# На каждую попытку пользователь отвечает одной из фраз:
#
# Больше;
# Меньше;
# Угадал!
# Данная задача проверяется интерактивно. Другими словами,
# пока вы не выведите своё число, система не предоставит вам данных.
number = 500
max_number = 1000
min_number = 1

print(number)

while (result := input()) != 'Угадал!':
    if result == 'Меньше':
        max_number = number - 1
    else:
        min_number = number + 1

    pivot = (max_number - min_number) // 2
    number = min_number + pivot
    print(number)
