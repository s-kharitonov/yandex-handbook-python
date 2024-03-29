# На старт! Внимание! Марш!
# По правилам велогонки, после квалификации каждый гонщик
# стартует с задержкой на секунду больше, чем у гонщика перед ним.
# Первый гонщик стартует на счёт 3.
# Напишите программу, которая сможет автоматизировать старт всех гонщиков, участвующих в велогонке.
#
# Формат ввода
# Вводится одно натуральное число — количество участников велогонки.
#
# Формат вывода
# Требуется вывести отсчёт.
racers_count = int(input())

for i in range(racers_count):
    for j in range(i + 3, 0, -1):
        print(f'До старта {j} секунд(ы)')
    else:
        print(f'Старт {i + 1}!!!')
