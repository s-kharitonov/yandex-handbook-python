# Автоматизация списка
# Многим весьма часто приходится вести списки продуктов, дел и так далее.
#
# Напишите программу, которая преобразует введённую строку в нумерованный список.
#
# Формат ввода
# Вводится одна строка.
#
# Формат вывода
# Требуется вывести нумерованный список, составленный из её слов.
words = input().split()

for number, word in enumerate(words, 1):
    print(f'{number}. {word}')
