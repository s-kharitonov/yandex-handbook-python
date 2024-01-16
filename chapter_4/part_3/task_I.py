# Циклический генератор
# Напишите генератор cycle, который принимает список и работает аналогично итератору itertools.cycle.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def cycle(collection):
    while True:
        for element in collection:
            yield element
