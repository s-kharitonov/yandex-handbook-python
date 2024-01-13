# Модернизация системы вывода
# Разработайте функцию modern_print, которая принимает строку и выводит её, если она не была выведена ранее.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.
prev_prints = set()


def modern_print(line):
    if line not in prev_prints:
        prev_prints.add(line)
        print(line)
