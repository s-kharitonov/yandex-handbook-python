# Стек
# Ещё одной полезной коллекцией является стек реализующий принцип «Последний пришёл – первый ушёл».
# Его часто представляют как стопку карт или магазин пистолета, где приходящие элементы закрывают
# выход уже находящимся в коллекции.
#
# Реализуйте класс Stack, который не имеет параметров инициализации, но поддерживает методы:
#
# push(item) — добавить элемент в конец стека;
# pop() — «вытащить» первый элемент из стека;
# is_empty() — проверяет стек на пустоту.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
